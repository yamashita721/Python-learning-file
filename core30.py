# nested loop
# making rectangle or square using this with symbols

rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the columns: "))
symbol = input("Enter a symbol to use: ")




for x in range(rows):
    for y in range(columns):
        print(symbol, end=" ")
    print()
    # take a look at notes from last slide!