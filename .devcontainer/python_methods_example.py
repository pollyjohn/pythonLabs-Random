## if you want to run this code, comment lines 52 and 53. they generate an
# I that I am demostrating on purpose. See the the comment near them.


class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user= None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection
    
    @staticmethod
    def log(msg):
        print("LOG", msg)

    @staticmethod
    def log_s(self, msg):
        print(f"LOG: {self.user}", msg)

## See that a class method requires less steps and
#consists of a simpler way to crete an instance/obj;

c1 = Connection.create_with_auth('gab','5432')
print(c1.user)
print(c1.password)
# we have access   obj created with class methods (fabric).
c1.log(": you're logged in")

c2 = Connection()
c2.set_user("fab")
c2.set_password(87654)
print(c2.user)
print(c2.password)
## see that we have acces to the instances with the static method.
# as we have to obj created with class methods (fabric).
c2.log(": you're logged in")

## but we don't have access to self atributes and methods
# or class atributes and methods. See that the "self" argument in "log_s"
# is being interpreted as a "any" type argument, not as the instance:
c2.log_s("you're logged in")  
c1.log_s("s","you're logged in")

## this is why could be better to create a simple global function