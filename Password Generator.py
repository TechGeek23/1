import random 
import string

password = ''.join(random.choice(string.acii_letters + string.digits) for i in range(10))
print(password)