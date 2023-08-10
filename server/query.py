from datetime import datetime

date = datetime.now().strftime('%y-%m-%d %H:%M:%S')

sql_get = "SELECT * FROM new_db.item;"


def get_select(idx=1):
    return "SELECT * FROM new_db.item where idx = %d;" % idx


def post_insert(i_1, i_2, i_3=None):
    return "INSERT INTO item (input_1, input_2, input_3, Create_date) VALUES('%s', '%s', '%s', '%s');" % (i_1, i_2, i_3, date)


def post_update(idx, i_1, i_2, i_3=None):
    return "UPDATE new_db.item SET Input_1='%s', Input_2='%s', Input_3='%s', Update_date='%s' WHERE idx = %d;" % (i_1, i_2, i_3, date, idx)


def delete_delete(idx):
    return "DELETE FROM new_db.item where idx=%d" % idx

