def restaurantName():
    firstPart = input("What's your favorite city or town? ")
    lastPart = input("What's your favorite food? ")
    results = "Maybe name your restaurant {}-{}?".format(firstPart, lastPart)
    return print(results)

if __name__ == "__main__":
    restaurantName()