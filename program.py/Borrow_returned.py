import Connection
from tabulate import tabulate
def borrow_Returned():
    conn = None
    cur = None
    try:
        conn, cur = Connection.connection()
        cur.execute("""SELECT Loans_Table.loan_id, Borrowers_Table.borrower_name, Loans_Table.book_assigned_id FROM Loans_Table INNER JOIN Borrowers_Table ON Loans_Table.borrower_id = Borrowers_Table.borrower_id WHERE Loans_Table.date_returned IS NULL;""") 
        loans = [dict(row) for row in cur.fetchall()] 
        if not loans:
            print("No active borrowed books")
            return
        print(tabulate(loans,headers = 'keys',tablefmt='grid'))
        while True:
            user_loan_id = input("Enter Loan ID to return book: ")
            if user_loan_id.lower() == 'q':
                return
            if not user_loan_id.isdigit():
                print("Invalid input")
                continue
            is_valid = False
            for loan in loans:
                if int(user_loan_id) == loan['loan_id']:
                    is_valid = True
                    break       
            if is_valid:        
                break
            else:
                print("The loan id is invalid")
                continue
        cur.execute("""UPDATE loans_table SET date_returned = CURRENT_TIMESTAMP WHERE loan_id = %s""", (int(user_loan_id),))
        
        conn.commit()
        print("Book returned successfully")
    
    except Exception as error:
        print("Error occured at borrow return :", error)
        return
    
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()