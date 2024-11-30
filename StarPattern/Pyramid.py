# n = 5
# for i in range(1, n):
#         print(i, end=' ')
# print()

def pyramid(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            print('*' , end=' ')
        print()

pyramid(5)

   