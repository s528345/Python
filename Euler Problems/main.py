import EulerProblems

def prompt():
    choice = input("Choose a Euler problem (1-10) to solve or 0 to quit: ")
    return choice

def choice(number):

    if (number == 1):
        print("Solution to Euler's Problem 1: ", EulerProblems.problem001(), "\n")

    if(number == 2):
        print("Solution to Euler's Problem 2: ", EulerProblems.problem002(), "\n")

if __name__ == '__main__':
    problem = int(prompt())
    while(problem != 0):
        if (problem > 3):
            print("Oops! Try Again\n")
            problem = int(prompt())
        if(problem == 0):
            break
        choice(problem)
        problem = int(prompt())
    print("Goodbye!")




