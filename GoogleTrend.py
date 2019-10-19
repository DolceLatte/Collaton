from pytrends.request import TrendReq

# Login to Google. Only need to run this once, the rest of requests will use the same session.
pytrend = TrendReq()

# Get Google Hot Trends data
trending_searches_df = pytrend.trending_searches(pn='south_korea')
print(trending_searches_df.head())

# 기본 검색어 설정
# Create payload and capture API tokens. Only needed for interest_over_time(), interest_by_region() & related_queries()
pytrend.build_payload(kw_list=['구혜선'], timeframe='today 5-y', geo='KR')
#
# # Interest Over Time
# interest_over_time_df = pytrend.interest_over_time()
# print(interest_over_time_df.head())
#
# # Interest by Region
# interest_by_region_df = pytrend.interest_by_region()
# print(interest_by_region_df.head())

# Related Queries, returns a dictionary of dataframes
related_queries_dict = pytrend.related_queries()
print(related_queries_dict)



# # Get Google Hot Trends data
# today_searches_df = pytrend.today_searches()
# print(today_searches_df.head())

# # Get Google Keyword Suggestions
# suggestions_dict = pytrend.suggestions(keyword='Block chain')
# print(suggestions_dict)
