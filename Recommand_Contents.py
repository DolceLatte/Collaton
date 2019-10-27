import json

import urllib.request
from urllib import parse

import GoogleTrend
import Search_Relative_Channel
import requests
from bs4 import BeautifulSoup


# contents의 구글 트렌트 데이터를 수집
def Recommand_Content(content):
    return GoogleTrend.GoogleTrendConstruct(content)


def relContents(channel,user):

    if channel == 'user':
        Channel = Search_Relative_Channel.getCategory(user)
    else:
        Channel = Search_Relative_Channel.getCategory_id(user)
    relativeChannel = json.loads(Channel)
    # 연관 contents 데이터를 수집
    content = relativeChannel["items"][0]["topicDetails"]["topicCategories"]

    # 관련컨텐츠 배열
    _content = []
    i = 0
    # 카테고리 분류 작업
    for a in content:
        if str(a).split('/')[4] == 'Hobby':
            _content.append('취미')
            i = i + 1
        elif str(a).split('/')[4] == 'Lifestyle_(sociology)':
            _content.append('예능')
            i = i + 1
        elif str(a).split('/')[4] == 'Entertainment':
            _content.append('오락')
            i = i + 1
        elif str(a).split('/')[4] == 'Video_game_culture':
            _content.append('게임')
            i = i + 1
        elif str(a).split('/')[4] == 'Pet':
            _content.append('동물')
            i = i + 1
        elif str(a).split('/')[4] == 'Film':
            pass
        elif str(a).split('/')[4] == 'Food':
            _content.append('음식')
            i = i + 1
        else:
            _content.append(str(a).split('/')[4])
            i = i + 1
        if i > 1:
            break

    # contents의 구글 트렌트 데이터를 수집
    # 예외처리 과정
    return _content

def relContents_with_ortherChannel(channel,user):

    if channel == 'user':
        Channel = Search_Relative_Channel.getCategory(user)
    else:
        Channel = Search_Relative_Channel.getCategory_id(user)
    relativeChannel = json.loads(Channel)
    # 연관 contents 데이터를 수집
    content = relativeChannel["items"][0]["topicDetails"]["topicCategories"]

    # 관련컨텐츠 배열
    _content = []
    i = 0
    # 카테고리 분류 작업
    for a in content:
        if str(a).split('/')[4] == 'Hobby':
            _content.append('취미')
            i = i + 1
        elif str(a).split('/')[4] == 'Lifestyle_(sociology)':
            _content.append('예능')
            i = i + 1
        elif str(a).split('/')[4] == 'Entertainment':
            _content.append('오락')
            i = i + 1
        elif str(a).split('/')[4] == 'Video_game_culture':
            _content.append('게임')
            i = i + 1
        elif str(a).split('/')[4] == 'Pet':
            _content.append('동물')
            i = i + 1
        elif str(a).split('/')[4] == 'Film':
            pass
        elif str(a).split('/')[4] == 'Food':
            _content.append('음식')
            i = i + 1
        else:
            _content.append(str(a).split('/')[4])
            i = i + 1
        if i > 4:
            break

    # contents의 구글 트렌트 데이터를 수집
    # 예외처리 과정
    return _content

def search(title):
    client_id = "TLJL6dICXVWTh4Q67_8N"
    client_secret = "BwPjecjHEp"
    url = "https://openapi.naver.com/v1/datalab/search";
    body = "{\"startDate\":\"2019-01-01\",\"endDate\":\"2019-10-30\",\"timeUnit\":\"month\",\"keywordGroups\":[{\"groupName\":\"유튜브\",\"keywords\":[\"" + title + "\"]}],\"device\":\"pc\",\"gender\":\"f\"}";

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    request.add_header("Content-Type", "application/json")
    response = urllib.request.urlopen(request, data=body.encode("utf-8"))
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        print(response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)


def matchingUser(title):
    ## HTTP GET Request
    url = urllib.parse.quote(title)
    req = requests.get('https://www.youtube.com/results?search_query=' + url)
    ## HTML 소스 가져오기
    html = req.text
    ## BeautifulSoup으로 html소스를 python객체로 변환하기
    ## 첫 인자는 html소스코드, 두 번째 인자는 어떤 parser를 이용할지 명시.
    ## 이 글에서는 Python 내장 html.parser를 이용했다.
    soup = BeautifulSoup(html, 'html.parser')
    id = soup.find('a', attrs={'class': 'yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link'})

    find = str(id.get('href')).split("/")

    return find




if __name__ == "__main__":
    m = matchingUser('장삐쭈')
    ratings_expand = relContents(m[1],m[2])
    # 인기 컨텐츠
    print(ratings_expand)
    result = GoogleTrend.GoogleTrendConstruct(ratings_expand)
    # 검색어 순위
    print(result)
    # 검색어추이
    print(search(ratings_expand[0]))
    GoogleTop = dict

    # print()
