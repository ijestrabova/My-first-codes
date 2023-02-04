

s = "acdacdefacdacdefacdacdefacdacdefacdacdefacdacdefacdacdefacdacdefacdacdefacdacdefacdacdef"

import itertools
from itertools import combinations

string_found = False
for string_length in range(len(s), 0, -1):
    if string_found:
        break
    for start in range(len(s)):
        if string_found:
            break
        if string_length > len(s[start: start + string_length]):
            break
        current_substring = s[start: start + string_length]
        for idx in range(len(current_substring)):
            if idx == len(current_substring) - 1:
                string_found = True
                print(current_substring)
                break
            if current_substring[idx] > current_substring[idx+1]:
                break


# for string_length in range(len(s), 0, -1):
#     flag = False
#     for start in range(len(s)):
#         if string_length > len(s[start: start + string_length]):
#             break
#         current_substring = s[start: start + string_length]
#         for i2,letter in enumerate(current_substring):
#             if i2 == len(current_substring)-1:
#                 print("Longest substring in alphabetical order is: ", "".join(current_substring))
#                 flag = True
#             if letter > "".join(current_substring[i2+1: len(current_substring)]):
#                 break
#         if flag == True:
#             break
#     if flag == True:
#         break

# for i in range(len(s), 0, -1):
#     flag = False
#     for current_substring in get_all_substrings(s):
#         for i2,letter in enumerate(current_substring):
#             if i2 == len(current_substring)-1:
#                 print("Longest substring in alphabetical order is: ", "".join(current_substring))
#                 flag = True
#             if letter > "".join(current_substring[i2+1: len(current_substring)]):
#                 break
#         if flag == True:
#             break
#     if flag == True:
#         break








# for substring_length in range(len(s), 0, -1):
#     for idx, letter in enumerate(s):
# for idx,letter in enumerate(s):
#     if letter < s[idx+1]:
# print("Longest substring in alphabetical order is: ", ss)]
