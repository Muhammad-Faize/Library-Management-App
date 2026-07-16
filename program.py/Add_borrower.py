import Connection

def add_borrower():
    while True:
        user_inp =  input("Enter borrower name: ").strip().capitalize()
        if user_inp.isdigit():
            print("Entered value must not be numeric")
            continue
        conn = None
        cur = None
        try:
            conn,cur =  Connection.connection()
            cur.execute('''SELECT * FROM Borrowers_Table ''')
            borrowers = cur.fetchall()
            is_valid = True
            for borrower in borrowers:
                if borrower['borrower_name'] == user_inp:
                    is_valid = False
            if is_valid:
                cur.execute('''INSERT INTO Borrowers_Table (borrower_name) VALUES (%s)''',(user_inp,))
                conn.commit()
            else:
                print("Record already exists")
            break
        except Exception as error:
            print("error occured at add borrower",error)
            break
        finally:              
            if cur:
                cur.close()
            if conn:
                conn.close() 