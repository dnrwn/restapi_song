from flask import Flask, request, render_template
import traceback, logging, datetime

import db_f.Query as Query
import db_f.db as db

server = Flask(__name__)

# console log 수집 script
time = datetime.datetime.now().strftime('%y%m%d_%H%M%S')
logging.basicConfig(filename=f'server/log/server_{time}.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

def response(a, b=None, c=None):
    if a == 0:
        return {
            "Result": "NG",
            "Description": "%s NG" % b,
            "Message": c
        }
    elif a == 1:
        return {
            "Result": "PASS"
        }
    else:
        return {
            "Result": "Error",
            "Description": "Null"
        }


@server.route('/', methods=['GET'])
def default():
    server.logger.info(default.__name__)
    a = (f'<p><a href="http://{ip}:{port}/func_1" methods="POST"> Select Update </a></p>'
         f'<p><a href="http://{ip}:{port}/func_2" methods="GET"> Insert </a></p> '
         f'<p><a href="http://{ip}:{port}/func_3" methods="POST"> Delete </a></p> '
         f'<p><a href="http://{ip}:{port}/ui" > web app </a></p>')
    return a


@server.route('/ui')
def ui():
    server.logger.info(ui.__name__)
    return render_template('test_test.html')


# DB 연동 기능 : Select, Update
@server.route('/func_1', methods=['GET', 'POST'])
def func_1():
    server.logger.info(func_1.__name__)
    if request.method == 'GET':
        try:
            val = int(request.values.get('idx'))
            a = response(1)
            a['data'] = db.Database.execute(Query.get_select_one(val))
            return a

        except Exception as m:
            server.logger.info(traceback.format_exc())
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
            db.Database.execute(Query.get_select_one(int(val['idx'])))
            db.Database.execute(Query.post_update(val))
            a = db.Database.execute(Query.get_select_one(int(val['idx'])))
            b = response(1)
            b['data'] = a
            return a

        except Exception as m:
            server.logger.info(traceback.format_exc())
            return response(0, 'Update', c=str(m))

# DB 연동 기능 : insert
@server.route('/func_2', methods=['POST'])
def func_2():
    try:
        server.logger.info(func_2.__name__)
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
        server.logger.info(traceback.format_exc())
        return response(0, 'Insert', c=str(m))


# DB 연동 기능 : Delete
@server.route('/func_3', methods=['POST', 'DELETE'])
def func_3():
    try:
        server.logger.info(func_3.__name__)
        if len(request.form) != 0 and request.method == 'POST':
            val = int(request.form['idx'])
        else:
            val = int(request.values.get('idx'))
        db.Database.execute(Query.delete_delete(val))
        a = response(1)
        a['idx'] = val
        return a

    except Exception as m:
        server.logger.info(traceback.format_exc())
        return response(0, 'Delete', c=str(m))


if __name__ == "__main__":
    # server 구동부
    ip = 'localhost'
    port = 70
    server.run(host=ip, port=port, debug=True)

