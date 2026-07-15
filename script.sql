CREATE TABLE IF NOT EXISTS Authors_Table(
	Author_Id SERIAL PRIMARY KEY,
	Author_Name VARCHAR(255)
);
SELECT * FROM Authors_Table;

CREATE TABLE IF NOT EXISTS Books_Table(
 	Book_Id SERIAL PRIMARY KEY,
	Book_Name VARCHAR(255),
	Author_Assigned_Id INT,
	FOREIGN KEY (Author_Assigned_Id) REFERENCES Authors_Table(Author_Id)
);
SELECT * FROM Books_Table;	

CREATE TABLE IF NOT EXISTS Loans_Table(
	Borrower_Id SERIAL PRIMARY KEY,
	Borrower_Name VARCHAR(255),
	Book_Assigned_Id INT,
	Date_Returned TIMESTAMP,
	Date_Borrowed TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY (Book_Assigned_Id) REFERENCES Books_Table(Book_Id)
);
SELECT * FROM Books_Table;