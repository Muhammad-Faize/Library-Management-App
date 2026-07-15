import Connection

def borrow_Returned():
    conn = None
    cur = None
    try:
        conn, cur = Connection.connection()
        cur.execute("""SELECT borrower_id, borrower_name, book_assigned_id FROM loans_table WHERE date_returned IS NULL;""") 
        loans = cur.fetchall() 
        if not loans:
            print("No active borrowed books")
            return
        for loan in loans:
            print(f"{loan['borrower_id']} : {loan['borrower_name']} : (book_Id: {loan['book_assigned_id']})")  
        while True:
            user_loan_id = input("Enter borrower ID to return book: ")
            if user_loan_id.lower() == 'q':
                return
            if not user_loan_id.isdigit():
                print("Invalid input")
                continue
            is_valid = False
            for loan in loans:
                if int(user_loan_id) == loan['borrower_id']:
                    is_valid = True
            if is_valid:        
                break
            else:
                print("The borrower id is invalid")
                continue
        cur.execute("""UPDATE loans_table SET date_returned = CURRENT_TIMESTAMP WHERE borrower_id = %s""", (int(user_loan_id),))
        
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