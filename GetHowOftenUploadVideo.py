import datetime
import urllib.request
import json

import Recommand_Contents as R

now = datetime.datetime.now()

def GetHowOftenUploadVideo(name, d):
    m = R.matchingUser(name)
    channel = m[1]
    if channel == 'user':
        channelId = getUserChannelID(m[2])
    else:
        channelId = m[2]
    channelId = json.loads(channelId)
    channelId = str(channelId["items"][0]["id"])
    url = "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=" + channelId+"&publishedAfter=2019-"+str(d-1)+"-01T15:00:00Z&publishedBefore=2019-" + \
          str(d) + "-01T15:00:00Z&key=AIzaSyCDuwnu7KS18S6FJ1EHSvTDtmEF405QJfc"
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        return response_body.decode('utf-8')


def getUserChannelID(user):
    url = "https://www.googleapis.com/youtube/v3/channels?part=id&forUsername=" + user + "&key=AIzaSyCDuwnu7KS18S6FJ1EHSvTDtmEF405QJfc"
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        return response_body.decode('utf-8')


if __name__ == "__main__":
    count = 2;
    while count <= 11:
        V = GetHowOftenUploadVideo("보겸TV", count)
        v = json.loads(V)
        print(v["pageInfo"]["totalResults"])
        count = count+1;
