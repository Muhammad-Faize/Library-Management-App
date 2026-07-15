from tabulate import tabulate
import Connection
def Status():
    conn = None
    cur = None
    try:
        conn,cur = Connection.connection()
        cur.execute('''SELECT borrower_id,borrower_name,book_name,date_borrowed,date_returned FROM books_table FULL JOIN loans_table ON loans_table.Book_Assigned_Id = books_table.Book_Id ORDER BY Book_Id ASC;''')
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