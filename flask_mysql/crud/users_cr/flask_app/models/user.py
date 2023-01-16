from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re	# the regex module
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class User:
    db_name='users_cr'
    def __init__( self , data ):
        self.id = data['id']
        self.firstname = data['firstname']
        self.lastname = data['lastname']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(cls.db_name).query_db(query)
        # Create an empty list to append our instances of friends
        users = []
        # Iterate over the db results and create instances of friends with cls.
        for user in results:
            users.append( user )
        return users

    @classmethod
    def getUserById(cls, data):
        query = "SELECT * FROM users WHERE users.id = %(user_id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return results[0]
    
    @classmethod
    def getUserByEmail(cls, data):
        query = "SELECT * FROM users WHERE users.email = %(email)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        if results:
            return results[0]
        return False
    
    @classmethod
    def createuser(cls,data):
        query = "INSERT INTO users (firstname, lastname, email) VALUES (%(firstname)s, %(lastname)s, %(email)s);"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        return connectToMySQL(cls.db_name).query_db(query,data)

    @classmethod
    def delete_user(cls,data):
        query = "DELETE FROM users WHERE users.id = %(user_id)s;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        return connectToMySQL(cls.db_name).query_db(query,data)

    @classmethod
    def updateUser(cls,data):
        query = "UPDATE users SET firstname = %(firstname)s, lastname= %(lastname)s, email = %(email)s WHERE users.id = %(user_id)s;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        return connectToMySQL(cls.db_name).query_db(query,data)

    @staticmethod
    def validate_user(user):
        is_valid = True
        if len(user['firstname']) <2:
            flash('First Name should be more than 2 characters', 'firstNameRegister')
            is_valid=False
        if len(user['lastname']) <2:
            flash('Last Name should be more than 2 characters', 'lastNameRegister')
            is_valid=False
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!", 'emailSignUp')
            is_valid = False
        return is_valid