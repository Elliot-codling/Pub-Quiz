#quiz
import csv, time
from csv import reader
file_name = "questions.csv"         #can change the file name globally here

#finds the current question number that has been entered
def quest_find():
    question_num = 0
    file_r = open(file_name, "r")
    with file_r as read_obj:
        csv_reader = reader(read_obj)
        for row in csv_reader:
            if row == []:           #if nothing is found at start
                pass
            else:
                question_num = int(row[0])      #question number is set to the first column

    file_r.close()
    return question_num

#checks to see if the answer is equal and adds a delay
def check_answer(user_input, answer):
    print("")
    print("Your answer was...")
    time.sleep(1)
    if user_input.lower() == answer.lower():
        print("Correct!")

    else:
        print("Incorrect!")

#main code ---------------------------------------

#when the user wants to play the game
def gameplay():
    print("")
    file_r = open(file_name, "r")
    with file_r as read_obj:
        csv_reader = reader(read_obj)
        for row in csv_reader:
            if row == []:
                pass
            else:
                print("Q{}) {} ({})".format(row[0], row[1], row[2]))
                print("")
                user_input = input(">>> ")

                check_answer(user_input, row[3])            #checks inputted answer
    file_r.close()

#add new questions to the program
def add_ques():
    print("")
    new_question = input("New question to ask: ")
    new_options = input("Enter options to choose from (A = ... D = ...): ")
    new_answer = input("Answer (A/B/C/D): ")

    file = open(file_name, "at")
    file.write("{},{},{},{}\n".format(quest_find() + 1, new_question, new_options, new_answer))
    file.close()

#remove the questions from the program
def remove_ques():
    print("")
    print("Would you like to see all of the saved questions (Y/N): ")
    print("")
    option = input(">>> ")
    temp_list = []
    with open(file_name, "r") as read_obj:
        csv_reader = reader(read_obj)
        for row in csv_reader:
            if row == []:
                pass
            else:
                if option.upper() == "Y":
                    print("Q{}) {} {}".format(row[0], row[1], row[2]))
                else:
                    pass

                #read all of the csv file and store it in a list
                temp_list += [[row[0], row[1], row[2], row[3]]]

    question_del = input("What question number would you like to remove? ")
    #[[question1], [question2]]...
    #then rebuild the csv file by using w to write over it
    csv_file = open(file_name, "w")
    csv_file.write("")
    csv_file.close()

    
    #when going through the list, check if the question is == to the question wanted to remove
    csv_file = open(file_name, "at")
    number_reduce = 0
    for question in temp_list:
        #question is printed out in ["", "", ""...]
        if question[0] == question_del:
            print("Deleting question: {}".format(question_del))
            number_reduce += 1
        else:
            #if found then when rebuilding, set the question number by -1
            #else then print question number not found
            question_number = int(question[0]) - number_reduce
            question_number = str(question_number)
            csv_file.write("{},{},{},{}\n".format(question_number, question[1], question[2], question[3]))
    csv_file.close()
    if number_reduce == 0:
        print("Question {} could not be found.".format(question_del))

def main():
    print("Welcome to the ePub Quiz!")
    print("")
    print("(1) Play")
    print("(2) Add questions")
    print("(3) Remove questions")
    print("")
    option = input(">>> ")

    if option == "1":
        gameplay()
    elif option == "2":
        add_ques()
    elif option == "3":
        remove_ques()
    else:
        print("Invalid input")

main()