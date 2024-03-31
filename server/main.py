from flask import Flask, request

import traceback
import Query
import node
import db_f.db as db

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
            a = response(1)
            a['data'] = db.Database.execute(Query.get_select_one(val))
            return a

        except Exception as m:
            print(traceback.format_exc())
            return response(0, 'Select', c=str(m))

    elif request.method == 'POST':
        try:
            val = request.get_json()
            db.Database.execute(Query.post_update(val))
            a = db.Database.execute(Query.get_select_one(int(val['idx'])))
            print(a)
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
        db.Database.execute(Query.post_insert(val))
        a = db.Database.execute(Query.get_select_all())
        b = response(1)
        b['data'] = a[-1]
        return b

    except Exception as m:
        print(traceback.format_exc())
        return response(0, 'Insert', c=str(m))


# DB 연동 기능 : Delete
@app.route('/func_3', methods=['DELETE'])
def func_3():
    try:
        print(func_3.__name__)
        val = int(request.values.get('idx'))
        db.Database.execute(Query.delete_delete(val))
        a = response(1)
        a['idx'] = val
        return a

    except Exception as m:
        print(traceback.format_exc())
        return response(0, 'Delete', c=str(m))


if __name__ == "__main__":
    ip = 'localhost'
    port = 70
    app.run(host=ip, port=port, debug=True)
