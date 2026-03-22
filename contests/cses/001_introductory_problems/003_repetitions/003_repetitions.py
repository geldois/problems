# https://cses.fi/problemset/task/1069

line = input()
last_char = None
actual_substring_lenght = 0
max_substring_lenght = 0

for char in line:
    if not last_char:
        last_char = char

    if last_char == char:
        actual_substring_lenght += 1

        if actual_substring_lenght > max_substring_lenght:
            max_substring_lenght = actual_substring_lenght

    if last_char != char:
        actual_substring_lenght = 1

    last_char = char

print(max_substring_lenght)
