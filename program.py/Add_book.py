import Connection

def Add_Book():
    conn = None
    cur = None
    while True:
        try:
            user_book = input("Enter Book name: ").strip().capitalize()
            if user_book.lower() == 'q':
                return
            conn,cur = Connection.connection()
            cur.execute('''SELECT Author_Id,Author_Name FROM authors_table; ''')
            authors = cur.fetchall()
            if not authors:
                print("No author exists in database")
                return
            while True:
                for author in authors:
                    print(f"{author['author_id']} :  {author['author_name']}")
                user_aa_id = input("Enter author id:    ")
                if user_aa_id.lower() == 'q':
                    return        
                if not user_aa_id.isdigit():
                    print("Author Id must be in digit")
                    continue
                user_aa_id = int(user_aa_id)         
                is_valid = False
                for author in authors:
                    if user_aa_id == author['author_id']:
                        is_valid = True
                        break
                if is_valid:    
                    cur.execute('''INSERT INTO books_table (Book_Name,Author_Assigned_Id) VALUES (%s,%s)''',(user_book,user_aa_id))
                    conn.commit()
                    print("Book added successfully")
                    break
                else:
                    print("Invalid author ID")
                    continue
                
        except Exception as error:
            print("Error occured at add_book",error)
            return
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()
        
        break 