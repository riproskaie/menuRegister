from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.kioskdb


@app.route('/')
def home():
    return render_template('menuRegister.html')


@app.route('/api/menus', methods=['POST'])
def write_menus():
    print(request.form['isCombo'])
    print(request.form['image'])
    print(request.form['menuType'])
    print(request.form['nameKr'])
    print(request.form['nameEng'])
    print(request.form['calories'])
    print(request.form['price'])
    print(request.form['extraPrice'])
    print(request.form['defaultCombo'])
    print(request.form['isDefaultCombo'])
    print(request.form['side'])
    print(request.form['drink'])
    print(request.form.getlist('ingredientsAllergicKr'))
    print(request.form.getlist('ingredientsAllergicEng'))
    print(request.form.getlist('ingredientsNonAllergicKr'))
    print(request.form.getlist('ingredientsNonAllergicEng'))
    print(request.form['isDiscounted'])
    print(request.form['isSoldOut'])
    print(request.form['isRecommended'])
    print(request.form['isDiscontinued'])

    isCombo = request.form['isCombo']
    image = request.form['image']
    menuType = request.form['menuType']
    nameKr = request.form['nameKr']
    nameEng = request.form['nameEng']
    calories = request.form['calories']
    price = request.form['price']
    extraPrice = request.form['extraPrice']
    defaultCombo = request.form['defaultCombo'],
    isDefaultCombo = request.form['isDefaultCombo']
    side = request.form['side']
    drink = request.form['drink']
    ingredientsAllergicKr = request.form.getlist('ingredientsAllergicKr')
    ingredientsAllergicEng = request.form.getlist('ingredientsAllergicEng')
    ingredientsNonAllergicKr = request.form.getlist('ingredientsNonAllergicKr')
    ingredientsNonAllergicEng = request.form.getlist('ingredientsNonAllergicEng')
    isDiscounted = request.form['isDiscounted']
    isSoldOut = request.form['isSoldOut']
    isRecommended = request.form['isRecommended']
    isDiscontinued = request.form['isDiscontinued']

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
    return jsonify({'result': 'success', 'msg': 'menus 연결되었습니다'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
