from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
# create a regular expression object that we'll use later   

class Book:
    db_name='bookclub'
    def __init__(self,data):
        self.id = data['id'],
        self.title = data['title'],
        self.description = data['description'],
        self.created_at = data['created_at'],
        self.updated_at = data['updated_at']

