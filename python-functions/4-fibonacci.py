def fibonacci_sequence(n):
    num1 = 0
    num2 = 1
    count = 1
    next_num = 0
    if n > 1:
        while count <= n:
            print(next_num, end=", ")
            count += 1
            num1 = num2
            num2 = next_num
            next_num = num1 + num2
    else:
        print("")
