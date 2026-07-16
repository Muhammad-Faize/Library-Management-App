CREATE TABLE IF NOT EXISTS Authors_Table(
	Author_Id SERIAL PRIMARY KEY,
	Author_Name VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS Books_Table(
 	Book_Id SERIAL PRIMARY KEY,
	Book_Name VARCHAR(255),
	Author_Assigned_Id INT,
	FOREIGN KEY (Author_Assigned_Id) REFERENCES Authors_Table(Author_Id)
);

CREATE TABLE IF NOT EXISTS Borrowers_Table(
	Borrower_Id SERIAL PRIMARY KEY,
	Borrower_Name VARCHAR(255)
);
CREATE TABLE IF NOT EXISTS Loans_Table(
	Loan_Id SERIAL PRIMARY KEY,
	Borrower_Id INT,
	Book_Assigned_Id INT,
	book_status VARCHAR(255),
	Date_Returned TIMESTAMP,
	Date_Borrowed TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY (Borrower_Id) REFERENCES Borrowers_Table(Borrower_Id),
	FOREIGN KEY (Book_Assigned_Id) REFERENCES Books_Table(Book_Id)
);

