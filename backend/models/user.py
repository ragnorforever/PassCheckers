import pymysql
import bcrypt
from datetime import datetime
from config import Config

class User:
    def __init__(self, db_connection):
        self.db = db_connection
    
    def create_user(self, email, password, name, nickname):
        try:
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            cursor = self.db.cursor()
            cursor.execute("""
                INSERT INTO users (email, password_hash, name, nickname, created_at)
                VALUES (%s, %s, %s, %s, %s)
            """, (email, hashed_password.decode('utf-8'), name, nickname, datetime.now()))
            user_id = cursor.lastrowid
            self.db.commit()
            cursor.close()
            return {
                'id': user_id,
                'email': email,
                'name': name,
                'nickname': nickname,
                'created_at': datetime.now()
            }
        except Exception as e:
            self.db.rollback()
            raise e
    
    def get_user_by_email(self, email):
        try:
            cursor = self.db.cursor()
            cursor.execute("""
                SELECT id, email, password_hash, name, nickname, created_at
                FROM users WHERE email = %s
            """, (email,))
            user_data = cursor.fetchone()
            cursor.close()
            if user_data:
                return {
                    'id': user_data['id'],
                    'email': user_data['email'],
                    'password_hash': user_data['password_hash'],
                    'name': user_data['name'],
                    'nickname': user_data['nickname'],
                    'created_at': user_data['created_at']
                }
            return None
        except Exception as e:
            raise e
    
    def get_user_by_id(self, user_id):
        try:
            cursor = self.db.cursor()
            cursor.execute("""
                SELECT id, email, name, nickname, created_at
                FROM users WHERE id = %s
            """, (user_id,))
            user_data = cursor.fetchone()
            cursor.close()
            if user_data:
                return {
                    'id': user_data['id'],
                    'email': user_data['email'],
                    'name': user_data['name'],
                    'nickname': user_data['nickname'],
                    'created_at': user_data['created_at']
                }
            return None
        except Exception as e:
            raise e
    
    def verify_password(self, email, password):
        user = self.get_user_by_email(email)
        if user and bcrypt.checkpw(password.encode('utf-8'), user['password_hash'].encode('utf-8')):
            return user
        return None 