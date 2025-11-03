
"""
Define the name of the histpry file (eg "history.txt")

    start the loop while true
        Ask for input ( in the form of expression)
        Or command (history,clear,exit)


        If user enter exit
            print goodbye message and exit the program
            Break the loop

        If user enter history
            try to open the history for reading
            if file exist and not empty print (all calculation)
            if file does not found, or its empty print("History is empty")

            Continue to the next loop

        If user enter clear
            open the history file and overwrite it with nothing
            Print (History cleared)
            Continue to the next loop

        Otherwise (assume user entered the calculation)
            try to parse the input and get the number and operator  (split the number by space )
            If input is not valid
                print("Invalid input")
                Continue to the next loop

            Perform the calculation using if/else
                if operator is + then add
                if operator is - then subtract
                if operator is * then multiply
                if operator is / then divide


            show the result of the calculation
            append the calculation to the history file
            Continue to the next loop

End the loop
"""
History_file="history.txt"

def show_history():
    with open(History_file,"r")as f:
        lines=f.readlines()
        if len(lines) == 0:
            print("History is empty")
        else:
            for line in lines:
                print(line.strip())



def clear_history():
    with open(History_file,"w"):
        print("History cleared")

def save_history(calculation) as f:




