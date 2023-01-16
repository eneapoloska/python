from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
# create a regular expression object that we'll use later   
class Magazine:
    db_name='magaz'
    def __init__(self,data):
        self.id = data['id'],
        self.title = data['title'],
        self.description = data['description'],
        self.created_at = data['created_at'],
        self.updated_at = data['updated_at']
    
    @classmethod
    def getAllMagazines(cls):
        query= 'SELECT * FROM magazines;'
        results =  connectToMySQL(cls.db_name).query_db(query)
        magazines= []
        if results:
            for row in results:
                magazines.append(row)
            return magazines
        return magazines
        
    @classmethod
    def get_magazine_by_id(cls, data):
        query= 'SELECT * FROM magazines WHERE magazines.id = %(magazine_id)s;'
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return results[0]
        
    @classmethod
    def get_user_by_email(cls, data):
        query= 'SELECT * FROM users WHERE users.email = %(email)s;'
        results = connectToMySQL(cls.db_name).query_db(query, data)
        if len(results)<1:
            return False
        return results[0]
        

    #@classmethod
    #def get_all_user_info(cls, data):
    #    query= 'SELECT * FROM users LEFT JOIN posts on posts.user_id = users.id WHERE users.id = %(user_id)s;'
    #    results =  connectToMySQL(cls.db_name).query_db(query, data)
    #    posts = []
    #    if results:
    #        for row in results:
    #            posts.append(row)
    #        return posts
    #    return posts
        
    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM magazines WHERE id=%(magazine_id)s;'
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def update_magazine(cls,data):
        query = 'UPDATE magazines SET title=%(title)s, description=%(description)s, user_id = %(user_id)s WHERE magazines.id = %(magazine_id)s;'
        return connectToMySQL(cls.db_name).query_db(query, data)

    #Class Method to create a magazine
    @classmethod
    def create_magazine(cls,data):
        query = 'INSERT INTO magazines (title, description, users_id) VALUES ( %(title)s, %(description)s, %(user_id)s);'
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    #@classmethod
    #def get_logged_user_liked_posts(cls, data):
    #    query = 'SELECT post_id as id FROM likes LEFT JOIN users on likes.user_id = users.id WHERE user_id = %(user_id)s;'
    #    results = connectToMySQL(cls.db_name).query_db(query, data)
    #    postsLiked = []
    #    for row in results:
    #        postsLiked.append(row['id'])
    #    return postsLiked

    @staticmethod
    def validate_magazine(magazine):
        is_valid = True
        if len(magazine['title']) < 2:
            flash("Title must be at least 2 characters.", 'name')
            is_valid = False
        if len(magazine['description']) < 10:
            flash("Magaznie description be at least 10 characters.", 'description')
            is_valid = False
        return is_valid