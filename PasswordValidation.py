import re
password=input("Enter your Password   : ")
x = True
while x:
    if not re.search("[a-z]",password):
        break
    elif not re.search("[0-9]",password):
        break
    elif not re.search("[A-Z]",password):
        break    
    elif (len(password)<6 or len(password)>16):
        break
    elif not re.search("[$#@]",password):
        break
    elif re.search("\s",password):
        break
    else:
        print("Valid Password")
        x=False
        break

if x:
    print("Your Password is Invalid")
    print("Your password should contain :\nAt least 1 letter between [a-z] and [A-Z].")
    print("At least 1 number between [0-9].")
    print("At least 1 character between [$#@].")
    print("Maximum length 16 character .")
    
   
