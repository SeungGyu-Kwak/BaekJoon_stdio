# test file

ary1 = [[0 for col in range(3)] for row in range(3)]

ary1[1][2] = 13
for i in ary1:
    for j in i:
        print(j, end=" ")
    print()
