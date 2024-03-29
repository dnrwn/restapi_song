from datetime import datetime

sql_get = "SELECT * FROM new_db.item;"
# date = datetime.now().strftime('%y-%m-%d %H:%M:%S')  ## time stamp 를 변수에 삽입할 경우 server 시작 시간으로 고정됨

def get_select(query):
    return ("SELECT * FROM new_db.item where idx = %d;"
            % query)


def post_insert(query):
    return (("INSERT INTO item (input_1, input_2, input_3, input_4, input_5, Create_date) "
             "VALUES('%d', '%d', '%s', '%s', '%d', '%s');")
            % (query['input_1'],
               query['input_2'],
               query.get('input_3'),  # get parameter 공란 = None
               query.get('input_4'),  # get parameter 공란 = None
               query.get('input_5', True),
               datetime.now().strftime('%y-%m-%d %H:%M:%S')))


def post_update(query):
    print(type(query))
    return ("UPDATE item SET Input_1='%d', Input_2='%d', Input_3='%s', Input_4='%s', input_5='%d', Update_date='%s' WHERE idx = %d;"
            % (query['input_1'],
               query['input_2'],
               query.get('input_3'),  # get parameter 공란 = None
               query.get('input_4'),  # get parameter 공란 = None
               query.get('input_5', True),
               datetime.now().strftime('%y-%m-%d %H:%M:%S'),
               query['idx']))


def delete_delete(query):
    return ("DELETE FROM new_db.item where idx=%d"
            % query)