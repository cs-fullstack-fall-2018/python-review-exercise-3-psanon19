# Exercise 4:
# Create a loop that quits with a user defined input


def main():

    input1= input("Press q to quit")
    iQuit= input("Enter your Quit phrase")

    while(input1 != iQuit):  #"q"):
        input1=input("Press q to quit")

if __name__ == '__main__':
    main()