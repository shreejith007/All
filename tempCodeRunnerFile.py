import random
otp =random.randint(10000,100000)
print(str(otp))
user =input ("Enter the OTP:-")
print(str(user))
if otp != user:
    print("Access Denied ")