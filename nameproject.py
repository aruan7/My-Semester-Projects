#Angie Ruan
#Name Project

print("Welcome to your My Little Pony character")
print("Answer the questions to find out your My Little Pony character")
ans = input("coffee or soda?")
if ans == "soda":
    ans = input("artistic or fun?")
    if ans == "artistic":
        ans = input("reading/writing or designing?")
        if ans == "reading/writing":
            print("You are Twilight Sparkle")
        else:
            print("You are Rarity")
    if ans == "fun":
        ans = input("partying/going out or singing?")
        if ans == "partying/going out":
            print("You are Pinkie Pie")
        else:
            print("You are Fluttershy")
if ans == "coffee":
    ans = input("athletic or energetic?")
    if ans == "athletic":
        ans = input("rodeo or track?")
        if ans == "rodeo":
            print("You are Applejack")
        else:
            print("You are Rainbow Dash")
    if ans == "energetic":
        ans = input("exercising or cooking?")
        if ans == "exercising":
            print("You are Shining Armor")
        else:
            print("You are Spike")
