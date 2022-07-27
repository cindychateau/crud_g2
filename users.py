from mysqlconnection import connectToMySQL

class User:

    def __init__(self, data):
        #data = {id: 1, first_name: "Elena", last_name: "De Troya", email: "elena@cd.com", created_at: "0000-00-00", updated_at: "0000-00-00"}
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def guardar(cls, formulario):
        #formulario = {first_name: "Elena", last_name: "De Troya", email: "elena@cd.com"}
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s)"
        #INSERT INTO users (first_name, last_name, email) VALUES ('Elena', 'De Troya', 'elena@cd.com')
        result = connectToMySQL('crud_g2').query_db(query, formulario)
        return result

    @classmethod
    def muestra_usuarios(cls):
        query = "SELECT * FROM users"
        results = connectToMySQL('crud_g2').query_db(query)
        #results = [
        #    {id: "1", first_name:"Elena", last_name:"De Troya", email:"e@cd.com", created_at:"0000-00-00", updated_at:"0000-00-00"},
        #    {id: "1", first_name:"Elena", last_name:"De Troya", email:"e@cd.com", created_at:"0000-00-00", updated_at:"0000-00-00"}
        #]
        users = []
        for u in results:
            instancia_usuario = cls(u) #User({id: "1", first_name:"Elena", last_name:"De Troya", email:"e@cd.com", created_at:"0000-00-00", updated_at:"0000-00-00"})
            users.append(instancia_usuario)
        return users
    
    @classmethod
    def borrar(cls, formulario):
        #formulario = {id: "1"}
        query = "DELETE FROM users WHERE id = %(id)s"
        #DELETE FROM users WHERE id = 1
        result = connectToMySQL('crud_g2').query_db(query, formulario)
        return result
