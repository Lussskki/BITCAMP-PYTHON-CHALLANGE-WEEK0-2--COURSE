def main():
    n = int(input("What is N? "))
    while True:
        if n != 0 :
           maybePositive = input("are you sure its positive number? ")
           
           
           yes = "yes"
           no = "no"
        if maybePositive == yes :
            print("yes it is positive")
            break
        elif maybePositive == no:
            print("it is not positive")
            break

main()