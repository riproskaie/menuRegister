from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.kioskdb


@app.route('/')
def home():
    return render_template('menuRegister.html')


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

@app.route('/api/menus', methods=['GET'])
def read_menus():
    return jsonify({'result': 'success', 'msg': 'menus 연결되었습니다'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
