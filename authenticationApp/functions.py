from django.test import TestCase
import re




#> This Function Take Handle of password matching and check password Length
def userCreationChecker(firstname , lastname ,email,password,password_conf):
    username_length = len(firstname) >= 3 and len(lastname) >= 3
    passwordLength = len(password) >= 8
    password_matching = (password == password_conf)
    if (username_length and email and passwordLength and password_matching):
        return True
    return False



#> This Function Check If The String paramater is a valid url
def check_url_pattern(input_string):
    url_pattern = r'^(https?:\/\/)?[a-zA-Z0-9_\-]+\.[a-zA-Z0-9_\-]+(\/[a-zA-Z0-9_\-]+)*\/?$'
    return re.match(url_pattern, input_string) is not None