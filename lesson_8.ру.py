# Контекстный менеджер "with, работа с файлами
# w - write (запись)
# a - add (дозапись)
# x - создание нового файла с проверкой названия

# file = open('new_file.txt','w')
# file.write('Строка на кириллице')
# file.close()

# with open('new_file.txt', 'a') as file:
 #    file.write('\nдобавляем третью строку')

# with open('new_file1.txt', 'x') as new_file:
#    new_file.write('new data')


# users_count = 1

# while users_count < 5:
#    name = input('enter name: ').title()
#    surname = input(f"{name},please enter your surname:")
#    birth_date = input(f'{name} {surname},please enter your birth_date: ')
#    with open('users_info.txt','a') as file:
#        file.write(f'\n{name} {surname}, {birth_date}')
#        users_count += 1

with open('users_info.txt', 'r') as file:
    print(file.read()[-1])



