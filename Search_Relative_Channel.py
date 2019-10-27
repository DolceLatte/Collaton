import urllib.request
import json

def getCategory(user):
    url = "https://www.googleapis.com/youtube/v3/channels?part=contentDetails,brandingSettings,topicDetails&forUsername="+user+"&key=AIzaSyA8bOeq4rtIj5qI6qkf2FRrMUpw0IoGoSk"
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        return response_body.decode('utf-8')

def getCategory_id(id):
    url = "https://www.googleapis.com/youtube/v3/channels?part=contentDetails,brandingSettings,topicDetails&id="+id+"&key=AIzaSyA8bOeq4rtIj5qI6qkf2FRrMUpw0IoGoSk"
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        return response_body.decode('utf-8')

def getbrandingSettings(r):
        url = "https://www.googleapis.com/youtube/v3/channels?part=brandingSettings&id="+r+"&key=AIzaSyA8bOeq4rtIj5qI6qkf2FRrMUpw0IoGoSk"
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        if (rescode == 200):
                response_body = response.read()
                return response_body.decode('utf-8')

if __name__ == "__main__":
    Channel = getCategory()
    relativeChannel = json.loads(Channel)
    c1 = relativeChannel["items"][0]["topicDetails"]["topicCategories"][0]
    c2 = relativeChannel["items"][0]["topicDetails"]["topicCategories"][1]
    c3 = relativeChannel["items"][0]["topicDetails"]["topicCategories"][2]
    c4 = relativeChannel["items"][0]["topicDetails"]["topicCategories"][3]
    print(str(c1).split('/')[-1])
    print(str(c2).split('/')[-1])
    print(str(c3).split('/')[-1])
    print(str(c4).split('/')[-1])
    r = relativeChannel["items"][0]['brandingSettings']["channel"]["featuredChannelsUrls"][0]
    rChannel = getbrandingSettings(r)
    rChannel = json.loads(rChannel)
    # print(rChannel["items"][0]['brandingSettings']["channel"])
    # print(rChannel["items"][0]['brandingSettings']["channel"]["title"])

