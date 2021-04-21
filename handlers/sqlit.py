import sqlite3

def reg_user(id):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute(""" CREATE TABLE IF NOT EXISTS user_time (
        id BIGINT,
        status_ref
        ) """)
    db.commit()

    # Бан лист
    sql.execute(""" CREATE TABLE IF NOT EXISTS ban_list (
            id BIGINT,
            status_ref
            ) """)
    db.commit()

    sql.execute(f"SELECT id FROM ban_list WHERE id ='{id}'")
    if sql.fetchone() is None:
        sql.execute(f"SELECT id FROM user_time WHERE id ='{id}'")
        if sql.fetchone() is None:
            sql.execute(f"INSERT INTO user_time VALUES (?,?)", (id, 1))
            db.commit()

def stata_user():
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    status = sql.execute(f'SELECT COUNT(*) FROM user_time').fetchone()[0]
    return status


def delite_user(id):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    try:
        sql.execute(f"SELECT id FROM user_time WHERE id ={id}")
        if sql.fetchone() != None:
            sql.execute(f'DELETE FROM user_time WHERE id ={id}')
            db.commit()

            db = sqlite3.connect('server.db')
            sql = db.cursor()
            sql.execute(f"SELECT id FROM ban_list WHERE id ='{id}'")
            if sql.fetchone() is None:
                sql.execute(f"INSERT INTO ban_list VALUES (?,?)", (id, 1))
                db.commit()
            return 1

        else:
            return 0

    except:
        return 404

def cheack_ban(id):
    db = sqlite3.connect('server.db')
    sql = db.cursor()

    sql.execute(f"SELECT id FROM ban_list WHERE id ='{id}'")
    if sql.fetchone() is None:
        return 1
    else: return 0