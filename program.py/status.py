from tabulate import tabulate
import Connection
def Status():
    conn = None
    cur = None
    try:
        conn,cur = Connection.connection()
        cur.execute('''
            SELECT b.book_id,
                   b.book_name,
                   br.borrower_name as last_borrower,
                   l.date_borrowed,
                   l.date_returned
            FROM Books_Table b
            LEFT JOIN Loans_Table l
              ON l.loan_id = (
                  SELECT MAX(loan_id) FROM Loans_Table WHERE Book_Assigned_Id = b.book_id
                )
            LEFT JOIN Borrowers_Table br
              ON l.borrower_id = br.borrower_id;
        ''')
        loans = [dict(row) for row in cur.fetchall()]
        if not loans:
            print("No record to show")
            return
        for loan in loans:
            if loan['date_returned'] == None and loan['date_borrowed'] == None:
                loan['status'] = 'Available'
            elif loan['date_returned'] == None:
                loan['status'] = 'Not Available'
            elif not loan['date_returned'] == None:
                loan['status'] = 'Available'
        print(tabulate(loans, headers="keys", tablefmt="grid"))
            
    except Exception as error:
        print("Error has occured at status",error)
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
            
            
