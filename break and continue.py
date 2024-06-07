for i in range(12):
    if i==5:
        print("printing stopped at 5.")
        break
    print(i)

for i in range(12):
    if i==10:
        print("printing skipped at 10.")
        continue
    print(i)
