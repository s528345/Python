import IFS

if __name__ == '__main__':
    choice = IFS.prompt()
    while choice != 'exit':
        if choice == 'exit':
            print("Goodbye!")
            break

        if choice != 'exit' and int(choice) < 3:
            number = int(choice)
            IFS.choice(number)
            choice = IFS.prompt()
        if(str(choice) != 'exit' and int(choice) > 2):
            print("\nOops! Try again\n")
            choice = IFS.prompt()



