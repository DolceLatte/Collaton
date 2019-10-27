import Recommand_Contents
import Search_Relative_Channel
import json

def relChannel(channel,user):
    rContents = Recommand_Contents.relContents_with_ortherChannel(channel,user)
    if channel == 'user':
        Channel = Search_Relative_Channel.getCategory(user)
    else:
        Channel = Search_Relative_Channel.getCategory_id(user)
    relativeChannel = json.loads(Channel)
    r = relativeChannel["items"][0]['brandingSettings']["channel"]["featuredChannelsUrls"][0]
    s = Search_Relative_Channel.getCategory_id(r)
    result = json.loads(s)
    return result["items"][0]['brandingSettings'],rContents



if __name__ == "__main__":
    m = Recommand_Contents.matchingUser('보겸')
    ratings_expand =  Recommand_Contents.relContents(m[1], m[2])
    # 사용자의 컨텐츠
    # print(ratings_expand)
    # 비교채널 관련 컨텐츠
    c = relChannel(m[1],m[2])
    # print(c[1])
    recommandC = c[1]
    print(c[0])
    for a in recommandC:
        if a in ratings_expand:
            recommandC.remove(a)

    print(recommandC)