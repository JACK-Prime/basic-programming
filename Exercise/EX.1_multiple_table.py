# exercise Program maltiple table 

x = int(input("Enter a number for the multiplication table: "))

for i in range(1, x+1):
    for j in range(1, 13):
        print(f"{i} * {j} = {i * j:2d}")
    print("==============================")  # New line after each row