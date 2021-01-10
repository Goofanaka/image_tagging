# 1. 프로젝트명 
* 개요 : 소셜이커머스 1위인 쿠팡의 과일 이미지를 크롤링하여 이미지 기반 분석 프로그램을 제작함
* 팀명 : Goofenaka 팀원 : 손기훈 김동건 유주아 김은찬
* 개발 기간 : 2020년 12월 22일 ~ 2021년 1월 10일
___

# 2. 프로젝트 정보
##	1.Technologies(해더2)
- 개발언어 : python
- 크롤링 : Beautifulsoup 
- 데이터베이스 : MongoDB,Mongoengine
- 분석 및 시각화 : Pandas, jupyter notebook, matplotlib 
- Gui tool : PyQT
- Git, Github

___

# 3. Features
- crawling.py : 이미지와 제목을 크롤링하고 크롤링한 이미지를 폴더에 저장
- dict_json.py : dict에서 json으로 변경 list에서 dict로 변경
- fruit_dict.py : 과일사전 
- pyqt_gui.py : GUI 환경을 구현
- img_to_mongo.py : DB에 이미지 파일을 저장
- tagdata.py : DB에 태깅된 데이터를 저장
- kakao.py : 크롤링한 이미지를 카카오 API에 넣고 태깅한 값을 받아 list로 변환 
- google_api.py : 크롤링한 이미지를 구글 API에 넣고 태깅한 값을 받아 list로 변환 
- main : 전체적인 모듈을 실행하는 파일

___

#4. 사용방법(해더2)

##1.python 필요 라이브러리 설치
- Open CV
- Beautiful Soup
- pandas
- google-cloud-vision
- matplotlib(seaborn)
- PyQT5
- mongoengine(pymongo,dnspython)

##2.개인 환경 구성
- python 가상환경 구현
- 카카오 비전 API 키
- 구글 비전 Credentials 파일(json)
- user-agent 입력
	
  ![workflow](https://user-images.githubusercontent.com/71329051/104127509-d1d46900-53a5-11eb-8c03-bdddded18698.PNG)
