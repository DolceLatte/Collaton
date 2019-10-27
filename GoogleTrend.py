from pytrends.request import TrendReq

def GoogleTrendConstruct(Keyword):
    # Login to Google. Only need to run this once, the rest of requests will use the same session.
    pytrend = TrendReq()
    # 기본 검색어 설정
    # suggestions_dict = pytrend.suggestions(keyword=Keyword)
    # keyword1 = suggestions_dict[1]['title'].split(' ')
    # keyword2 = suggestions_dict[2]['title'].split(' ')
    pytrend.build_payload(kw_list=Keyword, timeframe='today 5-y', geo='KR',gprop='youtube')

    # Related Queries, returns a dictionary of dataframes
    # 떠오르는 검색어 , 인기 연관 검색어를 반환
    related_queries_dict = pytrend.related_queries()
    return related_queries_dict


if __name__ == "__main__":
    print(GoogleTrendConstruct('Lifestyle'))

