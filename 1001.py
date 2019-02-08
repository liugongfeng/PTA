def toDo(s):
    if len(s) > 3:
        return s[:-3] + ',' + s[-3:]
    else:
        return s


def f(a, b):
    result = a + b
    if result > 0 :
        print(toDo(str(result)))
    else:
        print("-" + toDo(str(result)[1:]))

shuru = input()
num = [int(e) for e in shuru.split(" ")]
f(num[0], num[1])

