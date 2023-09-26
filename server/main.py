from flask import Flask, request
from db_f import db
import query

app = Flask(__name__)


def response(a, b=None, c=None):
    if a == 0:
        return {
            "result": "NG",
            "description": "%s NG" % b,
            "Message": c
        }
    elif a == 1:
        return {
            "result": "OK"
        }
    else:
        return {
            "result": "Error",
            "description": "Null"
        }


@app.route('/', methods=['GET'])
def default():
    a = 'http://%s:%s/func_1 or func_2' %(ip, port)
    return a


# DB 연동 기능 : 조회, 수정
@app.route('/func_1', methods=['GET', 'POST'])
def func_1():
    print(func_1.__name__)
    if request.method == 'GET':
        try:
            a = response(1)
            a['data'] = db.Database.execute(query.get_select(int(request.values.get('idx'))))
            return a
        except Exception as m:
            return response(0, 'Select', c=str(m))
    elif request.method == 'POST':
        try:
            db.Database.execute(query.post_update(int(request.get_json()['idx']), request.get_json()['input_1'], request.get_json()['input_2']))
            a = response(1)
            a['data'] = db.Database.execute(query.get_select(int(request.get_json()['idx'])))
            return a
        except Exception as m:
            return response(0, 'Update', c=str(m))


# DB 연동 기능 : 추가
@app.route('/func_2', methods=['POST'])
def func_2():
    try:
        print(func_2.__name__)
        db.Database.execute(query.post_insert(request.get_json()['input_1'], request.get_json()['input_2']))
        a = db.Database.execute(query.sql_get)

        b = response(1)
        b['data'] = a[-1]
        return b
    except Exception as m:
        return response(0, 'Insert', c=str(m))


if __name__ == "__main__":
    ip = '0.0.0.0'
    port = 70
    app.run(host=ip, port=port, debug=True)

