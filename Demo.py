import datetime
import CompareChannel as C
import Recommand_Contents as R
import GetHowOftenUploadVideo as G
import Function1 as F1
import Funtion2 as F
import Function3 as F3

now = datetime.datetime.now()
import json

# function 1
def YourGrade(name):
    count = 2;
    # 월별 동영상 업로드 수를 저장한 배열
    time = []
    # 2월부터 11월까지의 비디오 업로드 수
    while count <= now.month:
        V = G.GetHowOftenUploadVideo(name, count)
        v = json.loads(V)
        time.append(v["pageInfo"]["totalResults"])
        count = count + 1;
    avg = sum(time, 0.0) / len(time)
    min = avg * 0.8
    max = avg * 1.2
    month = time.pop()
    if month < min:
        return "c"
    elif min < month < max:
        return "b"
    else:
        return "a"


# function 2
def function2_1(name):
    m = F.getVideoId(name)
    m = json.loads(m)
    videoID = []
    count = 0
    while count < 20:
        try:
            videoID.append(m['items'][count]['id']['videoId'])
            count = count + 1
        except:
            count = count + 1
    list = F.checkViewCount(videoID)
    view = list[0]
    avg = sum(view, 0.0) / len(view)
    min = avg * 0.8
    max = avg * 1.2
    month = view.pop() + view.pop() + view.pop() / 3
    if month < min:
        return "c"
    elif min < month < max:
        return "b"
    else:
        return "a"


# function 2
def function2_2(name):
    m = F.getVideoId(name)
    m = json.loads(m)
    videoID = []
    count = 0
    while count < 20:
        try:
            videoID.append(m['items'][count]['id']['videoId'])
            count = count + 1
        except:
            count = count + 1
    list = F.checkViewCount(videoID)
    like = list[1]
    avg = sum(like, 0.0) / len(like)
    min = avg * 0.8
    max = avg * 1.2
    month = like.pop() + like.pop() + like.pop() / 3
    if month < min:
        return "c"
    elif min < month < max:
        return "b"
    else:
        return "a"


# function 3
def function3(name):
    m = F3.getVideoId(name)
    m = json.loads(m)
    videoID = []
    count = 0
    while count < 20:
        try:
            videoID.append(m['items'][count]['id']['videoId'])
            count = count + 1
        except:
            count = count + 1
    list = F3.checkViewCount(videoID)
    _max = max(list)
    maxVideoIndex = list.index(_max)
    v1 = videoID.pop(maxVideoIndex)
    _min = min(list)
    minVideoIndex = list.index(_min)
    v2 = videoID.pop(minVideoIndex)
    goodVideo = F3.videoData(v1)
    badVideo = F3.videoData(v2)
    gv = json.loads(goodVideo)
    bv = json.loads(badVideo)

    goodTitle = gv['items'][0]['snippet']['title']
    # 썸네일
    goodURL = gv['items'][0]['snippet']['thumbnails']['default']['url']

    badTitle = bv['items'][0]['snippet']['title']
    # 썸네일
    badURL = bv['items'][0]['snippet']['thumbnails']['default']['url']

    s = str(goodTitle) + str(goodURL) + str(badTitle) + str(badURL)

    return s


# function 4
def GetTrends(name):
    # 입력받은 유튜버의 ID && Channel ID를 받아옵니다.
    m = R.matchingUser(name)
    # ID & Channel ID를 통해서 채널정보를 얻어옵니다.
    # 채널이 가지고 있는 카테고리를 반환받습니다. ratings_expand(채널의 카테고리)
    ratings_expand = R.relContents(m[1], m[2])
    # 채널카테고리를 기반으로 구글 검색어 추이를 분석합니다.
    result = R.GoogleTrend.GoogleTrendConstruct(ratings_expand)
    return str(result)


def Getcontents_my_channel(name):
    # 입력받은 유튜버의 ID && Channel ID를 받아옵니다.
    m = R.matchingUser(name)
    # ID & Channel ID를 통해서 채널정보를 얻어옵니다.
    # 채널이 가지고 있는 카테고리를 반환받습니다. ratings_expand(채널의 카테고리)
    ratings_expand = R.relContents(m[1], m[2])
    return str(ratings_expand)


def searchGragh(name):
    # 입력받은 유튜버의 ID && Channel ID를 받아옵니다.
    m = R.matchingUser(name)
    # ID & Channel ID를 통해서 채널정보를 얻어옵니다.
    # 채널이 가지고 있는 카테고리를 반환받습니다. ratings_expand(채널의 카테고리)
    ratings_expand = R.relContents(m[1], m[2])
    # 채널 카테고리를 기반으로 네이버 검색 추이를 분석합니다.
    print(R.search(ratings_expand[0]))
    return str(R.search(ratings_expand[0]))


def Compare_with_youtuber(name):
    m = R.matchingUser(name)
    # 입력채널의 카테고리
    ratings_expand = R.relContents(m[1], m[2])
    # 비교채널 관련 컨텐츠
    c = C.relChannel(m[1], m[2])
    # 관련채널 카테고리 비교
    recommandC = c[1]
    print(c[0])
    for a in recommandC:
        if a in ratings_expand:
            recommandC.remove(a)
    # 반환결과 정리
    return str(recommandC)


def Recommand_Contents(name):
    m = R.matchingUser(name)
    # 입력채널의 카테고리
    ratings_expand = R.relContents(m[1], m[2])
    # 비교채널 관련 컨텐츠
    c = C.relChannel(m[1], m[2])
    # 관련채널 카테고리에서 나의 카테고리를 제외한 결과
    return str(c[0])


def count(name):
    m = R.matchingUser(name)
    channel = m[1]
    if channel == 'user':
        Channel = F1.getCount(m[2])
    else:
        Channel = F1.getCount_id(m[2])
    data = json.loads(Channel)
    data = data['items'][0]['statistics']['subscriberCount']
    return str(data)


if __name__ == '__main__':
    name = "보겸TV"

    print("구독자 수 : " + count(name))
    print(" 최근 영상 업로드 등급 : " + YourGrade(name))
    print(" 최근 영상 조회수 등급 : " + function2_1(name))
    print(" 최근 영상 좋아요 수 등급 : " + function2_2(name))
    print(" 인기 영상 + 비인기 영상" + function3(name))
    print(" 추천 컨텐츠 " + GetTrends(name))

    # 안쓰는 기능
