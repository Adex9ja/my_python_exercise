questions = [
    ["What is a computer", "Computer is a television", "Option 2", "Option3", "Option4", "Answer"],
    ["Test 2", "Option1", "Option 2", "Option3", "Option4", "Option1"],
    ["Test 3", "Option1", "Option 2", "Option3", "Option4", "Option2"],
    ["Test 4", "Option1", "Option 2", "Option3", "Option4", "Option4"],
    ["Test 5", "Option1", "Option 2", "Option3", "Option4", "Option1"],
    ["Test 6", "Option1", "Option 2", "Option3", "Option4", "Option4"],
    ["Test 7", "Option1", "Option 2", "Option3", "Option4", "Option4"],
    ["Test 8", "Option1", "Option 2", "Option3", "Option4", "Option1"],
    ["Test 9", "Option1", "Option 2", "Option3", "Option4", "Option3"],
    ["Test 10", "Option1", "Option 2", "Option3", "Option4", "Option1"],
]

test_in_progress = True


def check_answer(question_row, index):
    return question_row[index] == question_row[5]


def average_of_averages(averages):
    output = 0
    for _, mark in averages.items():
        output += mark
    output /= len(averages)
    return output


def get_user_name():
    while True:
        input_name = input('Enter your Name\n')
        if input_name != '':
            return input_name
        else:
            print('Invalid name entered. Try again!')


def get_selected_option():
    while True:
        selected_option = input("Pick an option from 1 to 4\n")
        if selected_option.isdigit() and 1 <= int(selected_option) <= 4:
            return int(selected_option)
        else:
            print('Invalid option selected.Try again!')


def get_number_of_question():
    while True:
        number_of_question = input('How many question do you want to answer?\n')
        if number_of_question.isdigit():
            return int(number_of_question)
        else:
            print('Invalid number entered.Try again!')


def get_if_user_wish_to_continue():
    while True:
        wish_to_continue = input("\nTo continue, Press 1\nTo end test, Press 2\n")
        if wish_to_continue.isdigit() and 1 <= int(wish_to_continue) <= 2:
            return int(wish_to_continue)
        else:
            print('Invalid option selected. Try again!')


result = dict()

while test_in_progress:
    score = 0
    name = get_user_name()
    no_of_question = get_number_of_question()
    for i in range(no_of_question):
        question = questions[i]
        preview = question[0] + "\n1.\t" + question[1] + "\n2.\t" + question[2] + "\n3.\t" + question[3] \
                  + "\n4.\t" + question[4]
        print(preview)
        answer = get_selected_option()
        is_correct = check_answer(question, answer)
        if is_correct:
            score = score + 1
    percentage = (score / 10 * 100)
    result[name] = percentage
    print('Hi ', name, ', Your score is => ', score, 'of ', no_of_question)
    print('Your percentage score => ', percentage, '%')
    want_to_continue = get_if_user_wish_to_continue()
    if want_to_continue == 2:
        test_in_progress = False
for w in sorted(result, key=result.get, reverse=True):
    print(w, result[w], '%')
print('Average score is => ', average_of_averages(result), '%')
