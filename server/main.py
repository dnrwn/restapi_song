import traceback, logging, datetime, configparser
from flask import Flask, request, render_template

import db_f.Query as Query
import db_f.db as db


########## Common func ##########
server = Flask(__name__)

# IP, PORT, PATH 정보 read
config = configparser.ConfigParser()
config.read('server/config.ini')
path = config['server']['directory']

# console log 수집 form 정의
time = datetime.datetime.now().strftime('%y%m%d_%H%M%S')
log_format = '%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s' # 로그 포맷 설정

logger = logging.getLogger('server') # 로거 생성
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler(f'{path}log/server_{time}.log') # 파일 핸들러 설정
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter(log_format))

console_handler = logging.StreamHandler() # 콘솔 핸들러 설정
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter(log_format))

logger.addHandler(file_handler) # 핸들러를 로거에 추가

# Response form 정의
def response(a, b=None, c=None):
    if a == 0:
        return {
            "Result": "NG",
            "Description": "%s NG" % b,
            "Message": c
        }
    elif a == 1:
        return {
            "Result": "PASS",
            "Description": "%s PASS" % b,
            "Message": c
        }
    else:
        return {
            "Result": "Error",
            "Description": "Null"
        }


########## Route func ##########
@server.route('/', methods=['GET'])
def route_default():
    return logic_default(request.host)

@server.route('/ui')
def route_ui():
    return logic_ui('test_test.html')

@server.route('/func_1', methods=['GET'])
def route_func_1():
    return logic_select(request)

@server.route('/func_2', methods=['POST'])
def route_func_2():
    return logic_update(request)

@server.route('/func_3', methods=['POST'])
def route_func_3():
    return logic_insert(request)

@server.route('/func_4', methods=['POST', 'DELETE'])
def route_func_4():
    return logic_delete(request)


########## Logic func ##########
def logic_default(route_data):
    server.logger.info(logic_default.__name__)
    ip_1 = route_data.split(':')[0]
    po_1 = route_data.split(':')[1]
    a = (f'<p><a href="http://{ip_1}:{po_1}/func_1" methods="GET"> Select </a></p>'
         f'<p><a href="http://{ip_1}:{po_1}/func_2" methods="POST"> Update </a></p>'
         f'<p><a href="http://{ip_1}:{po_1}/func_3" methods="GET"> Insert </a></p> '
         f'<p><a href="http://{ip_1}:{po_1}/func_4" methods="POST"> Delete </a></p> '
         f'<p><a href="http://{ip_1}:{po_1}/ui" > web app </a></p>')
    return a

def logic_ui(route_data='test_test.html'): # 기본 UI
    server.logger.info(logic_ui.__name__)
    return render_template(route_data)

def logic_select(route_data): # Select
    server.logger.info(logic_select.__name__)
    try:
        val = int(route_data.values.get('idx'))
        a = response(1, b='Select')
        a['data'] = db.Database.execute(Query.get_select_one(val))
        return a

    except Exception as m:
        server.logger.info(traceback.format_exc())
        return response(0, 'Select', c=str(m))

def logic_update(route_data): # Update
    server.logger.info(logic_update.__name__)
    try:
        if len(route_data.form) != 0:
            val = route_data.form.to_dict()
            val['idx'] = int(val['idx'])
            val['input_1'] = int(val['input_1'])
            if val['input_4'].lower() == 'false' or val['input_4'].lower() == '0':
                val['input_4'] = False
            elif val['input_4'].lower() == 'true' or val['input_4'].lower() == '1':
                val['input_4'] = True
            else:
                raise ValueError('Invalid input: Expected "false" or "true"')
        else:
            val = route_data.get_json()
        db.Database.execute(Query.get_select_one(int(val['idx'])))
        db.Database.execute(Query.post_update(val))
        a = db.Database.execute(Query.get_select_one(int(val['idx'])))
        b = response(1, 'Update')
        b['data'] = a
        return b

    except Exception as m:
        server.logger.info(traceback.format_exc())
        return response(0, 'Update', c=str(m))

def logic_insert(route_data): # Insert
    server.logger.info(logic_insert.__name__)
    try:
        if len(route_data.form) != 0:
            val = route_data.form.to_dict()
            val['input_1'] = int(val['input_1'])
            if val['input_4'].lower() == 'false' or val['input_4'].lower() == '0':
                val['input_4'] = False
            elif val['input_4'].lower() == 'true' or val['input_4'].lower() == '1':
                val['input_4'] = True
            else:
                raise ValueError('Invalid input: Expected "false" or "true"')
        else:
            val = route_data.get_json()
        db.Database.execute(Query.post_insert(val))
        a = db.Database.execute(Query.get_select_all())
        b = response(1, 'Insert')
        b['data'] = a[-1]
        return b

    except Exception as m:
        server.logger.info(traceback.format_exc())
        return response(0, 'Insert', c=str(m))

def logic_delete(route_data): # Delete
    server.logger.info(logic_delete.__name__)
    try:
        if len(route_data.form) != 0 and route_data.method == 'POST':
            val = int(route_data.form['idx'])
        else:
            val = int(route_data.values.get('idx'))
        db.Database.execute(Query.delete_delete(val))
        a = response(1, 'Delete')
        a['idx'] = val
        return a

    except Exception as m:
        server.logger.info(traceback.format_exc())
        return response(0, 'Delete', c=str(m))


if __name__ == "__main__":
    # server 구동부
    ip = config['server']['ip']
    port = config['server']['port']
    server.run(host=ip, port=port, debug=True)
