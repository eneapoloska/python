from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    db_name='bookclub'
    def __init__(self,data):
        self.id = data['id'],
        self.first_name = data['first_name'],
        self.last_name = data['last_name'],
        self.email = data['email'],
        self.password = data['password'],
        self.created_at = data['created_at'],
        self.updated_at = data['updated_at']
    
    #Class Method to create a user
    @classmethod
    def create_user(cls,data):
        query = 'INSERT INTO users (email, first_name, last_name, password) VALUES ( %(email)s, %(first_name)s, %(last_name)s, %(password)s);'
        return connectToMySQL(cls.db_name).query_db(query, data)# when we create a user we dont need to get a result back,
                                                                #but just to return the connetionc to MySQL

    @classmethod
    def getAllUsers(cls):
        query= 'SELECT * FROM users;'
        results =  connectToMySQL(cls.db_name).query_db(query)
        users= []
        for row in results:
            users.append(row)
        return users
    
    @classmethod
    def get_user_by_id(cls, data):
        query= 'SELECT * FROM users WHERE users.id = %(user_id)s;'
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return results[0]
        
    @classmethod
    def get_user_by_email(cls, data):
        query= 'SELECT * FROM users WHERE users.email = %(email)s;'#%(email)s is from the data 'email': request.form['email'] from users.py path
        results = connectToMySQL(cls.db_name).query_db(query, data)
        if len(results)<1:#+
            return False#+
        return results[0] # when we get staff from ID and EMAIL do allways  return results[0]
                            #it will be a list return the first element of the list 
        

    @classmethod
    def get_all_user_info(cls, data):
        query= 'SELECT * FROM users LEFT JOIN books on books.user_id = users.id WHERE users.id = %(user_id)s;'
        results =  connectToMySQL(cls.db_name).query_db(query, data)
        books = []
        for row in results:
            books.append(row)
        return books
    
    @classmethod
    def get_logged_user_liked_books(cls, data):
        query = 'SELECT book_id as id FROM likes LEFT JOIN users on likes.user_id = users.id WHERE user_id = %(user_id)s;'
        results = connectToMySQL(cls.db_name).query_db(query, data)
        booksLiked = []
        for row in results:
            booksLiked.append(row['id'])
        return booksLiked
    
    @staticmethod
    def validate_user(user):
        is_valid = True
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!", 'emailRegister')
            is_valid = False
        if len(user['first_name']) < 2:
            flash("Name must be at least 2 characters.", 'first_nameRegister')
            is_valid = False
        if len(user['last_name']) < 2:
            flash("Last name be at least 2 characters.", 'last_nameRegister')
            is_valid = False
        if len(user['password']) < 8:
            flash("Password be at least 8 characters.", 'passwordRegister')
            is_valid = False
        if user['confirmpassword'] != user['password']:
            flash("Password do not match!", 'passwordRegister')
            is_valid = False
        return is_valid