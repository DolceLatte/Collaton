from flask import Flask
import CompareChannel as C
import Recommand_Contents as R
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route('/Getcontents_my_channel/<name>')
@cross_origin()
def Getcontents_my_channel(name):
   #입력받은 유튜버의 ID && Channel ID를 받아옵니다.
   m = R.matchingUser(name)

   #ID & Channel ID를 통해서 채널정보를 얻어옵니다.
   #채널이 가지고 있는 카테고리를 반환받습니다. ratings_expand(채널의 카테고리)
   ratings_expand = R.relContents(m[1], m[2])
   return ratings_expand

@app.route('/GetTrends/<name>')
@cross_origin()
def GetTrends(name):
   #입력받은 유튜버의 ID && Channel ID를 받아옵니다.
   m = R.matchingUser(name)

   #ID & Channel ID를 통해서 채널정보를 얻어옵니다.
   #채널이 가지고 있는 카테고리를 반환받습니다. ratings_expand(채널의 카테고리)
   ratings_expand = R.relContents(m[1], m[2])

   #채널카테고리를 기반으로 구글 검색어 추이를 분석합니다.
   result = R.GoogleTrend.GoogleTrendConstruct(ratings_expand)
   return result

@app.route('/searchGragh/<name>')
@cross_origin()
def searchGragh(name):
   #입력받은 유튜버의 ID && Channel ID를 받아옵니다.
   m = R.matchingUser(name)

   #ID & Channel ID를 통해서 채널정보를 얻어옵니다.
   #채널이 가지고 있는 카테고리를 반환받습니다. ratings_expand(채널의 카테고리)
   ratings_expand = R.relContents(m[1], m[2])

   #채널 카테고리를 기반으로 네이버 검색 추이를 분석합니다.
   print(R.search(ratings_expand[0]))

   return R.search(ratings_expand[0])

@app.route('/Compare_with_youtuber/<name>')
@cross_origin()
def Compare_with_youtuber(name):
   m = R.matchingUser(name)
   # 입력채널의 카테고리
   ratings_expand = R.relContents(m[1], m[2])

   # 비교채널 관련 컨텐츠
   c = C.relChannel(m[1], m[2])

   #관련채널 카테고리 비교
   recommandC = c[1]
   print(c[0])
   for a in recommandC:
      if a in ratings_expand:
         recommandC.remove(a)
   # 반환결과 정리
   return str(recommandC)


@app.route('/Recommand_Contents/<name>')
@cross_origin()
def Recommand_Contents(name):
   m = R.matchingUser(name)
   # 입력채널의 카테고리
   ratings_expand = R.relContents(m[1], m[2])

   # 비교채널 관련 컨텐츠
   c = C.relChannel(m[1], m[2])

   #관련채널 카테고리에서 나의 카테고리를 제외한 결과
   return str(c[0])



if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080")