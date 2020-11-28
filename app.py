from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.kioskdb


@app.route('/')
def home():
    return render_template('menuRegister.html')


@app.route('/premium')
def premium():
    return render_template('premium.html')


@app.route('/whoppers')
def whoppers():
    return render_template("whoppers.html")


@app.route('/chickenBurgers')
def chickenBurgers():
    return render_template("chickenBurgers.html")


@app.route('/sides')
def sides():
    return render_template("sides.html")


@app.route('/drinks')
def drinks():
    return render_template("drinks.html")


@app.route('/desserts')
def desserts():
    return render_template('desserts.html')


@app.route('/inputForm')
def inputForm():
    return render_template('inputForm.html')


@app.route('/inputForm', methods=['POST'])
def write_menus():
    #여기 있는 스키마는 동환님 작업 pull해서 최신버전 확인해야.
    #강열님 스키마도 pull해서 최신작업 확인해야.
    # menuType = request.form['menuType']
    # nameKr = request.form['nameKr']
    # nameEng = request.form['nameEng']
    # image = request.form['image']
    # price = request.form['price']
    # extraPrice = request.form['extraPrice']
    # calories = request.form['calories']
    # isCombo = request.form['isCombo']
    # defaultCombo = request.form['defaultCombo']
    # isDefaultCombo = request.form['isDefaultCombo']
    # drink = request.form['drink']
    # sideMenu = request.form['sideMenu']
    # ingredientsNonAllergicKr = request.form['ingredientsNonAllergicKr']
    # ingredientsNonAllergicEng = request.form['ingredientsNonAllergicEng']
    # ingredientsAllergicKr = request.form['ingredientsAllergicKr']
    # ingredientsAllergicEng = request.form['ingredientsAllergicEng']
    # isSoldOut = request.form['isSoldOut']
    # isDiscounted = request.form['isDiscounted']
    # isRecommended = request.form['isRecommended']
    # isDiscontinued = request.form['isDiscontinued']

    # menu = {
    #     'menuType': menuType,
    #     'nameKr': nameKr,
    #     'nameEng': nameEng,
    #     'image': image,
    #     'price': price,
    #     'extraPrice': extraPrice,
    #     'calories': calories,
    #     'isCombo': isCombo,
    #     'defaultCombo': defaultCombo,
    #     'isDefaultCombo': isDefaultCombo,
    #     'drink': drink,
    #     'sideMenu': sideMenu,
    #     'ingredientsNonAllergicKr': ingredientsNonAllergicKr,
    #     'ingredientsNonAllergicEng': ingredientsNonAllergicEng,
    #     'ingredientsAllergicKr': ingredientsAllergicKr,
    #     'ingredientsAllergicEng': ingredientsAllergicEng,
    #     'isSoldOut': isSoldOut,
    #     'isDiscounted': isDiscounted,
    #     'isRecommended': isRecommended,
    #     'isDiscontinued': isDiscontinued
    # }
    #db.menus.insert_one(menu)
    return jsonify({'result': 'success', 'msg': '요청을 post했다.'})


@app.route('/premium', methods=['GET'])
def read_menus():
    print("get 호출")
    menu = list(db.menus.find({},{'_id': 0}))
    print("db 확인")
    return "connect"


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
