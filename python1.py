#INPUTS
while True:
    user_name = input("Please enter your username: ")
    if user_name == "":
        print("Username cannot be empty. Please try again.")
        continue
    else:
        break
while True:
    password = input("Please enter your password: ")
    if password == "":
        print("password cannot be empty. Please try again.")
        continue
    else:
        break


#FILTER CHECK
score = 0

# 1. lenght of password > 8
if len(password) > 8:
    score = score + 1
else:
    print("Password is shorter than 8 characters.")

# 2. password contains at least one English letter
for m in password:
    if m.isalpha():
        score = score + 1
        break
else:
    print ("Password does not contain any English letters.")

# 3. password contains at least one special character
for i in password:
    if not i.isalnum():
        score = score + 1
        break
else:
    print ("Password does not contain any special characters.")

# 4. password contains at least one uppercase letter  
for ch in password:        
    if ch.isupper():       
        score = score + 1   
        break
else:
    print ("Password does not contain any uppercase letters")

# 5. password Not identical to the username
if password != user_name:
    score = score + 1
else:
    print ("Password is identical to the username.")

# 6. password Not the swapcase version of the username
if password != user_name.swapcase():
    score = score + 1
else:
    print ("Password is the swapcase version of the username.")

# 7. Password is not a special-character version of the username
spc_dic = {"a": "@", "s": "$", "i": "!", "o": "0"}
spc_index = []
for index, char in enumerate(user_name.lower()):
    if char in spc_dic:
        spc_index.append(index)
for i in spc_index:
    if i >= len(password):
        continue 
    if password[i] == spc_dic[user_name.lower()[i]]:
        print ("Password is a special-character version of the username")
        break 
else:
    score = score + 1

# 8. Not a common password
common_password = ["123456", "12345678", "12345", "111111", "123456789",
"qwerty", "asdfgh", "zxcvbnm", "password", "admin","P@s$w0rd"]
if password not in common_password:
    score = score + 1
else:
    print ("a common password.")
max_score = 8
print(f"password score: {score} out of {max_score}")
if score <= 2:
    print ("your password is very weak")
elif score <= 4:
    print ("your password is weak")
elif score <= 6:
    print ("your password is medium")
else:
    print ("your password is strong")