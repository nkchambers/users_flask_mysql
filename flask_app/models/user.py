from flask_app.config.mysqlconnection import connectToMySQL


# model the class after the users table from our database
class User:
    def __init__( self, data ):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]



    # READ ALL
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL("users_db").query_db(query)
        
        print("This is data inside of results from running get all query", results)
        
        users = []
        
        # Iterate over the db results and create instances of users with cls.
        for row in results:
            users.append( cls(row) )
        
        return users

    # CREATE
    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW());"
        results = connectToMySQL("users_db").query_db(query, data)
        
        print("This is the data inside of the results after we insert into database", results)

        return results


    #READ ONE
    @classmethod
    def get_one(cls, data):
        query="SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL("users_db").query_db(query, data)

        if len(results) == 0:
            return False

        return User (results[0])


    #UPDATE
    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, updated_at = NOW() WHERE id = %(id)s;"
        results = connectToMySQL("users_db").query_db(query, data)

        return results
    
    #DELTE
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        results = connectToMySQL("users_db").query_db(query, data)




