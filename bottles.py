# trying to relearn/refresh python through projects

### 99 bottles of beer on the wall

def main():
    for num in range(100,0,-1):
        
        if num > 1:
            minus_one = str(num - 1)
            num = str(num)
            print(num + " bottles of beer on the wall, " + num + " bottles of beer, take one down, pass it around, " + minus_one + " bottles of beer on the wall.")
        else: 
            num = str(num)
            print(num + " bottle of beer on the wall, " + num + " bottle of beer, take one down, pass it around, 0 bottles of beer on the wall.")

if __name__ == "__main__":
    main()
        
        