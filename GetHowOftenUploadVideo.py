import urllib.request
import json

import Recommand_Contents as R


def GetHowOftenUploadVideo(name):
    m = R.matchingUser(name)
    channel = m[1]
    if channel == 'user':
        channelId = getUserChannelID(m[2])
    else:
        channelId = m[2]
    channelId = json.loads(channelId)
    url = "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId="+str(channelId["items"][0]["id"])+"&key=AIzaSyA8bOeq4rtIj5qI6qkf2FRrMUpw0IoGoSk"
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        return response_body.decode('utf-8')

def getUserChannelID(user):
    url = "https://www.googleapis.com/youtube/v3/channels?part=id&forUsername="+user+"&key=AIzaSyA8bOeq4rtIj5qI6qkf2FRrMUpw0IoGoSk"
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        return response_body.decode('utf-8')

if __name__ == "__main__":
    V = GetHowOftenUploadVideo("보겸TV")
    v = json.loads(V)
    uploadtime = []
    time = ""
    count = 0
    while count < 5:
        time = v["items"][count]["snippet"]["publishedAt"]
        print(time)
        count = count+1