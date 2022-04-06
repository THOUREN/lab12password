import random
from random import randint
import string


def generate_num_random(length):
    digits = string.digits
    rand_string = ''.join(random.sample(digits, length))
    print("Пароль сгенерирован:", rand_string)


def generate_random_alpha(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    print("Пароль сгенерирован:", rand_string)


def generate_random_string(length):
    letters = '!@#$%^&*()<>+=_'
    rand_string = ''.join(random.choice(letters) for i in range(length))
    print("Пароль сгенерирован:", rand_string)


def generate_alphanum_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    rand_string = ''.join(random.sample(letters_and_digits, length))
    print("Пароль сгенерирован:", rand_string)


def generate_alphaspec_random_string(length):
    letters_and_digits = string.ascii_letters + '!@#$%^&*()<>+=_'
    rand_string = ''.join(random.sample(letters_and_digits, length))
    print("Пароль сгенерирован:", rand_string)


def generate_specnum_random_string(length):
    letters_and_digits = string.digits + '!@#$%^&*()<>+=_'
    rand_string = ''.join(random.sample(letters_and_digits, length))
    print("Пароль сгенерирован:", rand_string)



print('Генератор пароля: ')
print('Укажите длину пароля:')
le = input()
a = 1

while a==1:
    print('1. Сгенерировать пароль из цифр')
    print('2. Сгенерировать пароль из букв')
    print('3. Сгенерировать пароль из спец символов')
    print('4. Сгенерировать пароль из букв и цифр')
    print('5. Сгенерировать пароль из букв и спец символов')
    print('6. Сгенерировать пароль из цифр и спец символов')
    print('0. Выход')
    print
    gen = input()
    if int(gen) == 1:
    	generate_num_random(int(le))
    if int(gen) == 2:
    	generate_random_alpha(int(le))
    if int(gen) == 3:
    	generate_random_string(int(le))
    if int(gen) == 4:
    	generate_alphanum_random_string(int(le))
    if int(gen) == 5:
    	generate_alphaspec_random_string(int(le))
    if int(gen) == 6:
    	generate_specnum_random_string(int(le))
    if int(gen) == 0:
    	a = 2

    
