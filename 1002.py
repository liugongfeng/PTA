

if __name__ == "__main__" :
    a = [0 for i in range(1001)]
    s1 = input().split(" ")
    s2 = input().split(" ")
# num1 : [2, 1, 2.4, 0, 3.2]
# num2 : [2, 2, 1.5, 1, 0.5]

    for i in range(int(s1[0])):
        a[int(s1[2*i+1])] += float(s1[2*i+2])

    for i in range(int(s2[0])):
        a[int(s2[2*i+1])] += float(s2[2*i+2])

    count = 0
    for i in range(1001):
        if a[i]:
            count += 1

    if count:
        print(count, end=" ")
    else:
        print(count)

    for i in range(1000, -1, -1):
        if a[i]:
            count -= 1
            if count > 0:
                print(i, a[i], end=' ')
            else:
                print(i, a[i])





