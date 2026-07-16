import Connection
from tabulate import tabulate
def View_Stock():
    conn = None 
    cur = None
    try:
        conn,cur = Connection.connection()
        cur.execute('''SELECT Authors_Table.Author_Name,Books_Table.Book_Name FROM Authors_Table INNER JOIN Books_Table ON Authors_Table.Author_Id = Books_Table.Author_Assigned_Id ''')
        stocks = [dict(row) for row in cur.fetchall()]
        if not stocks:
            print("No record exists")
            return
        print(tabulate(stocks,headers='keys',tablefmt='grid'))
    except Exception as error:
        print("An error occured at view stock",error)
        return
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()