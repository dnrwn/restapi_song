from flask import Flask, request, render_template

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
    a = (f'<p><a href="http://{ip}:{port}/func_1" methods="POST"> Select Update </a></p>'
         f'<p><a href="http://{ip}:{port}/func_2" methods="GET"> Insert </a></p> '
         f'<p><a href="http://{ip}:{port}/func_3" methods="POST"> Delete </a></p> '
         f'<p><a href="http://{ip}:{port}/ui" > web app </a></p>')
    return a


@app.route('/ui')
def ui():
    return render_template('test_test.html')


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
            if len(request.form) != 0:
                val = request.form.to_dict()
                val['idx'] = int(val['idx'])
                val['input_1'] = int(val['input_1'])
                val['input_4'] = int(val['input_4'])
            else:
                val = request.get_json()
            db.Database.execute(Query.post_update(val))
            a = db.Database.execute(Query.get_select_one(int(val['idx'])))
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
        if len(request.form) != 0:
            val = request.form.to_dict()
            val['input_1'] = int(val['input_1'])
            val['input_4'] = int(val['input_4'])
        else:
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
@app.route('/func_3', methods=['POST', 'DELETE'])
def func_3():
    try:
        print(func_3.__name__)
        if len(request.form) != 0 and request.method == 'POST':
            val = int(request.form['idx'])
        else:
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
