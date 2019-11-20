import datetime
import urllib.request
import json
import Recommand_Contents as R
import GetHowOftenUploadVideo as G


def getVideoId(name):
    m = R.matchingUser(name)
    channel = m[1]
    if channel == 'user':
        channelId = G.getUserChannelID(m[2])
        channelId = json.loads(channelId)
        channelId = channelId["items"][0]["id"]
    else:
        channelId = m[2]
    url = "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=" + channelId + "&maxResults=20&key=AIzaSyA8bOeq4rtIj5qI6qkf2FRrMUpw0IoGoSk"
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        return response_body.decode('utf-8')

def videoData(id):
    url = "https://www.googleapis.com/youtube/v3/videos?part=snippet&id=" + id + "&key=AIzaSyA8bOeq4rtIj5qI6qkf2FRrMUpw0IoGoSk"
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        return response_body.decode('utf-8')

def checkViewCount(list=[]):
    viewCount = []
    for l in list:
        url = "https://www.googleapis.com/youtube/v3/videos?part=statistics&id=" + l + "&maxResults=20&key=AIzaSyA8bOeq4rtIj5qI6qkf2FRrMUpw0IoGoSk"
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        if (rescode == 200):
            response_body = response.read()
            r = response_body.decode('utf-8')
            r = json.loads(r)
            view = r["items"][0]["statistics"]["viewCount"]
            viewCount.append(int(view))
    return viewCount


if __name__ == "__main__":
    m = getVideoId("보겸TV")
    m = json.loads(m)
    videoID = []
    count = 0
    while count < 20:
        try:
            videoID.append(m['items'][count]['id']['videoId'])
            count = count + 1
        except:
            count = count + 1

    list = checkViewCount(videoID)
    max = max(list)
    maxVideoIndex = list.index(max)
    v1 = videoID.pop(maxVideoIndex)
    min = min(list)
    minVideoIndex = list.index(min)
    v2 = videoID.pop(minVideoIndex)
    goodVideo = videoData(v1)
    badVideo = videoData(v2)
    gv = json.loads(goodVideo)
    bv = json.loads(badVideo)
    print(gv)
    #제목
    print(gv['items'][0]['snippet']['title'])
    #썸네일
    print(gv['items'][0]['snippet']['thumbnails']['default']['url'])
