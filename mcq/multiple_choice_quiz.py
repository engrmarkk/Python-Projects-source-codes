# Created a class for the quiz
class Question:
    # the __init__ method lets the class initialize the attributes (i.e. ask and answer)
    def __init__(self, ask, answer):
        # The 'self' represents the instance of the class, it enables us to access the attributes below
        self.ask = ask  # This enables us to access the question attribute from the class
        self.answer = answer  # This enables us to access the answer attribute from the class


# Creating a list of questions ranging from the index 0 to 9. That is 10 questions in total
question_to_ask = [
    "Which of this is not a programming language?\n(a) Javascript\n(b) Python\n(c) Cobra\n(d) Ruby\n\n> ",  # first question
    "Which of this is not a track in programing?\n(a) Frontend\n(b) Backend\n(c) Cloud\n(d) Middle-end\n\n> ",  # second question
    "Which of this frameworks is used for backend development?\n(a) Node.js\n(b) React.js\n(c) Vue.js\n(d) Angular.js\n\n> ",  # third question
    "AWS is related to which track?\n(a) Backend\n(b) Cloud\n(c) Frontend\n(d) UI/UX\n\n> ",  # fourth question
    "HTML is used in which track?\n(a) Cloud\n(b) Backend\n(c) Frontend\n(d) UI/UX\n\n> ",  # fifth question
    "Flask is used with which language?\n(a) Python\n(b) Javascript\n(c) Java\n(d) Ruby\n\n> ",  # sixth question
    "HTML is used for?\n(a) Structure\n(b) Functionality\n(c) Beautify\n(d) Database\n\n> ",  # seventh question
    "React is a framework for?\n(a) Cloud\n(b) Backend\n(c) Frontend\n(d) Devops\n\n> ",  # eight question
    "The 'P' in OOP stands for what?\n(a) paradigm\n(b) parachute\n(c) programming\n(d) post\n\n> ",  # ninth question
    "VSCODE can be used to write which language?\n(a) Javascript\n(b) Python\n(c) C++\n(d) All of the above\n\n> "  # tenth question, which is the last question
]

# using the Question class above to access self.ask and self.answer
# Here we are using the class to set up a question and answer for the quiz
# Question(self.ask, self.answer). The question at each index from the question_to_ask list above represents the ask attribute from the __init__ function in the class
# while the letters in quote represents the answer attribute from the __init__ function from the Question class
questions = [
    # This is basically calling the __init__ function from the Question class and using the ask attribute as the question at each index
    # and the answer attribute as the right answer for each question

    # So a list is being created to get the question from the question_to_ask list at their various indexes
    Question(question_to_ask[0], 'c'),  # question 1 is gotten from the index of 0 in the question_to_ask list and the letter attached to it is its correct answer
    Question(question_to_ask[1], 'd'),  # question 2 is gotten from the index of 1 in the question_to_ask list and the letter attached to it is its correct answer
    Question(question_to_ask[2], 'a'),  # question 3 is gotten from the index of 2 in the question_to_ask list and the letter attached to it is its correct answer
    Question(question_to_ask[3], 'b'),  # question 4 is gotten from the index of 3 in the question_to_ask list and the letter attached to it is its correct answer
    Question(question_to_ask[4], 'c'),  # question 5 is gotten from the index of 4 in the question_to_ask list and the letter attached to it is its correct answer
    Question(question_to_ask[5], 'a'),  # question 6 is gotten from the index of 5 in the question_to_ask list and the letter attached to it is its correct answer
    Question(question_to_ask[6], 'a'),  # question 7 is gotten from the index of 6 in the question_to_ask list and the letter attached to it is its correct answer
    Question(question_to_ask[7], 'c'),  # question 8 is gotten from the index of 7 in the question_to_ask list and the letter attached to it is its correct answer
    Question(question_to_ask[8], 'c'),  # question 9 is gotten from the index of 8 in the question_to_ask list and the letter attached to it is its correct answer
    Question(question_to_ask[9], 'd')  # question 10 is gotten from the index of 9 in the question_to_ask list and the letter attached to it is its correct answer
]

# creating an empty list globally to store the student's data (i.e. name and scores of each student)
infos = []


# The function that run the quiz
def run_mcq():
    # Used the try and except function to catch errors encountered during the run of the program
    try:
        result = 0  # Initial value of each student result/score before taking the quiz is set to be 0
        print('Each question carries 1 mark\n')     # This is telling the student how many mark is for each question
        user_name = input('What is your name?\n> ').title()  # prompting the student to enter his/her name and assign the input to the user_name variable in capitalized form irrespective of which case the student used in typing his/her name (i.e. the first letter is in capital letter)
        while not user_name:    # While your input is empty, it keeps asking for your name
            print('Please enter your name to continue\n')
            user_name = input('Your name please?\n> ').title()
        # Lopping through the questions list above
        for question in questions:
            prompt_question = input(question.ask)  # displaying the question at each index synchronously to the student so he/she can answer each questions
            # while your answer is not a, b, c or d, it keeps asking you to choose a valid option
            while prompt_question != 'a' and prompt_question != 'b' and prompt_question != 'c' and prompt_question != 'd':
                print('\nWrong input, please choose between a, b, c or d\n')
                prompt_question = input('Your answer please\n> ')   # if you fail to input the right option initially, you are to correct yourself once you get this prompt
            if prompt_question == question.answer:  # This is going to check if what the student inputted is same as the self.answer we declared as the correct answer for each question in the question list above
                result += 1  # if the two are the same, the value of result will increase by 1 for each correct answer
                print("\nYou are right\n")  # and the program will tell you are right for each question answered correctly
            else:  # If the student input is wrong, the else block will be executed
                print(f'\nYou are wrong, the correct answer is {question.answer}\n')  # If you are wrong, the program let you know you are wrong and as well tell you the right option for the question

        inf = f'Name = {user_name}\nResult = {result}/{len(questions)}\n'  # After answering all questions, the student's name and total result will be assigned to the variable 'inf'
        infos.append(inf)  # Then the student's details will be appended inside the empty list 'info' we created above

    except Exception as e:  # If there is an error, the except block will be executed. The error will be saved in a variable 'e'
        print("Error: ", e)  # and this is going to tell you what the error is
    # If you canceled the program halfway, this except block will let you know upon cancelling
    except KeyboardInterrupt:
        print('\nYou cancelled the program')


# Another function to ask if another student wants to take the quiz
def another_user():
    # Using a call back to call the first function, this will run the first function before running the codes below it
    run_mcq()
    try:
        # while this remain True, the code in this block keeps running, it stops running once False is returned
        while True:
            # asking if another student would like to take the quiz and assigning the value in lowercase to the an_user variable
            an_user = input('Does any student wants to take the quiz? (Yes/No)\n').lower()
            # while ur input is not yes or no, it keeps asking you the same question, with an 'invalid input' message till you either input yes or no
            while an_user != 'yes' and an_user != 'no':
                print('invalid input, try again')
                an_user = input('Does any student wants to take the quiz? (Yes/No)\n').lower()
            # if your input is yes, the first function runs again
            if an_user == 'yes':
                run_mcq()
            # if your input is no, the details of the students saved inside the info list gets displayed for you to see the name and scores of the student(s)
            elif an_user == 'no':
                if infos:   # This is going to check if there is any student info in the infos list, if there is, the if block will be executed
                    print('\nBelow is the the result of student(s) who took the quiz\n')
                    # looping through the info list, print each info on the console
                    for info in infos:
                        print(info)
                else:   # If there is nothing inside the infos list, this else block will be executed, hence, prints out 'No student took the quiz'
                    print('\nNo student took the quiz\n')
                # After running the if or else block, it returns False to end the program
                return False
    # If you encounter an error during the course of the program, this block let you know what error it is you encountered
    except Exception as e:
        print(e)
    # whether encountering error or not, this block gets printed out at the end of the program
    finally:
        print('........................End of quiz.........................')


# Calling the second function to run the program
another_user()
