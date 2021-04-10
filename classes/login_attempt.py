# Saturday April 3rd

# next is inheritance
# pg 171  exercise 9-5 Login Attempt



# do exercise  pg 171
# Homework exercises: 9-4

#to check int
#if isinstance(n, int):
#        return True


class User:
    """docstring: this will count login attempts """

    login_attempts = 0  # declared global variable

    """first is the init method"""
    def __init__(self):
        pass    # means do nothing, it just a place holder
        # self.login_attempts = 0 can do like that too

    def increment_login_attempts(self):
        print("incrementing value by 1")
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User() # we don't have nothing to pass

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print("Login attempts: ", user1.login_attempts)
user1.reset_login_attempts()
print("Login attempts: ", user1.login_attempts)
