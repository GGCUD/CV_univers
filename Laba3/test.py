import re

def find_lines_with_keywords(file_path, keyword):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    for line in lines:
            if re.search(keyword, line):
                print(line.rstrip())

