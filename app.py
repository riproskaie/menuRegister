from flask import Flask, render_template, jsonify, request, make_response
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.kioskdb


@app.route('/')
def home():
    return render_template('menuRegister.html')


# 올리기/수정/삭제 기능 동시 수행
@app.route('/api/menus', methods=['POST'])
def postEditMenu():
    print(request.form['objectId'])
    objectId = request.form['objectId']
    isCombo = bool(int(request.form['isCombo']))
    image = request.form['image']
    menuType = request.form['menuType']
    nameKr = request.form['nameKr']
    nameEng = request.form['nameEng']
    calories = int(request.form['calories'])
    price = int(request.form['price'])
    extraPrice = int(request.form['extraPrice'])
    defaultCombo = request.form['defaultCombo']
    isDefaultCombo = bool(int(request.form['isDefaultCombo']))
    side = request.form['side']
    drink = request.form['drink']
    ingredientsAllergicKr = request.form.getlist('ingredientsAllergicKr[]')
    ingredientsAllergicEng = request.form.getlist('ingredientsAllergicEng[]')
    ingredientsNonAllergicKr = request.form.getlist('ingredientsNonAllergicKr[]')
    ingredientsNonAllergicEng = request.form.getlist('ingredientsNonAllergicEng[]')
    isDiscounted = int(request.form['isDiscounted'])
    isSoldOut = bool(int(request.form['isSoldOut']))
    isRecommended = bool(int(request.form['isRecommended']))
    isDiscontinued = bool(int(request.form['isDiscontinued']))

    coke = db.menus.find_one({'nameKr': '코카콜라(R)'})
    frenchFries = db.menus.find_one({'nameKr': '프렌치프라이(R)'})

    if isCombo and coke is not None:
        drink = coke['_id']
    else:
        drink = ""

    if isCombo and frenchFries is not None:
        side = frenchFries['_id']
        ingredientsNonAllergicKr.append('감자')
        ingredientsNonAllergicEng.append('potato')
    else:
        side = ""

    if objectId == "":
        menu = {
            "isCombo": isCombo,
            "image": image,
            "menuType": menuType,
            "nameKr": nameKr,
            "nameEng": nameEng,
            "calories": calories,
            "price": price,
            "extraPrice": extraPrice,
            "defaultCombo": defaultCombo,
            "isDefaultCombo": isDefaultCombo,
            "side": side,
            "drink": drink,
            "ingredientsAllergicEng": ingredientsAllergicEng,
            "ingredientsAllergicKr": ingredientsAllergicKr,
            "ingredientsNonAllergicEng": ingredientsNonAllergicEng,
            "ingredientsNonAllergicKr": ingredientsNonAllergicKr,
            "isDiscounted": isDiscounted,
            "isSoldOut": isSoldOut,
            "isRecommended": isRecommended,
            "isDiscontinued": isDiscontinued
        }

        db.menus.insert_one(menu)


    else:
        assert isinstance(objectId, object)
        _id = ObjectId(objectId)

        if db.menus.find_one({"_id": _id}) is not None:
            db.menus.update_one({"nameKr": nameKr}, {"$set": {'isCombo': isCombo, 'image': image,
                                                              'menuType': menuType, 'nameKr': nameKr,
                                                              'nameEng': nameEng, 'calories': calories,
                                                              'price': price, 'extraPrice': extraPrice,
                                                              'defaultCombo': defaultCombo,
                                                              'isDefaultCombo': isDefaultCombo,
                                                              'side': side, 'drink': drink,
                                                              'ingredientsAllergicKr': ingredientsAllergicKr,
                                                              'ingredientsAllergicEng': ingredientsAllergicEng,
                                                              'ingredientsNonAllergicKr': ingredientsNonAllergicKr,
                                                              'ingredientsNonAllergicEng': ingredientsNonAllergicEng,
                                                              'isDiscounted': isDiscounted,
                                                              'isSoldOut': isSoldOut,
                                                              'isRecommended': isRecommended,
                                                              'isDiscontinued': isDiscontinued}})

    # 서버상으로 메뉴이름을 단품인 경우 [단품], 세트인경우 [세트]를  post한다
    return jsonify({'result': 'success', 'msg': '요청을 post했다.'})


@app.route('/api/menus', methods=['GET'])
def readMenus():
    menus = list(db.menus.find({}))
    for i in range(0, len(menus)):
        menus[i]['_id'] = str(menus[i]['_id'])  # ObjectId 값은 str 로 형변환시 내부값만 추출된다
        menus[i]['side'] = str(menus[i]['side'])
        menus[i]['drink'] = str(menus[i]['drink'])
        if menus[i]['isCombo'] and '감자' in menus[i]['ingredientsNonAllergicKr']:
            menus[i]['ingredientsNonAllergicKr'].remove('감자')
            menus[i]['ingredientsNonAllergicEng'].remove('potato')

    return jsonify({'result': 'success', 'menus_list': menus})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
