# Check Validate E-Mail Address in Python Using Regex 

import re 

email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"

user_email = input('Enter your Email :- ')

if re.search(email_condition,user_email) :
    print("Right Email")
else :
    print("Wrong Email")

