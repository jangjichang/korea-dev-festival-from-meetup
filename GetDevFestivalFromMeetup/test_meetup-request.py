"""
meetup에서 1000명 이상의 tech 그룹과
2020년 1월 2일 기준 최근에 활동했던 그룹 목록을 저장한다.

예정된 이벤트가 없는 경우, 1개인 경우, 2개 이상인 경우

요청하고 -> 해당 id의 이벤트가 있는지 확인하고 -> 없으면 등록

필요한 정보:
# title
# host
thumb_nail(특정 이벤트의 사진이 없으면 그룹의 사진을 보내주는 걸로함)
# category
# start_at
# end_at
# link
# location
# source
# meetup_event_id
"""
import requests
from datetime import datetime, timedelta

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


def check_for_new_events_from_meetup_dev_group(korea_meetup_dev_group):
    """
    featured_photo -> 이벤트 사진
    group_key_photo -> 그룹 사진
    """
    results = dict()
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

            photo = get_photo(response_json[event].get('group'), response_json[event].get('featured_photo'))
            print('photo: ' + photo)


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

def get_photo(group_photo, featured_photo):
    if featured_photo is None:
        return group_photo.get('key_photo').get('photo_link')
    return featured_photo.get('photo_link')

if __name__ == '__main__':
    check_for_new_events_from_meetup_dev_group(korea_meetup_dev_group)
