def greet_student(name):
    return f"Hello, {name}"



def calculate_scores(scores):
    number_of_subjects = len(scores)
    average_score = sum(scores) / number_of_subjects
    return number_of_subjects, average_score



def check_result(average):
    if average >= 50:
        return "Pass"
    else:
        return "Fail"


def main():
    
    name = input("Enter student name: ")
    
    scores_input = input("Enter scores separated by space: ")
    scores = list(map(int, scores_input.split()))

    
    greeting = greet_student(name)
    subjects, average = calculate_scores(scores)
    result = check_result(average)

    
    print(greeting)
    print("Subjects:", subjects)
    print("Average Score:", average)
    print("Result:", result)



main()
