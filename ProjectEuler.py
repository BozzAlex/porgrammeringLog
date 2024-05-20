txt = input("Import list.\n")
EntireList = []
for i in txt:
    if i == " ":
        print("", end="")
    else:
        EntireList.append(i)
print(len(EntireList))
print(EntireList)