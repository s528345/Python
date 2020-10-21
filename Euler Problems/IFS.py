import EulerProblems
import main

def prompt():
    choice = str(input("Choose a Euler problem (1-10) to solve or exit to quit: "))
    return choice

def choice(choice):

    if choice == 1:
        print("Solution to Euler's Problem 1: ", EulerProblems.problem001(), "\n")

    if choice == 2:
        print(EulerProblems.problem001())
