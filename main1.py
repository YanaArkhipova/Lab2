day=int(input("Days: "))
month=int(input("Month: "))
year=int(input("Years (the last two digits): "))

if day*month==year:
    print("The date is magic!")
else:
    print("Normal date")
