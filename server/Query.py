from datetime import *


def date():
    return datetime.now().strftime('%y-%m-%d %H:%M:%S')  # time stamp 를 변수에 삽입할 경우 server 시작 시간으로 고정됨


def get_select_all():
    return "SELECT * FROM new_db.item;"


def get_select_one(query):
    return ("SELECT * FROM new_db.item where idx = %d;"
            % query
            )


def post_insert(query):
    return (("INSERT INTO item (input_1, input_2, input_3, input_4, create_date) "
             "VALUES('%d', '%s', '%s', '%d', '%s');")
            % (query['input_1'],
               query.get('input_2'),  # get parameter 공란 = None
               query.get('input_3'),  # get parameter 공란 = None
               query.get('input_4', True),
               date())
            )


def post_update(query):
    return ("UPDATE item SET input_1='%d', input_2='%s', input_3='%s', input_4='%d', update_date='%s' WHERE idx = %d;"
            % (
                query['input_1'],
                query.get('input_2'),  # get parameter 공란 = None
                query.get('input_3'),  # get parameter 공란 = None
                query.get('input_4', True),
                date(),
                query['idx'])
            )


def delete_delete(query):
    return ("DELETE FROM new_db.item where idx=%d;"
            % query
            )
