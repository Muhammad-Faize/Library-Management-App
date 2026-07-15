import Connection

def Add_Loan():
    conn = None
    cur = None
    while True:
        try:
            conn,cur = Connection.connection()
            cur.execute('''SELECT Book_Id,Book_Name FROM books_table LEFT JOIN loans_table ON books_table.Book_Id = loans_table.Book_Assigned_Id AND loans_table.Date_Returned IS NULL WHERE loans_table.Book_Assigned_Id IS NULL ORDER BY Book_Id ASC ; ''')
            books = cur.fetchall()
            if not books:
                print("No books exists")
                return
            for book in books:
                print(f"{book['book_id']} : {book['book_name']}")
            user_borrow_book_id = input("Enter book Id: ")
            user_borrower = input("Enter Borrower name: ").strip().capitalize()
            if user_borrower.isdigit():
                print("Enter valid data")
                continue
            if user_borrower.lower() == 'q':
                return
            if user_borrow_book_id.lower() == 'q':
                return
            if not user_borrow_book_id.isdigit():
                print("Book ID must be digits")
                continue
            user_borrow_book_id = int(user_borrow_book_id)
            is_valid = False
            for book in books:
                if user_borrow_book_id == book['book_id']:
                    is_valid = True
            if is_valid:   
                cur.execute('''INSERT INTO loans_table (Borrower_Name,book_Assigned_Id) VALUES (%s,%s)''',(user_borrower,user_borrow_book_id))
                conn.commit()
                print("Book has been borrowed")
            else:
                print("Invalid book id")
                continue
        except Exception as error:
            print("Error occured at add_loan",error)
            return
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()
        
        break