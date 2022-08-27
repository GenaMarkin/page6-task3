x = int(input('Enter the number of lines: '))
for i in range(0, x):
    for j in range(i * 10, (i + 1) * 10):
        print(j + 1, end=' ')
    print('\n')
