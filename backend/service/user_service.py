import bcrypt
from repository.user_repo import UserRepository

class UserExistsException(Exception): pass
class InvalidCredentialsException(Exception): pass

class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def register(self, email, password, name, nickname):
        if self.user_repo.get_by_email(email):
            raise UserExistsException('이미 존재하는 이메일입니다')
        hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        user_id = self.user_repo.create(email, hashed_pw, name, nickname)
        user = self.user_repo.get_by_id(user_id)
        return user

    def login(self, email, password):
        user = self.user_repo.get_by_email(email)
        if not user or not bcrypt.checkpw(password.encode('utf-8'), user['password_hash'].encode('utf-8')):
            raise InvalidCredentialsException('잘못된 이메일 또는 비밀번호입니다')
        return user 