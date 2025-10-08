def convert(userInput):
    return userInput.replace(":)", "🙂").replace(":(", "🙁")

def main():
    userInput = input("Please input a string with either a sad or happy face inside! ")
    print(convert(userInput))

main()
