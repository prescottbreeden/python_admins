from app.database import connectToMySQL


class UserAPI:
    def get_all(self):
        mysql = connectToMySQL('flask_users')
        query = '''
            SELECT u.user_id,
                CONCAT(u.first_name, ' ', u.last_name) AS full_name,
                u.email,
                u.status
            FROM users AS u;
        '''
        all_users = mysql.query_db(query)
        return all_users

    def delete_one(self, id):
        mysql = connectToMySQL('flask_users')
        query = "DELETE FROM users WHERE user_id={}".format(id)
        mysql.query_db(query)
        return 1
