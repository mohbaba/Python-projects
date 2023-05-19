import random

spec_char = ['~','!','@','#','$','%','^','&','*']
num = list('1234567890')
low_alpha =list ('qwertyuioplkjhgfdsazxcvbnm')
upper_alpha =list ('QWERTYUIOPLKJHGFDSAZXCVBNM')
gen_char = spec_char + num + low_alpha + upper_alpha
def generate(length = 8):
    
    
    password = ''
    
    # Ensure at least one number
    password += random.choice(num)
    
    # Ensure at least one special character
    password += random.choice(spec_char)
    
    for i in range(length-2):
        password += random.choice(gen_char) 
    
    # Shuffle the characters to make the password more random
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)
    return password

def main():
    while True:
        try:
            pass_len = int(input("Enter the length of the password(s): "))
            break
        except ValueError:
            print("Please enter a valid integer.")
            
    generate(pass_len)


