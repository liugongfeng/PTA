if __name__ == "__main__":
  
    line = input().split(" ")
    a , b = int(line[0]), int(line[1])
    
    print('{:,}'.format(a+b))
    
   
  
    # another way
    s = input().split(" ")
    a = int(s[0])
    b = int(s[1])
    c = str(a+b)
    
    for i in range(len(c)):
        print(c[i], end="")
        if c[i] == '-':
            continue
        if len(c) - i == 4:
            print(',', end='')
