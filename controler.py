import sqlite3


def store_player_in_db(user):
    conn = sqlite3.connect('volleyball.db')
    c = conn.cursor()
    nickname = user.get('nickname')
    sex = user.get('sex')
    address = user.get('address')
    c.execute('INSERT INTO players_test(nickname, sex, address) VALUES(?,?,?)', [nickname, sex, address])
    print("Storing this tripplet: ", user.get('nickname'), user.get('sex'), user.get('address'))
    conn.commit()
    return


def get_all_players():
    conn = sqlite3.connect('volleyball.db')
    c = conn.cursor()
    results = c.execute('SELECT * FROM players_test').fetchall()
    return results


def delete_player_from_db(id):
    conn = sqlite3.connect('volleyball.db')
    c = conn.cursor()
    c.execute("DELETE FROM players_test WHERE (id = ?)", [id])
    conn.commit()
    return "Successfully deleted player"
