
def getUserSelection():
    while True: 
        try:
            chosenStat = int(input("\nPlease enter the number of which stat you'd like to see: \n1: Top 5 Goal Leaders \n2: Top 5 Assist Leaders "
            "\n3: Top 5 Points Leaders\n"))
            return chosenStat
        except ValueError:
            print("\nInvalid Selection. Please try again")

if __name__ == '__main__':
    userStat = getUserSelection()

            



