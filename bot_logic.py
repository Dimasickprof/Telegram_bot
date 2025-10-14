import random

def gen_pass(pass_length):
    elements = "+-*!&$?=@<>123456789abcdefghijklmnopqrstuvwxyz"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password
    