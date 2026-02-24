
def check(question, tryagain, checkforwhat):
    loop = True
    while loop:
        try:
            if checkforwhat == "int":
                int(input(question))
            elif checkforwhat == "float":
                float(input(question))
            loop = False
        except ValueError:
            print(tryagain)
    return question


uni = input("Name your nearest uni: ")

loop = True
while loop:
    try:
        bike_count = int(input("How many bicycles do you own: "))
        loop = False
    except ValueError:
        print("Not an integer")

print("User choice is ", bike_count)


print(check("give me a integer", "not a integer"), "int")