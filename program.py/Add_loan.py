import Connection
from tabulate import tabulate
def Add_Loan():
    conn = None
    cur = None
    while True:
        try:
            conn,cur = Connection.connection()
            cur.execute('''SELECT Books_Table.Book_Id,Books_Table.Book_Name FROM Books_Table LEFT JOIN Loans_Table ON Books_Table.Book_Id = Loans_Table.Book_Assigned_Id AND Loans_Table.Date_Returned IS NULL WHERE Loans_Table.Book_Assigned_Id IS NULL ORDER BY Book_Id ASC ; ''')
            books = [dict(row) for row in cur.fetchall()]
            if not books:
                print("No books exists")
                return
            print(tabulate(books,headers='keys',tablefmt='grid'))
            user_borrow_book_id = input("Enter book Id: ")
            if user_borrow_book_id.lower() == 'q':
                return
            if not user_borrow_book_id.isdigit():
                print("Book ID must be digits")
                continue
            user_borrow_book_id = int(user_borrow_book_id)
            
            cur.execute('''SELECT * FROM Borrowers_table ; ''')
            borrowers = [dict(row) for row in cur.fetchall()]
            if not borrowers:
                print("No borrowers exists")
                return
            print(tabulate(borrowers,headers='keys',tablefmt='grid'))
            user_borrower = input("Enter Borrower id: ").strip()
            if user_borrower.lower() == 'q':
                return
            if not user_borrower.isdigit():
                print("Enter valid data")
                continue
            user_borrower = int(user_borrower)
            is_valid = False
            for book in books:
                if user_borrow_book_id == book['book_id']:
                    is_valid = True
            if not is_valid:   
                print("Invalid book id")
                continue
            
            is_valid2 = False
            for borrower in borrowers:
                if user_borrower == borrower['borrower_id']:
                    is_valid2 = True
            if is_valid2:   
                cur.execute('''INSERT INTO Loans_Table (Borrower_Id,Book_Assigned_Id,book_status) VALUES (%s,%s,'Not Available') ''',(user_borrower,user_borrow_book_id))
                conn.commit()
                print("Book has been borrowed")
                break
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
        
        