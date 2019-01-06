# trying to relearn/refresh python through projects

### 99 bottles of beer on the wall

def bottles():
    for num in range(100,0,-1):
        
        if num > 1:
            print(str(num) + " bottles of beer on the wall, " + str(num) + " bottles of beer, take one down, pass it around, " + str(num-1) + " bottles of beer on the wall.")
        else: 
            print("1 bottle of beer on the wall, 1 bottle of beer, take it down, pass it around, 0 bottles of beer on the wall.")

if __name__ == "__main__":
    bottles()
        
        