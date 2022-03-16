from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.user import User
db = 'recipes_schema'

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.time = data['time']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        # insert other required fields as shown in schema
    

    # create method
    @classmethod
    def create(cls, data):
        # some query
        query = "INSERT INTO recipes (name, description, time, instructions, date_made, created_at, updated_at, user_id) VALUES ( %(name)s, %(description)s, %(time)s, %(instructions)s, %(date_made)s, NOW(), NOW(), %(user_id)s );"
        return connectToMySQL(db).query_db(query, data)
    
    # read
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL(db).query_db(query)
        all_list = []
        for row in results:
            all_list.append( cls(row) )
        return all_list
    
    @classmethod
    def get_from_id(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        results = connectToMySQL(db).query_db(query, data)
        print(results[0])
        if len(results) < 1:
            return False
        return cls(results[0])
    
    @classmethod
    def get_from_user_id(cls, data):
        query = "SELECT * FROM recipes WHERE user_id = %(user_id)s;"
        results = connectToMySQL(db).query_db(query, data)
        all_recipes = []
        for row in results:
            all_recipes.append(cls(row))
        return all_recipes

    # update
    @classmethod
    def update(cls, data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, time = %(time)s, instructions = %(instructions)s, date_made = %(date_made)s, user_id = %(user_id)s WHERE id = %(id)s;"
        return connectToMySQL(db).query_db(query, data)
    
    # delete
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(db).query_db(query, data)
    