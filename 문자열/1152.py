string = input()

if len(string) == 0:
    print(0)
elif len(string) == 1:
    if string == " ":
        print(0)
    else:
        print(1)
elif string.replace(" ","") == "":
    print(0)
else:
    if string[0] == " ":
        string = string[1:]
    if string[-1] == " ":
        string = string[:-1]
    split = string.split(" ")

    if  "" in split:
        new_split = []
        for i in range(len(split)):
            if split[i] != "":
                new_split.append(split[i])
        split = new_split

    print(len(split))
