from flask_app.config.mysqlconnection import connectToMySQL

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
    def createuser(cls,data):
        query = "INSERT INTO users (firstname, lastname, email) VALUES (%(firstname)s, %(lastname)s, %(email)s);"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        return connectToMySQL(cls.db_name).query_db(query,data)