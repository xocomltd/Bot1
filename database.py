import sqlite3
import uuid


local_db = "database.db"

def init_db():
    conn = sqlite3.connect(local_db)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS login (
            id TEXT PRIMARY KEY,
            code TEXT)''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS accounts (
            id TEXT PRIMARY KEY,
            website TEXT,
            email TEXT,
            password TEXT
        )
    ''')
    conn.commit()
    conn.close()
    
    return cursor

def fetch_login(code):
    conn = sqlite3.connect(local_db)
    cursor = conn.cursor()
    cursor.execute('SELECT code FROM login WHERE code=?', (code,))
    result = cursor.fetchone()
    conn.close()
    return bool(result)

def get_all_wsites():
    conn = sqlite3.connect(local_db)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM websites')
    websites = cursor.fetchall()
    conn.close()
    return websites

def get_all_accounts():
    conn = sqlite3.connect(local_db)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM accounts')
    accounts = cursor.fetchall()
    conn.close()
    return accounts

def delete_account(account_id):
    conn = sqlite3.connect(local_db)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM accounts WHERE id = ?', (account_id,))
    conn.commit()
    conn.close()


def insert_wsite(wsite):
    conn = sqlite3.connect(local_db)
    cursor = conn.cursor()
    cursor.execute('SELECT MAX(id) FROM websites' )
    max_value = cursor.fetchone()[0]
    if max_value is None:
        max_value = 0
    cursor.execute('''
        INSERT INTO websites (id,wsite)
        VALUES (?,?)
    ''', (max_value+1,wsite))

    conn.commit()
    conn.close()

def update_wsite(id,wsite):
    try:
        conn = sqlite3.connect(local_db)
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE websites
            SET  wsite = ?
            WHERE id = ?
        ''', (wsite,id))
        conn.commit()
        conn.close()
        print("updated:")
    except sqlite3.Error as e:
        print("Error updating card information:", e)

def delete_wsite(id):
    conn = sqlite3.connect(local_db)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM websites WHERE id = ?', (id,))
    conn.commit()
    conn.close()

def insert_account(email, password):
        conn = sqlite3.connect(local_db)
        cursor = conn.cursor()
        cursor.execute('SELECT MAX(id) FROM accounts')
        max_value = cursor.fetchone()[0]
        cursor.execute('''
            INSERT INTO accounts (id,email, password)
            VALUES (?, ?, ?)
        ''', (max_value+1,email, password))

        conn.commit()
        conn.close()
def update_account(id, email, password):
    conn = sqlite3.connect(local_db)
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE Accounts
        SET email = ?, password = ?
        WHERE id = ?
    ''', (email, password, id))

    conn.commit()
    conn.close()

def insert_login_code():
    conn = sqlite3.connect(local_db)
    cursor = conn.cursor()
    id = str(uuid.uuid4())  # Generate a unique id
    code = "hello"
    cursor.execute('INSERT INTO login (id, code) VALUES (?, ?)', (id, code))
    conn.commit()
    conn.close()
    
    print("Login code inserted successfully.")

def get_card():
    conn = sqlite3.connect(local_db)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM card_information')
    card = cursor.fetchall()
    conn.close()
    return card

def update_card(card_number, expiry_date, cvv):
        try:
            conn = sqlite3.connect(local_db)
            cursor = conn.cursor()
            cursor.execute('UPDATE card_information SET card_number=?, expiry_date=?, cvv=? WHERE id = 1',
                           (card_number, expiry_date, cvv))
            conn.commit()
            conn.close()
            print("Card information updated successfully.")
        except sqlite3.Error as e:
            print("Error updating card information:", e)


def get_paypal():
    conn = sqlite3.connect(local_db)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM paypal')
    paypal = cursor.fetchall()
    conn.close()
    return paypal


def update_paypal(email_account, password):
        try:
            conn = sqlite3.connect(local_db)
            cursor = conn.cursor()
            cursor.execute('UPDATE paypal SET email_account=?, password=? WHERE id = 1',
                           (email_account, password))
            conn.commit()
            conn.close()
            print("Paypal updated successfully.")
        except sqlite3.Error as e:
            print("Error updating Paypal:", e)




