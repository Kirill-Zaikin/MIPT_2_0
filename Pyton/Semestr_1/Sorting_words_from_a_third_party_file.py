import os

def clear_terminal():
    # Для Windows
    if os.name == 'nt':
        os.system('cls')
    # Для Unix/Linux/Mac
    else:
        os.system('clear')

clear_terminal()

max_len_consol = 220
print("-" * max_len_consol)

file_name = "test.txt"

with open(file_name, 'r') as fd:
    content = fd.read()

lines = content.split('\n')
words = []

for line in lines:
    line_words = line.split(" ")
    words = words + line_words

hash_map = {}

for word in words:
    if word == "": 
        continue

    if word in hash_map.keys():
        hash_map[word] = hash_map[word] + 1
    else:
        hash_map[word] = 1

hash_map = dict(sorted(hash_map.items(), key=lambda x: x[0], reverse=False))
hash_map = dict(sorted(hash_map.items(), key=lambda x: x[1], reverse=True))
for key, value in hash_map.items():
    print(f"{value} {key}")

print("-" * max_len_consol)