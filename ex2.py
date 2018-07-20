# Exercise 2:
# Print 1 to a user defined input

def main():
    while True:
        userInput = int(input("Enter 1 or else...: "))
        if userInput== 1:
            print(userInput)
            break
        else:
            print("I told you to type 1")
            continue

if __name__ == '__main__':
    main()