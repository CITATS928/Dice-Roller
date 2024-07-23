# roll a "die" some number of times.
# roll - run it once and go into a loop
# roll 1 - produce a number 1-6 random and print it
# roll 2 - produce two numbers 1-6 and print them
# roll 3 - produce three numbers and print them.
#
import random


def roll():
    return(int(random.randint(1,6)))

def main():
    print("Your first number is: ",end ="")
    print(roll())
    string = ""
    user_Input = int(input("how many times would you like to run?"))
    for i in range(1,user_Input+1):
        if i == user_Input:
            string +=str(roll())
            break
        string +=str(roll())+", "
    print(string)

if __name__=='__main__':
    main()
    