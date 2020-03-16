# hobbies = ['Reading', 'Sleeping', 'Singing', 'Loving you']

# # for H in hobbies:
# #     print(H)

# # for H in hobbies[0:2]:
# #     print(H)

# for H in hobbies:
#     if H == 'Sleeping':
#         print(f'{H} the best thing ever!')
#         break
#     else:
#         print(H) 

age = 36
num = 0

while num <= age:
    if num % 2 != 0:
        print(num)
    if num > 14:
        break
    num += 3