# Exercise 5:
# Create a loop that takes user input and put it in an array. Once the user quits, print all items in the array. DO NOT print the array, print the items in the array.

def main():

    smallArray=[]
    while True:
        userInput = input("Enter whatever or enter 'q' to quit")
        if userInput=="q":
            for answer in smallArray:
                print(answer)
            break
        else:smallArray.append(userInput)

if __name__ == '__main__':
    main()