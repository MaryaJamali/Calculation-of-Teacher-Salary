# It is used for security purposes
import secrets


class Character:
    # Use "secrets.token_urlsafe()" to generate security tokens.
    def __init__(self, first_name, last_name, id=secrets.token_urlsafe(16), **kwargs):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

        for key, value in kwargs.items():
            setattr(self, key, value)


# Inherit from character class
class Teacher(Character):
    hour = 0
    pay_per_one_hour = 0

    def __init__(self, first_name, last_name):
        # "super()" gives us access to a higher class
        super().__init__(first_name, last_name)

    def get_hour(self):
        return self.hour

    def set_hour(self, value):
        self.hour = value

    def get_pay_per_one_hour(self):
        return self.pay_per_one_hour

    def set_pay_per_one_hour(self, value):
        # Prevent negative numbers from entering the system
        if value > 0:
            self.pay_per_one_hour = value
        else:
            self.pay_per_one_hour = 0

    def payment(self):
        return self.hour * self.pay_per_one_hour

# The examples in this section call the __str__() and __repr__() methods directly for demonstration purposes.
# In general, the __str__() method is intended for users and the __repr__() method is intended for developers.
    # This function is executed when the object is converted to string or when we want to print the object
    def __str__(self):
        return "{}, {}, {}, {}, {}".format(self.id, self.first_name, self.last_name, self.hour, self.pay_per_one_hour)

    # The __repr__() method returns a more information string representation of an object.
    def __repr__(self):
        return "mr/miss.{} object".format(self.last_name)


# Object definition
teacher = Teacher('Maryam', 'Jamali')
print(teacher)
teacher.set_pay_per_one_hour(1000000)
teacher.set_hour(50)
print(teacher.payment())
