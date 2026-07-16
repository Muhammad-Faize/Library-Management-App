import os
import Connection
import Add_author,Add_book,Add_loan,Borrow_returned,status,view_stock,Status_borrow,Search_book,Add_borrower

def main():
    create_tables()
    print("Welcome To Library Management App")
    while True:
        print("----------------------------------")
        print("1.Add a Author:    ")
        print("2.Add a Book:    ")
        print("3.Enter a borrower")
        print("4.Borrow a book:    ")
        print("5.Returned a borrowed book:    ")
        print("6.View list of books:    ")
        print("7.View books status:    ")
        print("8.List of books borrowed by a specific user: ")
        print("9.Search a book")
        print("0.To exit")
        print("----------------------------------")
        user_inp = input("Choose one of the option: ").strip()
        os.system('cls')
        if not user_inp.isdigit():
            print("Entered value must be digit")
            continue
        user_inp = int(user_inp)
        if user_inp == 1:
            Add_author.Add_Author()
        elif user_inp == 2:
            Add_book.Add_Book()
        elif user_inp == 3:
            Add_borrower.add_borrower()
        elif user_inp == 4:
            Add_loan.Add_Loan()
        elif user_inp == 5:
            Borrow_returned.borrow_Returned()
        elif user_inp == 6:
            view_stock.View_Stock()
        elif user_inp == 7:
            status.Status()
        elif user_inp == 8:
            Status_borrow.status_borrow()
        elif user_inp == 9:
            Search_book.search_book()
        elif user_inp == 0:
            break
        else:
            print("Invalid entry:")
            continue
        user_inp2 = input("Enter to show the menu(q to exit)").strip()
        os.system('cls')
        if user_inp2.lower() == 'q':
            break
    print("----END----")
        
def create_tables():
    cur = None
    conn = None
    try:
        conn,cur = Connection.connection()
        folder = 'D:\\Faize\\Library_Management_App'
        files =[
            "script.sql"
        ]
        for file in files:
            file_path = os.path.join(folder,file)
            with open(file_path,"r") as f:
                script = f.read()
                cur.execute(script)
        conn.commit()
        print("Tables created")
    except Exception as error:
        print("An error has occured at create_table",error)
    finally:    
        if cur:
            cur.close()
        if conn:
            conn.close()


if __name__ == "__main__":
    main()
