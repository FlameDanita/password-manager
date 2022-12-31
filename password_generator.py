import random

def get_simple_password():
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "-"

    main_use_for = lower_case + upper_case + numbers
    supp_use_for = symbols
    lenght_for_pass = 4
    password = ""
    for i in range(4):
        if i != 0:
            password += "".join(random.sample(supp_use_for, 1))
        password += "".join(random.sample(main_use_for, lenght_for_pass))
        
    return password

def get_strong_password():
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*()_-+="

    main_use_for = lower_case + upper_case + numbers
    supp_use_for = symbols
    lenght_for_pass = 4
    password = ""
    for i in range(4):
        if i != 0:
            password += "".join(random.sample(supp_use_for, 1))
        password += "".join(random.sample(main_use_for, lenght_for_pass))
        
    return password