from tabulate import tabulate
import Connection
def Status():
    conn = None
    cur = None
    try:
        conn,cur = Connection.connection()
        cur.execute('''SELECT Books_Table.book_id,Books_Table.book_name,Loans_Table.loan_id,Borrowers_Table.borrower_name,Loans_Table.date_borrowed, Loans_Table.date_returned from Books_Table 
                        left join loans_table on loans_table.Book_Assigned_Id = Books_Table.Book_Id
                        left join borrowers_table on loans_table.borrower_id = borrowers_table.borrower_id
                        WHERE Loans_Table.loan_id IS NULL 
                        OR Loans_Table.date_returned IS NULL;''')
        loans = [dict(row) for row in cur.fetchall()]
        if not loans:
            print("No record to show")
            return
        print(tabulate(loans, headers="keys", tablefmt="grid"))
            
    except Exception as error:
        print("Error has occured at status",error)
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()        