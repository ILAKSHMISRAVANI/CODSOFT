# Password Generator by user with desired length as random using python
import string
import random # define the random module.
def Random_Password_Generator(len):   # Create a function for password generation 
 pwd= ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k = len))  # Random concatination of alphabets,digits and special symbol
 return pwd
print('-----------------------------------------\nPassword Generator\nBased on length given by user\n-------------------------------------- ')
len=int(input('Enter desired length of password based on complexity :\n'))
password=Random_Password_Generator(len) # Call function for password generation
print("Randomly Generated Password is : " + str(password))    # print the random password
print('Generated Password Successfully!')
print('---------------------------------------------')