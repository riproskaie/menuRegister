from flask import Flask, render_template, jsonify, request, make_response
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.kioskdb


@app.route('/')
def home():
    return render_template('menuRegister.html')


@app.route('/api/menus', methods=['POST'])
def write_menus():
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

    # 서버상으로 메뉴이름을 단품인 경우 [단품], 세트인경우 [세트]를  post한다
    return jsonify({'result': 'success', 'msg': '요청을 post했다.'})

@app.route('/api/menus', methods=['GET'])
def read_menus():
    menus = list(db.menus.find({}))
    menus[0]['_id'] = str(menus[0]['_id']) # ObjectId 값은 str 로 형변환시 내부값만 추출된다
    return jsonify({'result': 'success', 'menus_list': menus})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
