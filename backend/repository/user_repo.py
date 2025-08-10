class UserRepository:
    def __init__(self, db):
        self.db = db

    def get_by_email(self, email):
        cursor = self.db.cursor()
        cursor.execute("""
            SELECT id, email, password_hash, name, nickname, created_at
            FROM users WHERE email = %s
        """, (email,))
        user_data = cursor.fetchone()
        cursor.close()
        return user_data

    def get_by_id(self, user_id):
        cursor = self.db.cursor()
        cursor.execute("""
            SELECT id, email, name, nickname, created_at
            FROM users WHERE id = %s
        """, (user_id,))
        user_data = cursor.fetchone()
        cursor.close()
        return user_data

    def create(self, email, password_hash, name, nickname):
        cursor = self.db.cursor()
        cursor.execute("""
            INSERT INTO users (email, password_hash, name, nickname, created_at)
            VALUES (%s, %s, %s, %s, NOW())
        """, (email, password_hash, name, nickname))
        user_id = cursor.lastrowid
        self.db.commit()
        cursor.close()
        return user_id 