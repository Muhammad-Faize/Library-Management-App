import Connection

def Add_Author():
    conn = None
    cur = None
    while True:
        user_author = input("Enter Author name: ").strip().capitalize()
        if len(user_author) == 0:
            print("No data entered")
            continue
        if user_author.isdigit():
            print("Enter valid data")
            continue
        if user_author.lower() == 'q':
            return
        try:    
            conn,cur =  Connection.connection()
            cur.execute('''INSERT INTO authors_table (Author_Name) VALUES (%s)''',(user_author,))
            conn.commit()
            print("Author added successfully")
        except Exception as error:
            print("Error occured at add_author",error)
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()
        break