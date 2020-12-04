import sqlite3
from sqlite3 import Error

def post_sql_query(sql_query):
    with sqlite3.connect('my.db') as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(sql_query)
        except Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            print('SQLite traceback: ')
            exc_type, exc_value, exc_tb = sys.exc_info()
            print(traceback.format_exception(exc_type, exc_value, exc_tb))
            pass
        result = cursor.fetchall()
        return result


def create_userdata_table():
    orders_query = '''CREATE TABLE IF NOT EXISTS USERDATA
                        (user_id TEXT,
                        current_stage TEXT,
                        stage1 TEXT,stage2 TEXT,stage3 TEXT,
                        stage4 TEXT,stage5 TEXT,stage6 TEXT,
                        stage7 TEXT,stage8 TEXT,stage9 TEXT,
                        stage10 TEXT,stage11 TEXT,stage12 TEXT,
                        stage13 TEXT,stage14 TEXT,stage15 TEXT,
                        stage16 TEXT,stage17 TEXT,stage18 TEXT,
                        stage19 TEXT,stage20 TEXT,stage21 TEXT,
                        stage22 TEXT,stage23 TEXT,stage24 TEXT,
                        stage25 TEXT,stage26 TEXT,stage27 TEXT,
                        stage28 TEXT,stage29 TEXT, stage30 TEXT,
                        stage31 TEXT);'''
    post_sql_query(orders_query)


def user_in_db(current_id, user_list):
    for user in user_list:
        if user[0] == current_id:
            return [True, user[1]]
    return [False, '']


def grab_all_data(user):
    query = f'SELECT * FROM USERDATA '\
            f'WHERE user_id = "{user}";'
    return(post_sql_query(query))


def save_reply_to_db(stage_num, answer, user):
    stage = 'stage' + stage_num
    if stage_num == '31':
        next_stage = '3'
    else:
        next_stage = str(int(stage_num)+1)
    query = f'UPDATE USERDATA SET {stage} = "{answer}", '\
            f'current_stage = "{next_stage}" '\
            f'WHERE user_id = "{user}";'
    post_sql_query(query)
