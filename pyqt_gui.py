from PyQt5.QtCore import QVariant, Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import glob
import os
import errno
from urllib.request import urlretrieve
import re
from bs4 import BeautifulSoup
from datetime import datetime
from os import listdir
from os.path import isfile, join
import requests
import cv2
from google.cloud import vision
import io
import six
import crawling
import time
import tagdata
import img_to_mongo
import dict_json
from visualization import fruit_statistics
import my_setting
import shutil


class textItem(QWidget):
    crawling.make_dir('images') 
    header = {"User-Agent": my_setting.USER_AGENT } #크롤링 헤더
    crawl_list =  crawling.crawling(1,'images',header)


    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.layout = QBoxLayout(QBoxLayout.TopToBottom)
        self.lbl1 = QLabel(self)
        self.lbl2 = QLabel(self)

    def set_text(self, i):
        self.lbl1.setText(self.crawl_list[i][0])
        self.lbl2.setText(self.crawl_list[i][1])
        self.layout.addWidget(self.lbl1)
        self.layout.addWidget(self.lbl2)
        # self.layout.setSizeConstraint(QBoxLayout.SetFixedSize)

        fontVar = QFont("나눔스퀘어",20)
        self.lbl1.setFont(fontVar)
        self.lbl2.setFont(fontVar)

        self.setLayout(self.layout)
      
class Item(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.layout = QBoxLayout(QBoxLayout.LeftToRight)
        self.lbl = QLabel(self)    

    def set_img(self, path,i=0) :
        pixmap = QPixmap(path)     #pixmap = QPixmap("C:\\Project2020\\venv\\images\\2021_01_05_7.jpg")
        self.lbl.setPixmap(QPixmap(pixmap))

        self.layout.addWidget(self.lbl)
        self.layout.setSizeConstraint(QBoxLayout.SetFixedSize)   #레이아웃에 고정
        self.setLayout(self.layout)

        custom_widget = textItem()
        custom_widget.set_text(i)
        self.layout.addWidget(custom_widget)

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.kakao_list = []
        self.google_list = []
        self.fruit_list = []
        self.crawl_list =[]
        self.initUI()

    def initUI(self):
        self.btn2 = QPushButton('크롤링', self)
        self.btn3 = QPushButton('API 및 과일사전\n태그생성', self)
        self.btn4 = QPushButton('데이터 DB 전송', self)
        self.btn5 = QPushButton('일일 빈도 분석', self)

        self.btn3.setDisabled(True)
        self.btn4.setDisabled(True)
        self.btn5.setDisabled(True)

        self.stylebtn()

        hbox = QHBoxLayout()
        hbox.addWidget(self.btn2)
        hbox.addWidget(self.btn3)
        hbox.addWidget(self.btn4)
        hbox.addWidget(self.btn5)
        hbox.setContentsMargins(5, 30, 5, 10)   #(left, top, right, bottom)

        self.vbox = QVBoxLayout()
        self.vbox.addLayout(hbox)

        self.btn2.clicked.connect(self.crawling)
        self.btn2.clicked.connect(self.add_list)

        self.btn3.clicked.connect(self.kakao_tag)
        self.btn3.clicked.connect(self.localize_objects)
        self.btn3.clicked.connect(self.fruit_check)
        self.btn3.clicked.connect(self.tag_res)

        self.btn4.clicked.connect(self.tag_data_to_mongo)
        self.btn4.clicked.connect(self.db_res)

        self.btn5.clicked.connect(self.freq_today)
        self.btn5.clicked.connect(self.res_a)

        self.pic = QLabel(self)
        pixmap = QPixmap('main_img.png')     #pixmap = QPixmap("C:\\Project2020\\venv\\images\\2021_01_05_7.jpg")
        pixmap = pixmap.scaledToWidth(1000)
        self.pic.setPixmap(QPixmap(pixmap))
        self.pic.setAlignment(Qt.AlignCenter)   #정렬 수직,수평 중앙
        
        self.vbox.addWidget(self.pic)
        self.setLayout(self.vbox)
        self.setGeometry(300, 300, 1200, 1000)
        self.show()
    
    def stylebtn(self):
        self.btn2.setStyleSheet("height: 30px")
        self.btn3.setStyleSheet("height: 30px")
        self.btn4.setStyleSheet("height: 30px")
        self.btn5.setStyleSheet("height: 30px")
        
    def crawling(self):
        headers = {"User-Agent": my_setting.USER_AGENT}
        str_date = datetime.now().strftime('%Y_%m_%d')
        cnt = 1

        for page in range(1, 2):
            # 페이지 설정
            url = 'https://www.coupang.com/np/categories/194282?listSize=120&page={}'.format(page)
            res = requests.get(url, headers=headers)
            soup = BeautifulSoup(res.text, 'html.parser')

            # 이미지 태그 리스트 불러오기
            data1_list = soup.find_all('dt', attrs={'class': 'image'})

            for li in data1_list:
                img = li.find("img")  # img 태그 찾기
                title = img["alt"]  # 제목 alt 넣은거
                img_src = 'http:' + img["src"]  # img 다운 url완성
                title = re.sub("[^0-9a-zA-Zㄱ-힗]", "", title)  # title 특수문자,공백 제거
                savename = str_date + '_' + str(cnt) + '.jpg'
                urlretrieve(img_src, './images/' + savename)  # 이미지 크롤링(제목 : 날짜)
                self.crawl_list.append([savename, title, str_date])  # list 저장
                cnt += 1
            
        self.pic.setParent(None)

    def add_list(self):
        self.listw = QListWidget(self)

        images = sorted(glob.glob('C:\\Project2020\\venv\\\images\\*.jpg'), key=os.path.getctime)

        for i in range(len(images)):
            item = QListWidgetItem(self.listw)
            custom_widget = Item()
            custom_widget.set_img(images[i],i)

            item.setSizeHint(custom_widget.sizeHint())
            self.listw.addItem(item)
            self.listw.setItemWidget(item, custom_widget)
            self.vbox.addWidget(self.listw)
            self.setLayout(self.vbox)

        self.btn3.setEnabled(True)

    def tag_res(self):
        self.freslbl = QLabel(self)
        self.freslbl.setText("태그 생성 완료")

        self.freslbl.setAlignment(Qt.AlignCenter)   #정렬 수직,수평 중앙
        fontVar = QFont("나눔스퀘어",20)
        self.freslbl.setFont(fontVar)
        self.freslbl.setStyleSheet("Color : black")  # 글자색 변환

        self.listw.setParent(None)
        self.vbox.addWidget(self.freslbl)
        self.setLayout(self.vbox)
        self.btn3.setDisabled(True)
        self.btn4.setEnabled(True)

    def db_res(self):
        self.reslbl_db = QLabel(self)
        self.reslbl_db.setText("DB 전송 완료")

        self.reslbl_db.setAlignment(Qt.AlignCenter)   #정렬 수직,수평 중앙
        fontVar = QFont("나눔스퀘어",20)
        self.reslbl_db.setFont(fontVar)
        self.reslbl_db.setStyleSheet("Color : black")  # 글자색 변환

        self.freslbl.setParent(None)
        self.pic.setParent(None)
        self.vbox.addWidget(self.reslbl_db)
        self.setLayout(self.vbox)
        self.btn4.setDisabled(True)
        self.btn5.setEnabled(True)
        shutil.rmtree('C:\\Project2020\\venv\\images')

    def res_a(self):
        self.lbla = QLabel(self)
        pixmap = QPixmap('fruit_statistics.png')     
        # pixmap = pixmap.scaledToWidth(1000) #크기 지정시 사용
        self.lbla.setPixmap(QPixmap(pixmap))

        self.vbox.setSizeConstraint(QBoxLayout.SetFixedSize)

        self.reslbl_db.setParent(None)
        self.vbox.addWidget(self.lbla)
        self.setLayout(self.vbox)
        self.btn5.setDisabled(True)

    def kakao_tag(self):
        KEY = my_setting.KAKAO_API_KEY
        API_URL = 'https://dapi.kakao.com/v2/vision/multitag/generate'
        headers = {'Authorization': 'KakaoAK {}'.format(KEY)}
        images = sorted(glob.glob('C:\\Project2020\\venv\\images\\*.jpg'), key=os.path.getctime)

        try:
            for img in images:
                image = cv2.imread(img)
                image2 = cv2.imencode('.jpg', image)[1].tobytes()

                data = {'image': image2}  # 이미지 받고
                resp = requests.post(API_URL, headers=headers, files=data)  # 요청보냄
                resp.raise_for_status()
                result = resp.json()['result']  # {'label_kr': ['과일', '감'], 'label': ['fruit', 'persimmon']}
                self.kakao_list.append(result['label'])

        except Exception as e:
            print(str(e))
            sys.exit(0)
        
    def localize_objects(self):
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = my_setting.GOOGLE_API_KEY
        images = sorted(glob.glob('C:\\Project2020\\venv\\images\\*.jpg'), key=os.path.getctime)
        client = vision.ImageAnnotatorClient()
        cnt = 0
        for path in images:
            with open(path, 'rb') as image_file:
                content = image_file.read()

            image = vision.Image(content=content)

            objects = client.object_localization(
                image=image).localized_object_annotations

            cnt += 1
            # print(cnt)

            tags = []
            try:
                for object_ in objects:
                    if object_.score >= 0.50:  # 일치 퍼센트
                        tags.append(object_.name.lower())
            except Exception as e:
                print('error occured' * 10)
                tags.append("error")
                print(cnt)

            self.google_list.append(list(set(tags)))

    def fruit_check(self):

        for text in self.crawl_list:
            tags = []

            if "사과" in text[1]:
                tags.append("apple")

            elif ("단감" in text[1]) or ("곶감" in text[1]) or ("반건시" in text[1]) or ("홍시" in text[1]) or ("감말랭이" in text[1]) or (
                "대봉감" in text[1]):
                tags.append("persimmon")

            elif ("감귤" in text[1]) or ("오렌지" in text[1]) or ("레드향" in text[1]) or ("한라봉" in text[1]) or (
                    "천혜향" in text[1]) or ("황금향" in text[1]) or ("유자" in text[1]) or ("홍미향" in text[1]):
                tags.append("orange")

            elif ("토마토" in text[1]) or ("토망고" in text[1]) or ("쿠마토" in text[1]) or ("샤인마토" in text[1]):
                tags.append("tomato")

            elif "바나나" in text[1]:
                tags.append("banana")

            elif "딸기" in text[1]:
                tags.append("strawberry")

            elif ("샤인머스캣" in text[1]) or ("샤인머스켓" in text[1]) or ("포도" in text[1]):
                tags.append("grape")

            elif "복숭아" in text[1]:
                tags.append("peach")

            elif ("키위" in text[1]) or ("다래" in text[1]):
                tags.append("kiwi")

            elif "수박" in text[1]:
                tags.append("watermelon")

            elif ("패션후르츠" in text[1]) or ("패션프루트" in text[1]) or ("패션프룻" in text[1]) or ("패션플룻" in text[1]):
                tags.append("passion fruit")

            elif ("파인애플" in text[1]) or ("골드파인" in text[1]) or ("파인" in text[1]):
                tags.append("pineapple")

            elif "체리" in text[1]:
                tags.append("cherry")

            elif "석류" in text[1]:
                tags.append("pomegranate")

            elif ("멜론" in text[1]) or ("메론" in text[1]):
                tags.append("melon")

            elif ("레몬" in text[1]) or ("라임" in text[1]):
                tags.append("lemon")

            elif "용과" in text[1]:
                tags.append("dragon fruit")

            elif "람부탄" in text[1]:
                tags.append("rambutan")

            elif "두리안" in text[1]:
                tags.append("durian")

            elif "망고스틴" in text[1]:
                tags.append("mangosteen")

            elif "망고" in text[1]:
                tags.append("mango")

            elif "참외" in text[1]:
                tags.append("orientalmelon")

            elif "무화과" in text[1]:
                tags.append("fig")

            elif "리치" in text[1]:
                tags.append("litchi")

            elif "매실" in text[1]:
                tags.append("japanese apricot")

            elif "아보카도" in text[1]:
                tags.append("avocado")

            elif "파파야" in text[1]:
                tags.append("papaya")

            elif "모과" in text[1]:
                tags.append("quince")

            elif "코코넛" in text[1]:
                tags.append("coconut")

            elif "자두" in text[1]:
                tags.append("plum")

            elif "용안" in text[1]:
                tags.append("dimocarpus longan")

            elif ("자몽" in text[1]) or ("메로골드" in text[1]):
                tags.append("grapefruit")

            elif ("잭후르츠" in text[1]) or ("잭프룻" in text[1]) or ("잭프루트" in text[1]) or ("잭플룻" in text[1]):
                tags.append("jackfruit")

            elif ("베리" in text[1]) or ("아로니아" in text[1]) or ("블랙커런트" in text[1]) or ("오미자" in text[1]) or (
                    "복분자" in text[1]) or ("꾸지뽕" in text[1]):
                tags.append("berry")

            elif "배" in text[1]:
                tags.append("pear")

            else:
                tags.append("fruit_etc")

            self.fruit_list.append(tags)

    def tag_data_to_mongo(self):

        key_list = ['filename','title','date','kakao_tag','google_tag','fruit_dict']

        for i in range(0,len(self.crawl_list)) :
            self.crawl_list[i].append(self.kakao_list[i])
            self.crawl_list[i].append(self.google_list[i])
            self.crawl_list[i].append(self.fruit_list[i])

        res = dict_json.toDict(key_list, self.crawl_list)      #(key값 리스트, value값 리스트)
        for k in res.keys():
            date_obj = datetime.strptime(res[k]['date'], '%Y_%m_%d')
            data = tagdata.Tagdata(
                name = res[k]['filename'],
                date = date_obj,
                title = res[k]['title'],
                kakao_tag = res[k]['kakao_tag'],
                google_tag = res[k]['google_tag'],
                title_tag = res[k]['fruit_dict']
            )
            data.save()

        images = sorted(glob.glob('C:\\Project2020\\venv\\images\\*.jpg'), key=os.path.getctime)

        for i in images:
            example = img_to_mongo.Image(name = i[26:] )
            with open(i, 'rb') as img:
                name = i[26:]
                example.image.replace(img, filename = name)
                example.save()
        
    def freq_today(self):
        date = datetime.today().strftime('%Y-%m-%d')
        fruit_statistics.fruit_statistics(date)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.setWindowTitle("구페네카")

    #위젯 디자인
    fontVar = QFont("나눔스퀘어")
    app.setFont(fontVar)
    app.setStyle("Fusion")  #['windowsvista', 'Windows', 'Fusion', 'Breeze']  print(PyQt5.QtWidgets.QStyleFactory.keys())
    qp = QPalette()
    qp.setColor(QPalette.ButtonText, Qt.black)
    qp.setColor(QPalette.Window, Qt.white)   
    qp.setColor(QPalette.Button, Qt.white)   
    app.setPalette(qp)
    
    sys.exit(app.exec_())
