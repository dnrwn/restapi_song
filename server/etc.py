from flask import Flask, jsonify, request

app = Flask(__name__)


# 연습
@app.route('/api_1', methods=['GET', 'POST', 'DELETE'])
def api_1():
    # Postman -> Parameter data 조회
    if request.method == 'GET':
        a = request.values.get('GET_1')
        print('Get 결과 : ', a)  # Server 내 동작
        return jsonify(a)  # Postman Response 값

    # Postman -> Body data 조회
    elif request.method == 'POST':
        b = request.get_json()
        # b = request.values.get('POST_1')
        print('POST 결과 : ', b)  # Server 내 동작
        return jsonify(b)  # Postman Response 값


# 자료형 검사 기능
@app.route('/api_2', methods=['POST'])
def api_2(item_a=None, item_b=None, item_c=None):
    try:
        item_a = request.get_json()['item_a']
        item_b = request.get_json()['item_b']
        print(len(item_b))
        # item_c = request.get_json()['item_c']
        # print(item_a, item_b, item_c)
        # print(type(item_a), type(item_b), type(item_c))

        if int(item_a) <= 100 and int(item_a) == int or len(item_b) <= 10 and item_b == str:
            print('hihi')
            a = 'Pass'
        # elif item_c == bool:
        #     a = 'Pass'
        else:
            a = 'Fail'

        print(a)
        return jsonify(a)

    except:
        print('입력 값 오류')
        return jsonify('입력 값 오류')


# 필수, 선택 data
def api_3(a, b=1):
    print(a)
    print(b)


if __name__ == "__main__":
    app.run(port='50')
