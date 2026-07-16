import Connection
import os
from tabulate import tabulate

def search_book():
    while True:
        print("1.Search by author name")
        print("2.Search by book title")
        print("-----------------------")
        user_inp = input("Enter one of the choice:  ").strip()
        os.system('cls')
        if not user_inp.isdigit():
            print("Enter numeric value only")
            continue
        user_inp = int(user_inp)
        if user_inp == 1:
            search_by_author()
        elif user_inp == 2:
            search_by_title()
        else:
            print("Invalid input entered")
            continue
        break
    return
def search_by_author():
    conn = None
    cur = None
    try:
        conn,cur = Connection.connection()
        user_inp = input("Enter Author Name:     ").strip().capitalize()
        cur.execute('''SELECT * FROM Authors_Table;''')
        authors = [dict(row) for row in cur.fetchall()]
        is_valid = False
        for author in authors:
            if author['author_name'] == user_inp:
                is_valid = True
                break
        if is_valid:
            cur.execute('''SELECT * FROM Authors_Table WHERE author_name = %s ''',(user_inp,))
            required_author = [dict(row) for row in cur.fetchall()]
            required_author_id = required_author[0]['author_id']
            cur.execute('''SELECT * FROM Books_Table WHERE author_assigned_id = %s ''',(required_author_id,))
            required_books = [dict(row) for row in cur.fetchall()]
            print(tabulate(required_books,headers='keys',tablefmt='grid'))
            return
        else:
            print(f"no book found for author {user_inp}")
            return
    except Exception as error:
        print("Error occured ar search book:    ",error)
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
        
def search_by_title():
    conn = None
    cur = None
    try:
        conn,cur = Connection.connection()
        user_inp = input("Enter book title:     ").strip().capitalize()
        cur.execute('''SELECT * FROM Books_Table;''')
        books = [dict(row) for row in cur.fetchall()]
        is_valid = False
        for book in books:
            if book['book_name'] == user_inp:
                is_valid = True
                break
        if is_valid:
            cur.execute('''SELECT * FROM Books_Table WHERE book_name = %s ''',(user_inp,))
            required_books = [dict(row) for row in cur.fetchall()]
            print(tabulate(required_books,headers='keys',tablefmt='grid'))
            return
        else:
            print(f"no book found named {user_inp}")
            return
    except Exception as error:
        print("Error occured ar search book:    ",error)
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()