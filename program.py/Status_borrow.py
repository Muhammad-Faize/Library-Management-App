from tabulate import tabulate
import Connection
def status_borrow():
    conn = None
    cur = None
    while True:
        try:
            conn,cur = Connection.connection()
            cur.execute('''
                        SELECT DISTINCT Borrowers_Table.borrower_id, Borrowers_Table.borrower_name
                        FROM Borrowers_Table
                        INNER JOIN Loans_Table 
                            ON Loans_Table.borrower_id = Borrowers_Table.borrower_id
                        WHERE Loans_Table.date_returned IS NULL;
                    ''')
            borrowers = [dict(row) for row in cur.fetchall()]
            if not borrowers:
                print("No record to show")
                return
            print(tabulate(borrowers , headers="keys", tablefmt="grid"))
            borrower_name = input("Enter borrower name:  ").strip().capitalize()
            if borrower_name.isdigit():
                print("Dont enter numeric value for name")
                continue
            borrower_names = [b["borrower_name"] for b in borrowers]
            if borrower_name not in borrower_names:
                print("Invalid borrower name")
                return
            cur.execute('''SELECT Books_Table.book_id,Books_Table.book_name,Loans_Table.loan_id,Borrowers_Table.borrower_name,Loans_Table.date_borrowed, Loans_Table.date_returned from Books_Table 
                            left join loans_table on loans_table.Book_Assigned_Id = Books_Table.Book_Id
                            left join borrowers_table on loans_table.borrower_id = borrowers_table.borrower_id
                            WHERE Borrowers_Table.borrower_name = %s
                            AND Loans_Table.date_returned IS NULL;
                        ''', (borrower_name,))
            loans = [dict(row) for row in cur.fetchall()]
            if not loans:
                print("No record to show")
                return
            print(tabulate(loans, headers="keys", tablefmt="grid"))
            break
            
        except Exception as error:
            print("Error has occured at status_borrow",error)
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()        