from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.kioskdb

#더미데이터 입력 (성공적으로 작동됩니다)
db.menus.insert_one({'menuType': '와퍼', 'nameKr': '와퍼', 'nameEng': 'Whopper', 'productImage': 'https://imgur.com/KRRUR8g',
                     'comboImage': 'https://i.imgur.com/uhJ1Hkb.png', 'price': 5000, 'extraPrice': 2000, 'calories': 233,
                     'ingredientsNonAllergicKr': ['밀가루'], 'ingredientsNonAllergicEng': ['flour'], 'ingredientsAllergicKr': ['쇠고기', '난류'],
                     'ingredientsAllergicEng': ['beef', 'egg'], 'isSoldOut': False, 'isDiscounted': False,
                     'isRecommended': True, 'isDiscontinued': False})

all_menus = list(db.menus.find({}))

print(all_menus[0])
