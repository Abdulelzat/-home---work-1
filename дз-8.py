
def guess_number():
    low = 1
    high = 100
    attempts = 0
    guesses = []

    print("загадайте числоот до 100, и я попробую угадать его.")

    while True:
        guess = (low + high) // 2
        attempts += 1
        guesses.append(guess)

        user_input = (f"Ваше число {guess}? Ответьте 'да', 'больше' или 'меньше': ").strip().lower()

        if  user_input == "да":
            print(f"Угадано число {guess} за {attempts} попыток!")

            with open("results.txt", "w") as file:
                file.write(f"Загадано число: {guess}\n")
                file.write(f"Количество попыток: {attempts}\n")
                file.write(f"Список попыток: " + ",".join(map(str, guesses)) + "\n")

            break
        elif user_input == "больше":
            low = guess + 1
        elif user_input == "меньше":
            high = guess - 1
        else:
            print(("Пажалуйста, ведите 'да', 'больше' или 'меньше'."))
guess_number()













