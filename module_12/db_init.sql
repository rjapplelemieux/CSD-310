-- drop test user if exists 
DROP USER IF EXISTS 'whatabook_user'@'localhost';

-- create whatabook_user and grant them all privileges to the whatabook database 
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'root';

-- grant all privileges to the whatabook database to user whatabook_user on localhost 
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

-- drop contstraints if they exist
ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

-- drop tables if they exist
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;

/*
    Create table(s)
*/
CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);

/*
    insert store record 
*/
INSERT INTO store(locale)
    VALUES('111 Winnie Dr, Bellevue, NE 68005');

/*
    insert book records 
*/
INSERT INTO book(book_name, author, details)
    VALUES('To Kill a Mockingbird', 'Harper Lee', 'A classic novel exploring racial injustice and moral growth in the American South');

INSERT INTO book(book_name, author, details)
    VALUES('1984', 'George Orwell', 'A dystopian novel depicting a totalitarian society and the struggle for individualism');

INSERT INTO book(book_name, author, details)
    VALUES('The Great Gatsby', 'F.Scott Fitzgerald', "A portrayal of the Roaring Twenties, capturing the excesses and illusions of the Jazz Age");

INSERT INTO book(book_name, author)
    VALUES('Pride and Prejudice', 'Jane Austen');

INSERT INTO book(book_name, author)
    VALUES('The Shining', 'Stephen King');

INSERT INTO book(book_name, author)
    VALUES("Harry Potter and the Sorcerer's Stone", 'J.K. Rowling');

INSERT INTO book(book_name, author)
    VALUES('The Da Vinci Code', 'Dan Brown');

INSERT INTO book(book_name, author)
    VALUES('The Hitchhikers guide to the Galaxy', 'Douglas Adams');

INSERT INTO book(book_name, author)
    VALUES('The Catcher and the Rye', 'J.D. Salinger');

/*
    insert user
*/ 
INSERT INTO user(first_name, last_name) 
    VALUES('Atticus', 'Finch');

INSERT INTO user(first_name, last_name)
    VALUES('Winston', 'Smith');

INSERT INTO user(first_name, last_name)
    VALUES('Jay', 'Gatsby');

/*
    insert wishlist records 
*/
INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Atticus'), 
        (SELECT book_id FROM book WHERE book_name = 'To Kill a Mockingbird')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Winston'),
        (SELECT book_id FROM book WHERE book_name = '1984')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Jay'),
        (SELECT book_id FROM book WHERE book_name = 'the Great Gatsby')
    );
