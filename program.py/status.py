import Connection
def Status():
    conn = None
    cur = None
    try:
        conn,cur = Connection.connection()
        cur.execute('''SELECT book_id,book_name,date_borrowed,date_returned FROM books_table FULL JOIN loans_table ON loans_table.Book_Assigned_Id = books_table.Book_Id ORDER BY Book_Id ASC;''')
        loans = cur.fetchall()
        if not loans:
            print("No record to show")
            return
        for loan in loans:
            print("---------------------")
            for keys,values in loan.items():
                print(f"{keys} : {values}")
    except Exception as error:
        print("Error has occured at status",error)
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close() 