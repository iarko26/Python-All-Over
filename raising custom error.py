def customval(val):
    if val > 10 and val < 20:
        raise ValueError("Value is between 10 and 20")
    

try:
    customval(1)

except ValueError as e:
    print(e)

    



