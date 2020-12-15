from tkinter.filedialog import askopenfilename
import traceback
import threading
import utils.get_input
import utils.format
import utils.create_output

# get questions file and save questions and choices to two dimensional array
# require: question have number
def save_question(question):
    arr = []
    count = -1

    for i in range (len(question)):
        # check if first letter of questions is a number or not
        if(question[i][0].isnumeric()):
            arr.append([])
            count+=1
            arr[count].append(question[i])
        else:
            arr[count].append(question[i])

    return arr

# get the test answers from student with limited time
def get_student_ans(question):
    student_ans = [None] * len(question)
    current_question = 0
    current_answer = 0
    time_out = False

    # invoke when timer run out
    def out_of_time():
        print("The test is over!")
        time_out = True

    # set timer as 10 minutes
    test_time = threading.Timer(10*60, out_of_time)
    test_time.start()

    while(not time_out):
        utils.format.print_split_line(150)

        # print questions and choices
        for i in range (len(question[current_question % len(question)])):
            print(question[current_question % len(question)][i])

        answer = utils.get_input.char("Choose an answer (only one character are allow) "
                       "(choose 1 to go to the next ans,"
                       " choose 2 to go back"
                       " choose 0 to end the test early): ")

        if answer == '1':
            current_question+=1
        elif answer == '2':
            current_question-=1
        elif answer == '0':
            test_time.cancel()
            break
        else:
            student_ans[current_answer % len(question)] = answer.upper()
            current_answer += 1
            current_question += 1

    return student_ans

# compare student answer to the correct answer and display message
def compare(students_answer,correct_answer):
    incorrect_answer = []
    utils.format.print_split_line(150)

    # check if student answer correctly or not
    for i in range (len(students_answer)):
        if(students_answer[i] != correct_answer[i].split(" ")[1]):

            # check if student answer or not
            if(students_answer[i] != None):
                temp = f'{i+1}.{students_answer[i]}'
                incorrect_answer.append(temp)
            else:
                incorrect_answer.append('No answer')

    # check if student passed the test or not
    if(len(correct_answer) - len(incorrect_answer) >= 15):
        print('Student have passed the exam!')
    else:
        print('Student have failed the exam!')

    print(f"Correct answers: {len(correct_answer)- len(incorrect_answer)}")
    print(f'Incorrect answers: {len(incorrect_answer)}')

    # print incorrect answer
    temp = ''
    for i in range (len(incorrect_answer)):
        temp += incorrect_answer[i] + " "
    print(f'Answer that are incorrect: {temp}')

def main():
    question, cor_ans = [], []

    while True:  # Keep getting input from the user
        try:
            question = utils.get_input.vietnamese_file_to_list("Enter the multiple choice questions path: ")
            cor_ans = utils.get_input.file_to_list("Enter correct answers path: ")
            question = save_question(question)
            if (len(question) <= len(cor_ans)):
                break
            else:
                print('Too many question! Please input again')
        except ValueError:
            print('Conversion error, please re-input')
            continue

    stu_ans = get_student_ans(question)
    utils.create_output.create_text_file("student_answer.txt",utils.format.format_list(stu_ans))
    compare(stu_ans,cor_ans)

main()