'''
Created on Mar 19, 2013

@author: macha
'''

_special_characters = ['@','#','$','%','^','&','*','!','~','`','[',']','{','}','|','\\','?','/',',','.','<','>']
_numbers = ['0','1','2','3','4','5','6','7','8','9']

class Validations(object):
    """
    validation class to validate user inputs
    """

    def check_valid_userName(self,name):
        """
method to check whether user has given a valid user name
@returns False if it contains a special character or lenth is zero or is None
@returns True, otherwise
"""
        validation = Validations()
        if validation.is_None(name):
            return False
        elif validation.is_length_zero(name):
            return False
        elif validation.contains_special_character(name):
            return False
        return True

    def check_valid_userId(self,name):
        """
method to check if use has provided a valid ID
@returns True, if userId starts with an alphabet and length >= 9
@returns False otherwise
"""
        validation = Validations()
        if validation.is_None(name):
            return False
        elif validation.is_length_zero(name) == True or len(name) > 9:
            print 'i am here'
            return False
        elif validation.starts_with_number(name):
            return False
        elif validation.starts_with_special_character(name):
            return False
        return True

    def contains_special_character(self,name):
        """
this method checks if the name contains a special character in it
@returns True, if it contains
@returns False otherwise
"""
        for char in _special_characters:
            if char in name:
                return True
        return False

    def starts_with_number(self,name):
        """
this method checks if the name starts with a number
@returns True, if it contains
@returns False otherwise
"""
        if name[0] in _numbers:
            return True
        return False

    def starts_with_special_character(self,name):
        """
this method checks if the name starts with a special character
@returns True, if it contains
@returns False otherwise
"""
        if name[0] in _special_characters:
            return True
        return False

    def is_length_zero(self,name):
        """
this method checks if the length of the name is zero
@returns True, if it is zero
@returns False otherwise
"""
        if len(name) == 0:
            return True
        return False

    def is_None(self,name):
        """
this method checks if the name is None
@returns True, if it is None
@returns False otherwise
"""
        if name == None:
            return True
        return False


validation = Validations()
#print validation.check_valid_userName("nawe")


# error = "no error"
# return True,error

#validation = Validations()
#result = validation.check_valid_username("name") or len(name) > 9
#print result[1]


"""
if validation.is_None(name):
print 'i am here'
return False
"""

