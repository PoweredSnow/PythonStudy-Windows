class AnonymousSurvey:
    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        print(self.question)

    def store_response(self, new_response):
        self.responses.append(new_response)

    def show_results(self):
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")


# def get_formatted_name(first, last, middle=''):
#     if middle:
#         full_name = f"{first} {middle} {last}"
#     else:
#         full_name = f"{first} {last}"
#     return full_name.title()

# 文件和异常

# import json
# def get_stored_username():
#     filename = 'username.json'
#     try:
#         with open(filename) as f:
#             username = json.load(f)
#     except FileNotFoundError:
#         return None
#     else:
#         return username

# def get_new_username():
#     username = input("What's your name: ")
#     filename = 'username.json'
#     with open(filename, 'w') as f:
#         json.dump(username, f)
#     return username

# def greet_user():
#     username = get_stored_username()
#     running = True
#     while running:
#         answer = input(f"Is '{username}' your name?(y/n) ")
#         if answer == 'y':
#             print(f"Welcome back, {username}!")
#             running = False
#         elif answer == 'n':
#             username = get_new_username()
#             print(f"We'll remember you when you come back, {username}!")
#             running = False
#         else:
#             print("your answer is illegal.")

# greet_user()

# def count_words(filename):
#     try:
#         with open(filename, encoding='utf-8') as f:
#             contents = f.read()
#     except FileNotFoundError:
#         pass
#         # print(f"Sorry, the file {filename} does not exist.")
#     else:
#         words = contents.split()
#         num_words = len(words)
#         print(f"The file {filename} has about {num_words} words.")

# filenames = ['alice.txt', 'siddhartha.txt',
#              'moby_dick.txt', 'little_women.txt']
# for filename in filenames:
#     count_words(filename)

# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero!")

# filename = 'programming.txt'
# with open(filename, 'a') as file_object:
#     file_object.write("I also love finding meaning in large datasets.\n")
#     file_object.write("I love creating apps that can run in a browser.\n")

# filename = 'pi_million_digits.txt'
# with open(filename) as file_object:
#     lines = file_object.readlines()
#     # for line in file_object:
#     #     print(line.rstrip())
#     # contents = file_object.read()
# pi_string = ''
# for line in lines:
#     pi_string += line.strip()

# birthday = input("yymmdd: ")
# if birthday in pi_string:
#     print("your birthday appears in the first million digits of pi!")
# else:
#     print("your birthday does not appear in the first million digits pf pi.")

# 集合

# languages = {'python', 'ruby', 'python', 'c'}
# print(languages)

# 字典

# users = {
#     'aeinstein': {
#         'first': 'albert',
#         'last': 'einstein',
#         'location': 'princeton',
#     },
#     'mucurie': {
#         'first': 'marie',
#         'last': 'curie',
#         'location': 'paris',
#     },
# }
# for username, user_info in users.items():
#     print(f"\nUsername: {username}")
#     full_name = f"{user_info['first']} {user_info['last']}"
#     location = user_info['location']
#     print(f"\tFull name:{full_name.title()}")
#     print(f"\tlocation:{location.title()}")

# pizza = {
#     'crust': 'thick',
#     'toppings': ['mushrooms', 'extrs cheese']
# }
# print(f"You ordered a {pizza['crust']}-crust pizza "
#       "with the following topings:")
# for topping in pizza['toppings']:
#     print("\t" + topping)

# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}
# aliens = [alien_0, alien_1, alien_2]
# for alien in aliens:
#     print(alien)

# user_0 = {
#     'username': 'efermi',
#     'first': 'enrico',
#     'last': 'fermi',
# }
# for key, value in user_0.items():
#     print(f"\nKey: {key}")
#     print(f"Value: {value}")

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }
# language = favorite_languages['sarah'].title()
# print(f"Sarah's favorite language is {language}.")
# for name, language in favorite_languages.items():
#     print(f"{name.title()}'s favorite language is {language.title()}.")
# for name in favorite_languages.keys():
#     print(name.title())
# for name in sorted(favorite_languages.keys()):
#     print(f"{name.title()}, thank you for taking the poll.")
# print("The following languages have been mentioned:")
# for language in set(favorite_languages.values()):
#     print(language.title())

# alien_0 = {'color': 'green', 'points': 5}
# del alien_0['points']
# point_value = alien_0.get('points', 'No point value assigned.')
# print(point_value)

# 列表

# current_users = ["Alice", "Bob", "David", "Steve", "Black"]
# new_users = ["Neri", "Sena", "Black", "ALICE", "Hotaru"]
# current_users_check = [current_user.lower() for current_user in current_users]
# for new_user in new_users:
#     if new_user.lower() in current_users_check:
#         print("此用户名已被占用！请使用不同的用户名。")
#     else:
#         print("成功!")

# squares = [value**2 for value in range(1, 11)]
# print(squares)

# digits = []
# for i in list(range(10, 0, -2)):
#     digits.append(i)
# print(min(digits))
# print(max(digits))
# print(sum(digits))

# new_list = ["abandent", "blance", "client"]
# new_list.append("devide")
# new_list.insert(4, "eslint")
# del new_list[4]
# new_list.pop()
# new_list.remove("client")
# new_list.sort(reverse=True)
# sorted(new_list)  # 临时排序（不改变列表）
# new_list.reverse()
# for i in new_list:
#     print(i, end=' ')

# 变量和简单数据类型

# str = "123"
# print(str[:-1])

# MAX_CONNECTIONS = 5000
# x, y, z = 0, 0, 0

# universe_age = 14_000_000_000
# print(universe_age)

# favorite_language = ' python'
# print(favorite_language.lstrip())
# favorite_language = 'python '
# print(favorite_language.rstrip())
# favorite_language = ' python '
# print(favorite_language.strip())

# first_name = "ada"
# last_name = "lovelace"
# full_name = f"{first_name} {last_name}"
# message = f"Hello, {full_name.title()}!"
# print(message)

# str = "HelLo, worLd!"
# print(str.title())
