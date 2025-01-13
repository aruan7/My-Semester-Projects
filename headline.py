#Clickbait Headline Generator

#Init

#Functions
def gift_headline():
    num = input("Please enter a number (1-99)")
    noun = input("Please enter a noun")
    state = input("Please enter a state")
    print(num + " Gift Ideas to Give Your " + noun + " from " + state)

def photos_headline():
    num = input ("Please enter a number(1-15)")
    noun = input("Please enter a noun")
    country = input("Please enter a country")
    print("These " + num + " Photos" + " of" + noun + " Will Make You Think Twice About Living in " + country)

def travel_headline():
    num = input("Please enter a number(1-15)")
    city = input("Please enter a city")
    country = input("Please enter a country")
    print("Why You've Never Heard of These Top " + num + " Travel Destinations " + "in " + " " + city + "," + country)


#Main
travel_headline()
