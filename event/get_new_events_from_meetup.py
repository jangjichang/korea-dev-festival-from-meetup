"""
https://www.meetup.com/ko-KR/meetup_api/
"""
import requests
from datetime import datetime, timedelta

from django.core.files.base import ContentFile
import django
django.setup()
from event.models import MeetupCrawling, Category

korea_meetup_dev_group = {
    'GDG-Seoul', 'awskrug', 'HashedLounge', 'seoul-tech-society',
    'IBM-developerWorks-Meetup', 'KryptoSeoul', 'codeseoul',
    'Seoul-Cloud-Foundry-Meetup', 'Hyperledger-Korea', 'OracleDeveloperKR',
    'GDG-Cloud-Korea', 'Korea-Ravencoin', 'GDG-WebTech', 'golangskynet',
    'Hongdae-Machine-Learning-Study', 'Seoul-Startup-Founders-101',
    'theslowtech', 'BlockchainROK', 'Cloud-Native-Computing-Seoul',
    'Internet-of-Things-Korea-Meetup', 'react-native-seoul', 'graphdatabase',
    'Cosmos-Seoul', 'Korea-Blockchain-Hub', 'KOREASLUG', 'Software-QA'
}

MIMETYPE = {
    "image/bmp": '.bmp',
    'image/jpeg': '.jpg',
    'image/png': '.png',
}


def save_new_events_from_meetup_dev_group(korea_meetup_dev_group):
    event_dict = dict()
    for group in korea_meetup_dev_group:
        url = 'https://api.meetup.com/%s/events?&sign=true&photo-host=public&page=50&fields=group_key_photo,featured_photo' % (
            group)
        response = requests.get(url)
        response_json = response.json()
        for event in range(len(response_json)):
            print('title: ' + response_json[event]['name'])

            print('host: ' + response_json[event]['group']['name'])

            start_at, end_at = get_start_and_end_time(response_json[event])
            print('start at: ' + str(start_at))
            print('end_at: ' + str(end_at))

            print('link: ' + response_json[event]['link'])
            print('source: ' + 'meetup')

            venue = get_venue(response_json[event].get('venue'))
            print('location: ' + venue)

            print('meetup_event_id: ' + response_json[event]['id'])

            photo_url = get_photo_url(response_json[event].get('group'), response_json[event].get('featured_photo'))
            print('photo: ' + photo_url)

            event_dict['title'] = response_json[event]['name']
            event_dict['host'] = response_json[event]['group']['name']
            event_dict['start_at'] = start_at
            event_dict['end_at'] = end_at
            event_dict['external_link'] = response_json[event]['link']
            event_dict['source'] = 'meetup_crawling'
            event_dict['location'] = venue

            category_ = Category.objects.get(name='conference')

            photo = requests.get(photo_url)
            meetup_event = MeetupCrawling.objects.create(**event_dict, category=category_)
            image_extension = MIMETYPE[photo.headers['Content-Type']]
            meetup_event.photo.save('image' + image_extension, ContentFile(photo.content), save=True)


def get_start_and_end_time(response_json):
    start_at = datetime.fromisoformat(
        response_json['local_date'] + ' ' + response_json['local_time'])
    end_at = start_at + \
        timedelta(milliseconds=response_json['duration'])
    return start_at, end_at


def get_venue(venue_json):
    location = ""
    if venue_json is None:
        return location
    else:
        if venue_json.get('city') is not None:
            location += venue_json.get('city')
        if venue_json.get('address_1') is not None:
            location += ' ' + venue_json.get('address_1')
        if venue_json.get('address_2') is not None:
            location += ' ' + venue_json.get('address_2')
        if venue_json.get('address_3') is not None:
            location += ' ' + venue_json.get('address_3')
        if venue_json.get('name') is not None:
            location += ' ' + venue_json.get('name')
        return location

def get_photo_url(group_photo, featured_photo):
    if featured_photo is None:
        return group_photo.get('key_photo').get('photo_link')
    return featured_photo.get('photo_link')

if __name__ == '__main__':
    save_new_events_from_meetup_dev_group(korea_meetup_dev_group)
