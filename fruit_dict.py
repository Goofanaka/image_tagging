# -*- encoding: utf-8 -*-

def fruit_check(title):
    fruit_list = []

    for text in title:
        tags = []
        
        if "사과" in text[1]:
            tags.append("apple")

        elif ("단감" in text[1]) or ("곶감" in text[1]) or ("반건시" in text[1]) or ("홍시" in text[1]) or ("감말랭이" in text[1]):
            tags.append("persimmon")

        elif ("감귤" in text[1]) or ("오렌지" in text[1]) or ("레드향" in text[1]) or ("한라봉" in text[1]) or ("천혜향" in text[1]) or ("황금향" in text[1]) or ("유자" in text[1]) or ("홍미향" in text[1]):
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
            tags.append("papadya")

        elif "코코넛" in text[1]:
            tags.append("coconut")

        elif "자두" in text[1]:
            tags.append("plum")

        elif ("자몽" in text[1]) or ("메로골드" in text[1]):
            tags.append("grapefruit")

        elif ("잭후르츠" in text[1]) or ("잭프룻" in text[1]) or ("잭프루트" in text[1]) or ("잭플룻" in text[1]):
            tags.append("jackfruit")

        elif ("베리" in text[1]) or ("아로니아" in text[1]) or ("블랙커런트" in text[1]) or ("오미자" in text[1]) or ("복분자" in text[1]) or ("꾸지뽕" in text[1]):
            tags.append("berry")

        elif "배" in text[1]:
            tags.append("pear")

        else:
            tags.append("fruit_etc")

        fruit_list.append(tags)
    
    return fruit_list
