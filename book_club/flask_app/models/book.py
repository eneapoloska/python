from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
# create a regular expression object that we'll use later   

class Book:
    db_name='bookclub'
    def __init__(self,data):
        self.id = data['id'],
        self.title = data['title'],
        self.image = data['image'],
        self.description = data['description'],
        self.user_id = data['user_id'],
        self.created_at = data['created_at'],
        self.updated_at = data['updated_at']

    @classmethod
    def getAllBooks(cls):
        query= 'SELECT books.id, title, image, users.first_name as creator_name,users.last_name as creator_lastname FROM books LEFT JOIN users on books.user_id = users.id LEFT JOIN likes on likes.book_id = books.id GROUP BY books.id;'
        results =  connectToMySQL(cls.db_name).query_db(query)
        books= []
        for row in results:
            books.append(row)
        return books
        
    @classmethod
    def create_book(cls,data):
        query = 'INSERT INTO books (title, description, user_id, image) VALUES ( %(title)s, %(description)s, %(user_id)s, %(image)s );'
        result1=  connectToMySQL(cls.db_name).query_db(query, data)
        query2 = 'SELECT id from books ORDER BY id DESC LIMIT 1;'
        result2=  connectToMySQL(cls.db_name).query_db(query2)
        if result2:
            return result2[0]
    
    @classmethod
    def get_book_by_id(cls, data):
        query= 'SELECT books.id, books.user_id, books.title, books.image, books.description, books.created_at, books.updated_at, users.first_name as creator_name,users.last_name as creator_lastname FROM books LEFT JOIN users on books.user_id = users.id LEFT JOIN likes on likes.book_id = books.id WHERE books.id = %(book_id)s;'
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return results[0]


    @classmethod
    def get_user_posts(cls, data):
        query= 'SELECT * FROM users LEFT JOIN posts on posts.user_id = users.id WHERE users.id = %(user_id)s;'
        results = connectToMySQL(cls.db_name).query_db(query, data)
        posts = []
        for row in results:
            posts.append(row)
        return posts

    @classmethod
    def addLike(cls, data): # from def addLIKE path at posts.py
        query= 'INSERT INTO likes (book_id, user_id) VALUES ( %(book_id)s, %(user_id)s );'
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def removeLike(cls, data): #def removeLike(id): from the path of books.py
        query= 'DELETE FROM likes WHERE book_id = %(book_id)s and user_id = %(user_id)s;'
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def destroyBook(cls, data):
        query= 'DELETE FROM books WHERE books.id = %(book_id)s;'
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def updateBook(cls, data):
        query= 'UPDATE books SET description = %(description)s WHERE books.id = %(book_id)s;'
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def deleteAllLikes(cls, data):
        query= 'DELETE FROM likes WHERE likes.book_id = %(book_id)s;'
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def getUserWhoLiked(cls, data):
        query = 'SELECT book_id as id, users.first_name, users.last_name FROM likes LEFT JOIN users on likes.user_id = users.id WHERE book_id = %(book_id)s;'
        results = connectToMySQL(cls.db_name).query_db(query, data)
        usersWhoLiked = []
        for row in results:
            usersWhoLiked.append(row)
        return usersWhoLiked

    @staticmethod
    def validate_book(book):
        is_valid = True
        if len(book['title']) < 2:
            flash("Book title must be at least 2 characters.", 'title')
            is_valid = False
        if len(book['description']) < 5:
            flash("Book description must be at least 5 characters.", 'description')
            is_valid = False
        return is_valid