import urllib.request

from pandas._libs import json

from Recommand_Contents import matchingUser


def getCount(user):
    url = "https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername="+user+"&key=AIzaSyA8bOeq4rtIj5qI6qkf2FRrMUpw0IoGoSk"
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        return response_body.decode('utf-8')

def getCount_id(id):
    url = "https://www.googleapis.com/youtube/v3/channels?part=statistics&id="+id+"&key=AIzaSyA8bOeq4rtIj5qI6qkf2FRrMUpw0IoGoSk"
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        return response_body.decode('utf-8')

if __name__ == "__main__":
    m = matchingUser("보겸TV")
    channel = m[1]
    if channel == 'user':
        Channel = getCount(m[2])
    else:
        Channel = getCount_id(m[2])
    data = json.loads(Channel)
    print(data['items'][0]['statistics']['subscriberCount'])