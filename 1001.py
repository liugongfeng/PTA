if __name__ == "__main__":
  
    line = input().split(" ")
    a , b = int(line[0]), int(line[1])
    
    print('{:,}'.format(a+b))
