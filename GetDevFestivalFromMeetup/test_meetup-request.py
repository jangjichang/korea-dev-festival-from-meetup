import requests

korea_meetup_dev_group = [
    'Software-QA',
]

def meetup_group_event_title(url):
    res = requests.get(url)
    res_json = res.json()
    data = dict()
    for event in range(len(res_json)):
        data[event] = res_json[event]['name']
    return data


def test_meetup_group_event():
    data = {0: '[9th GroundBreakers Meetup] 아홉번째 스토리 : 차근차근 알아보는 Infrastructure as Code'}
    assert meetup_group_event_title(
        'https://api.meetup.com/OracleDeveloperKR/events?&sign=true&photo-host=public&page=20') == data
    data = {0: 'Software QA(Quality Assurance) 소모임 - 2번째 모임 (1월 23일)'}
    assert meetup_group_event_title(
        'https://api.meetup.com/Software-QA/events?&sign=true&photo-host=public&page=20') == data
