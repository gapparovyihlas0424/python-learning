hello = 'Hello'
world = 'World'

greet = hello + world

greeting = hello + ' ' + world

gr = f"{hello} {world}"

print(greet)  # output= HelloWorld
print(greeting)  # Output = Hello World
print(gr)  # = Hello World

name = 'Ыхлас'
time = '20:00'
habit = 'reading'

res = f"{name} likes {habit} Atomic Habits everyday starting from {str(time)} o\'clock "
print(res)


def greeting(greet):
    return lambda name: f"{greet},{name}"


morning_greet = greeting('Good morning')

# Output = <function greeting.<locals>.<lambda> at 0x000001F853593480>
print(morning_greet)
print(morning_greet('Yhlas'))

# white_button = {
#     'signal': 'up',
#     'color': 'white',
# }

# black_button = {

#     **white_button,
#     'signal': 'down',
#     'color': 'black',
# }

# print(black_button)
# print(white_button)


# a_list = [1, 5, 6]
# sec = ['a', 'g', 'k']

# print(a_list or sec)  # Output: [1, 5, 6,]
# print(len(a_list) > 0 or sec)  # Output: True
# print(len(a_list) < 0 or sec)  # Output: ['a', 'g', 'k']

# numbers = [1, 2, 3, 4, 5]
# dictionary = {}
# # Output: {} when numbers is True and dictionary is False so it returns the last False value
# print(numbers and dictionary)

# list = [1, 2, 3, 4, 5]
# list and print("its not empty")  # Output: its not empty

# dict1 = {'name': 'Alice', 'age': 30}
# dict2 = {'name': 'Alice', 'age': 30}

# if dict1 == dict2:
#     print('they are equal')


# print(bool([4, 5])) # Output: True
# print(bool([])) # Output: False

# just = [4, 5, 6]
# if len(just) > 0:
#     print('List is not empty')


# just = [4, 5, 6]
# if just:
#     print('List is not empty')  # Output: List is not empty


# uni = {'Standford', 'Harvard', 'MIT', 'Yale'}
# physics = {'Quantum Mechanics', 'Thermodynamics', 'Electromagnetism', 'Optics'}
# print(uni.__eq__(physics))  # Output: False
# print(uni is physics)  # Output: False


# my_car = {
#     'make': 'Toyota',
#     'mark': 'Camry',
#     'color': 'blue'
# }

# print('year' in my_car)
# print('year'not in my_car)


# numb = 5
# print(+ numb)

# bool = False
# print(+ bool)  # Output: 0

# Логика not в Python очень простая: not переворачивает логическое значение на противоположное.
# В Python числа тоже можно воспринимать как True или False:

# * 0 → False
# * любое число, кроме 0 → True

# ten = 10
# print(not ten)  # Output: False

# one = 0
# print(not one)  # Output: True


# a = 9
# b = a
# print(a is b) # Output: True
# a = [4, 5, 6]
# b = [4, 5, 6]
# print(a is b) # Output: False
# print(a == b) # Output: True
# # (a.__eq__(b)) # Output: True


# a = 15


# def number():
#     a = 45
#     b = 75
#     print(a)
#     print(b)


# number()
# print(a)

# b = 78
# c = 66


# def my_func():
#     global b
#     b = 90
#     print(c)
#     print(b)


# my_func()
# print(b)

# def print_number_inf(num):
#     if (num % 2) == 0:
#         print('Entered number is even')
#     else:
#         print('Entered number is odd')


# def process(num, callback):
#     callback(num)


# enter_num = int(input('Enter a number: '))
# process(enter_num, print_number_inf)


# from datetime import date


# def get_weekday():
#     return date.today().strftime("%A")


# def create_new_post(post, weekday=get_weekday()):
#     post_copy = post.copy()
#     post_copy['created_on_weekday'] = weekday
#     return post_copy


# initial_post = {
#     'title': 'My First Post',
#     'content': 'This is the content of my first post.',
#     'author': 'John Doe'
# }

# print(create_new_post(initial_post))
# # Output: {'title': 'My First Post', 'content': 'This is the content of my first post.', 'author': 'John Doe', 'created_on_weekday': 'Monday'}
# print(initial_post)


# def upd_car_info(**car):
#     car['color'] = 'red'
#     return car


# res = upd_car_info(mark='toyota', model='camry', year=2020)
# print(res)
# print(res['color'])

# def argu(*args):
#     print(args)
#     print(args[1])
#     return sum(args)


# print(argu(1, 5, 8, 6, 7))


# def merge(first, second):
#     new_dct = zip(first, second)
#     return dict(new_dct)


# res = merge(['a', 'b', 'c'], [1, 2, 3])
# print(res)  # Output: {'a': 1, 'b': 2, 'c': 3}


# def sum(a, b):
#     c = a + b
#     print(c)


# sum(6, 5)
# sum(10, 20)

# def my_fn(a, b):
#     a = a + 5
#     c = a + b
#     return c


# first = 10
# sec = 5
# res = my_fn(first, sec)
# print(res)


# def inc_age(person):
#     person['age'] += 1
#     return person


# an_age = {'name': 'Alice', 'age': 30}
# inc_age(an_age)
# print(an_age['age'])  # Output: 31

# from copy import deepcopy
# snacks = {
#     'chips': 'Lays',
#     'consumer': 'students',
#     'city': []
# }
# sacks_copy = deepcopy(snacks)
# sacks_copy['city'].append('Los Angeles')
# print(snacks)  # Output: {'chips': 'Lays', 'consumer': 'students', 'city': []}
# # Output: {'chips': 'Lays', 'consumer': 'students', 'city': ['Los Angeles']}
# print(sacks_copy)


# drinks = {
#     'water': 'Dizzy',
#     'consumer': 'students',
#     'city': []
# }
# drinks_copy = drinks.copy()
# drinks_copy['city'].append('New York')
# # Output: {'water': 'Dizzy', 'consumer': 'students', 'city': ['New York']}
# print(drinks)
# # Output: {'water': 'Dizzy', 'consumer': 'students', 'city': ['New York']}
# print(drinks_copy)


# drinks['water'] = 'Coca-Cola'
# # Output: {'water': 'Coca-Cola', 'consumer': 'students', 'city': ['New York']}
# print(drinks)
# # Output: {'water': 'Coca-Cola', 'consumer': 'students', 'city': ['New York']}
# print(drinks_copy)
# print(drinks_copy['city'])  # Output: ['New York']

# zip() берёт элементы с одинаковыми индексами из двух списков и соединяет их в пары — кортежи.
# languages = ['Python', 'Java', 'C++', 'JavaScript']
# numeration = [1, 2, 3, 4,]
# lan_num = zip(languages, numeration)
# print(list(lan_num)) # output: [('Python', 1), ('Java', 2), ('C++', 3), ('JavaScript', 4)]
# dict_lan_num = dict(lan_num)
# output: {'Python': 1, 'Java': 2, 'C++': 3, 'JavaScript': 4}
# print(dict_lan_num)
# new_dict = dict(zip(languages, numeration))
# print(new_dict)
# print(new_dict['Python'])


# a = {'ads', 's', 'g', 'k', 'j'}
# b = {'ads', 's', 'g', 'k', 'm'}
# # print(a | b)
# new_set = a.intersection(b)
# print(new_set)
# print((a | b)-(b & a))
# print((a.symmetric_difference(b)))


# first_set = {'bbc', 'a', 'r', 't'}
# second_set = {'s', 'g', 'k', 'j'}
# print(first_set.intersection("bbca"))  # result = {'a'}
# print(first_set.intersection(['bbc', 'a']))  # result = {'bbc', 'a'}
# set_test = {1, 2, 9, 9, 3, 4, 5}
# set_test.add(6)
# set_test.remove(3)
# This will raise an error because sets do not support indexing
# print(set_test[0])
# print(set_test.__getitem__(0))
# print(set_test)  # Output: {1, 2, 4, 5, 6}

# photo_sizes = {'480x720', '880x720', '1920x1080'}
# second_size = {'480x720', '770x880', '650x123'}
# # Output: {'480x720', '880x720', '1920x1080', '770x880', '650x123'}
# print(photo_sizes.union(second_size))
# print(photo_sizes.intersection(second_size))  # Output: {'480x720'}


# my_nums = (1, 5, 5, 9, 7, 5)
# index_test = my_nums.index(5)
# index_two = my_nums.index(5, index_test + 1)
# index_three = my_nums.index(5, index_two + 1)
# print(index_three)
# del my_nums [0]  # This will raise an error because tuples are immutable
# my_nums.append(10)  # This will raise an error because tuples are immutable
# print(my_nums)  # Output: (1, 5, 5, 9, 7, 5)

# user = ({
#     "user_id": 125,
#     "user_name": "Yhlas"
# },
#     {
#     "user_id": 456,
#     "user_name": "Maks"
# })
# print(user[0]['user_name'])  # Output: Yhlas
# print(user[1]['user_name'])  # Output: Maks
# user[0]['user_id'] = 45  # change
# print(user[0]['user_id'])  # Output: 45


# new_dict = {}
# key = input('Enter a key: ')
# value = input('Enter a value: ')
# new_dict[key] = value
# key2 = input('Enter a second key: ')
# value2 = input('Enter a second value: ')
# new_dict[key2] = value2
# print(new_dict)

# only_list = [True, 0, 'apple']
# # my_dict = dict(only_list)  # it is not possible
# second_list = [('name', 'Alice'), ('age', 30), ('city', 'New York')]
# s_dict = dict(second_list)
# print(s_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}
# s_dict.pop('city')
# print(s_dict)  # Output: {'name': 'Alice', 'age': 30}

# test_tuple = ('name', 'Alice')
# # test_tuple[0] = 'Me'  # This will raise an error because tuples are immutable
# print(type(test_tuple))  # Output: <class 'tuple'>

# my_disk = {
#     'name': 'Story',
#     'size': 1000,
#     'unit': 'gb'
# }
# new_disk = my_disk.copy()
# new_disk['size'] = 2000
# print(my_disk)
# print(new_disk)

# mac_price = {
#     'name': 'mac neo',
#     'price': 600,
#     'mac_info': {
#         'creator': 'steve jobs',
#         'year': 2000
#     }
# }
# mac_price['price'] = 700
# mac_price['color'] = 'silver'  # adds new key-value pair to the dictionary
# print(mac_price['mac_info']['creator'])  # Output: steve jobs
# print(mac_price.get('CPU'))

# a_list = ['apple', 'banana', 'cherry']
# del a_list[1]
# print(a_list)  # Output: ['apple', 'cherry']
# a_list.append('orange')
# print(a_list)  # Output: ['apple', 'cherry', 'orange']
# a_list.pop(0)
# print(a_list)
# a_list.extend('yhlas')
# print(a_list)


# bool_h = True
# number_k = 5
# print(number_k + bool_h)

# a_word = "hello"
# a_number = 5
# a_numberstring = '7'
# a_word2 = '15'
# a_floatnum = 1.5
# print(a_number + a_floatnum)  # result = 6.5
# print(a_floatnum + a_number)  # result = 6.5
# print(a_number.__add__(a_floatnum))  # result = notimplemented
# print(a_floatnum.__radd__(a_number))  # result = 6.5
# print(a_numberstring.__rmul__(a_number))  # multiplies '7' 5 times = 77777
# print(a_word2.__rmul__(a_number))  # multiplies '15' 5 times = 1515151515

# phyton does not operate this cus it does not know with which number
# print(a_number + int(a_word))

# print(a_word + str(a_number))# result = hello5
# print(a_numberstring + str(a_number))
# it equals 75 because it (a_number) is a string and not a number


# a_word = "Hello, World!"
# print(a_word[5])

# print(45 > 3)
# print('Apple' > 'iphone')

# identity = {'name': 'Alice', 'age': 30}
# print(identity['name'])


# avarage_price = 25.5
# price = int(avarage_price)
# print(price)

# approx_price = 12.6
# print(round(approx_price))


# степень
# base = 2
# power = 4
# print(pow(base, power))

# Превращение строки в число то есть 'str to int'

# input_string = input("Enter a string: ")
# print(input_string)
# input_int = int(input_string)
# print(type(input_int))

# Поменять слова местами
# a_comment = "This is a comment that explains the purpose of the code."
# print(a_comment.replace("comment", "remark"))


# def sum_nums(a, b):
#     sum = a + b
#     return sum


# result = sum_nums(5, 10)
# result2 = sum_nums(20, 30)
# print(result)
# print(result2)
# print(sum_nums(5, 10))


# import random
# friends = ('Alice', 'Bob', 'Charlie', 'David', 'Eve')
# who_pays = random.choice(friends)
# print(who_pays)
# print(id(who_pays))
