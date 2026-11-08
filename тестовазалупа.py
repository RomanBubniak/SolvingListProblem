numbers = [7, 9, 20, 8, 10]
for num in numbers:
    for num1 in range(len(numbers)):
        num2 = numbers[num1] +1
        res = num + num2
        if res == 15:
            print(num, num2)