def word_and_symblos_counter(line):
    words = line.split()
    word_number = len(words)
    symbols_number = sum(len(word) for word in words)
    return word_number, symbols_number

def create_and_fill_file(file_path):
    try:
        with open(file_path, 'w') as file:
            print(f"Файл '{file_path}' створений. Введіть текст у файл. Для завершення введення введіть 'exit'.")
            while True:
                user_input = input()
                if user_input.lower() == 'exit':
                    break
                file.write(user_input + '\n')
        with open(file_path, 'r') as file:
            line_number = 1
            for line in file:
                word_number, symbols_number = word_and_symblos_counter(line)
                print(f"Рядок {line_number}: Кількість слів - {word_number}, Кількість символів - {symbols_number}")
                line_number += 1

        print(f"Введення завершено. Текст було записано у файл '{file_path}' Він збережений в папці Users.")
    except Exception as e:
        print(f"Виникла помилка: {e}")

if __name__ == "__main__":
    file_path = "zalik.txt"
    create_and_fill_file(file_path)
