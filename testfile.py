#this is the file i test for anything i cant test manually inside my prototypes



test = input("press a number here").lower()

print(test)

def invalid():
    print("invalid option")
    return


choice = input("enter something other than [no] ").lower()

while choice != "no":
    choice = input("enter something other than [no] ").lower()
    if choice == "no":
        print("you broke the cycle")
        break
    else:
        invalid()
