from flask import Flask, request
from db_f import db
import Query, traceback

app = Flask(__name__)


def response(a, b=None, c=None):
    if a == 0:
        return {
            "Result": "NG",
            "Description": "%s NG" % b,
            "Message": c
        }
    elif a == 1:
        return {
            "Result": "OK"
        }
    else:
        return {
            "Result": "Error",
            "Description": "Null"
        }


@app.route('/', methods=['GET'])
def default():
    a = 'http://%s:%s/func_1 or func_2' % (ip, port)
    return a


# DB 연동 기능 : Select, Update
@app.route('/func_1', methods=['GET', 'POST'])
def func_1():
    print(func_1.__name__)
    if request.method == 'GET':
        try:
            val = int(request.values.get('idx'))
            print(val)
            a = response(1)
            a['data'] = db.Database.execute(Query.get_select(val))

            return a
        except Exception as m:
            return response(0, 'Select', c=str(m))
    elif request.method == 'POST':
        try:
            val = request.get_json()
            print(val)
            db.Database.execute(Query.post_update(val))
            a = db.Database.execute(Query.get_select(int(val['idx'])))
            b = response(1)
            b['data'] = a

            return a
        except Exception as m:
            print(traceback.format_exc())
            return response(0, 'Update', c=str(m))


# DB 연동 기능 : insert
@app.route('/func_2', methods=['POST'])
def func_2():
    try:
        print(func_2.__name__)
        val = request.get_json()
        print(val)
        db.Database.execute(Query.post_insert(val))
        a = db.Database.execute(Query.sql_get)
        b = response(1)
        b['data'] = a[-1]

        return b
    except Exception as m:
        return response(0, 'Insert', c=str(m))


if __name__ == "__main__":
    ip = 'localhost'
    port = 70
    app.run(host=ip, port=port, debug=True)

