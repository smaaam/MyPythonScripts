"""

****************
*              *
*              *
*              *
****************



"""
def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Only 1 symbol please.')

    if (width < 2) or (height < 2):
        raise Exception('Width and height must be over 2.')

    
    print(symbol * width)

    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)

    print(symbol * width)

boxPrint('@', 5, 5)
