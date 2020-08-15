import math 

#Any odd number with a natural square root { 9, 25, 81, 361}
number = 9

squareRoot = math.sqrt(number)
if squareRoot % 1 != 0 or number % 2 == 0:
    print("It is not a valid number")
    exit()

resultArray = []

squareRoot = int(squareRoot)

for count in range(int(squareRoot)):
    array = []
    for count2 in range(int(squareRoot)):
        array.append(0)
    resultArray.append(array)

centerIndex = squareRoot // 2

col = 1
x = centerIndex - 1
y = centerIndex 
direction = "right"
changeToBottom = False

for num in range(number):
    
    if direction == "right":
        x += 1
        resultArray[y][x] = num + 1
        
        if changeToBottom:
            direction = "bottom"
            changeToBottom = False
        elif x - centerIndex == col // 2:
            col += 2
            changeToBottom = True
    
    elif direction == "bottom":
        y += 1
        resultArray[y][x] = num + 1
        
        if y - centerIndex == col // 2:
            direction = "left"
    
    elif direction == "left":
        x -= 1
        resultArray[y][x] = num + 1
        
        if -1 * (x - centerIndex) == col // 2:
            direction = "top"
    
    elif direction == "top":
        y -= 1
        resultArray[y][x] = num + 1
        
        if -1 * (y - centerIndex) == col // 2:
            direction = "right"


for count in range(len(resultArray)):
    print(str(resultArray[count]))