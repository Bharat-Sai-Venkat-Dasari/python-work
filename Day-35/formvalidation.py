#============================Validation of User name====================================

# import re
# fullname = input("Enter your full name: ")
# pattern = r'^[A-Za-z]{2,25}( [A-Za-z]{2,25})+$'
# res = re.fullmatch(pattern, fullname)
# print("Valid Fullname" if res else "Invalid Fullname")



# import re
# fullname = input("Enter your full name: ")
# pattern = r'^[A-Za-z]{2,25}( [A-Za-z]{2,25})*$'
# res = re.fullmatch(pattern, fullname)
# print("Valid Fullname" if res else "Invalid Fullname")



#============================Validation of Email====================================

# import re
# pattern = r'^[a-zA-Z._0-9]+@[a-zA-Z._0-9]+\.[a-zA-Z]{2,}$'
# email = input("Enter your email: ")
# res = re.fullmatch(pattern, email)
# print("Valid Email" if res else "Invalid Email")

#============================Validation of Phone number====================================

# import re
# pattern = r'^(?:\+91|0)?[6-9]\d{9}$'
# phone_number = input("Enter your phone number: ")
# res = re.fullmatch(pattern, phone_number)
# print("Valid Phone number" if res else "Invalid Phone number")


#============================Validation of Password====================================

# import re
# pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[@$!%?&])[A-Za-z0-9@$!%?&]{8,}$'
# password = input("Enter your password: ")
# res = re.fullmatch(pattern, password)
# print("Valid password" if res else "Invalid password")


#============================Validation of Username====================================


# import re
# pattern = r'^[A-Za-z0-9._]{5,15}$'
# username = input("Enter your username: ")
# res = re.fullmatch(pattern, username)
# print("Valid username" if res else "Invalid username")

#============================Validation of Username====================================

# import re
# pattern = r'^([0-9]{4})( ([0-9]{4}))( ([0-9]{4}))$'
# aadhar = input("Enter your Aadhar: ")
# res = re.fullmatch(pattern, aadhar)
# print("Valid Aadhar" if res else "Invalid Aadhar")


#============================Validation of Pancard====================================

#SSQPS5723E
import re
pattern = r'^([A-Z]{5})([0-9]{4})([A-Z]{1})$'
pancard = input("Enter your pancard: ")
res = re.fullmatch(pattern, pancard)
print("Valid Pancard number" if res else "Invalid Pancard number")
