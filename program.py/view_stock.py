import Connection
def View_Stock():
    conn = None 
    cur = None
    try:
        conn,cur = Connection.connection()
        cur.execute('''SELECT Author_Name,Book_Name FROM authors_table INNER JOIN books_table ON authors_table.Author_Id = books_table.Author_Assigned_Id ''')
        stocks = cur.fetchall()
        if not stocks:
            print("No record exists")
            return
        for stock in stocks:
            print(f"{stock['book_name']} by {stock['author_name']}")
    except Exception as error:
        print("An error occured at view stock",error)
        return
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()