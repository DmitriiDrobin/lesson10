my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
n = 0
while n < len(my_list):

    if my_list[n] < 0:
        break
    elif my_list[n] == 0:
        n = n + 1
    else:
        print(my_list[n])
        n = n + 1