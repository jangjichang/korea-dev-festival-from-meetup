"""
meetup api를 이용해서 20개의 그룹에 새롭게 올라온 이벤트를 저장하는 것이다. 이벤트가 저장되는 순서는 다음과 같다.

1. 람다를 이용해 특정 시간에 프로그램을 실행하여 새롭게 올라온 이벤트 목록을 MeetupCrawling에 저장한다.
2. MeetupCrawling에 저장된 데이터 중 WaitingEvent, DevEvent에 존재하지 않는 데이터를 WaitingEvent에 복사한다.
3. 운영진이 WaitingEvent에 있는 데이터를 DevEvent 혹은 NotDevEvent로 복사한다.




내가 해야할 게 뭔가?

한국 개발 그룹(예를들어 A, B, C)에서 새로운 이벤트 정보를 가져온다.

이벤트 정보는 title, host, photo, thumnail photo, category(conference, education, circle), start_at, end_at, created_at, updated_at, external_link, location, source(default=meetup)

TODO: 1. 크롤링할 한국 개발 그룹들을 조사하자. 회원수가 많은 것들 혹은 최근 활동이 있는 것들에서 추린다.
2. 개발 그룹의 이벤트 목록을 요청한다.
3. 데이터베이스(DevEvent)에 있는지 확인하고 


"""


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
