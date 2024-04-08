import re
import math
class Search:
 def find_lines_with_keyword(self, filename, word):
    # Открываем файл для чтения
    with open(filename, 'r') as file:
        lines = file.readlines()
        # Читаем содержимое файла построчно
        for line in file.readlines():
           if re.search(word, line):
                # Если ключевое слово найдено, выводим строку
                print(line.strip())
                break
