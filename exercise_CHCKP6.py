class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


new_user = User('Rosa', '1234abc')

print(new_user.username)
print(new_user.password)