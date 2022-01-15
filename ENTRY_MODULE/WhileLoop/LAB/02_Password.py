class UserClass:
    username: str
    password: str
    authenticated: bool = False

    def __init__(self, user_in: str, pass_in: str) -> None:
        self.username = user_in.strip()
        self.password = pass_in.strip()

    def authenticate(self, pass_in: str) -> None:
        self.authenticated = self.password == pass_in.strip()

    def is_authenticated(self) -> bool:
        return self.authenticated

if __name__ == '__main__':
    current_user = UserClass(input(), input())

    while not current_user.is_authenticated():
        current_user.authenticate(input())

    print(f'Welcome {current_user.username}!')
