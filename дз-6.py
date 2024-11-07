"""    Задание №1     """

#
# def get_password(password):
#     if len(password) < 6:
#         return False
#
#     has_letter = False
#     has_number = False
#
#     for letter in password:
#         if letter.isalpha():
#             has_letter = True
#         elif letter.isdigit():
#             has_number = True
#
#     return has_letter and has_number
#
# print(get_password(input('Введите пароль: ')))

"""     Задание №2      """


# def get_number_list(numbers_list, number=0):
#     nearest_num = numbers_list[0]
#
#     for num in numbers_list:
#         if abs(num - number) < abs(nearest_num - number):
#             nearest_num = num
#
#     return nearest_num
#
#
# print(get_number_list([33, 22, 30, 40], 34))