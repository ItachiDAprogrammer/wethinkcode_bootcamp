def user_name():
    username = input("Enter username: ")
    return username


def read_file(username):
    student_results_file = open("student_results.txt", "rt")
    file_content = student_results_file.read()
    student_results = file_content.split("\n\n")

    # Slice each section of file data
    exams_data = student_results[:2]
    gp_data = student_results[2:4]
    de_data = student_results[4:]

    # Get only the results for each assessment
    exam_students = exams_data[1].split("\n")
    gp_students = gp_data[1].split("\n")
    de_students = de_data[1].split("\n")[:-1] # Get all except last

    # Store the usernames
    usernames = []

    # Get exam scores
    exam_scores = []
    for x in exam_students:
        student = x.split(" - ")
        usernames.append(student[0])
        exam_scores.append(student[1])

    exam_results = {name:score for (name,score) in zip(usernames, exam_scores)}

    # Get group project(gp) scores
    gp_scores = []
    for x in gp_students:
        score = x.split(" - ")[1]
        gp_scores.append(score)
        
    gp_results = {name:score for (name,score) in zip(usernames, gp_scores)}

    # Get daily exercises(de) scores
    de_scores = []
    for x in de_students:
        score = x.split(" - ")[1]
        de_scores.append(score)
        
    de_results = {name:score for (name,score) in zip(usernames, de_scores)}

    # Get average scores for each assessment
    user_exam_score = calculate_exam_av(exam_results[username])
    user_gp_score = calculate_group_project_av(gp_results[username])
    user_de_score = calculate_daily_exercise(de_results[username])

    # Get final result
    f_result = first_class_or_av_pass(user_exam_score, user_gp_score, user_de_score)
    f_status = user_status(f_result)

    
    # Display users results
    print(f"{f_result}/100")
    print(f_status)
    if f_result >= 90:
        print("You passed first class")
    elif f_result >= 80:
        print("You passed normally")
    else:
        print("Uh, oh! You fell short of the accuracy threshold (80%).")



def calculate_exam_av(score):
    result = (int(score) / 100) * 60
    return result


def calculate_group_project_av(score):
    result = (int(score) / 20) * 20
    return result 


def calculate_daily_exercise(score):
    result = (int(score) / 30) * 20
    return result


def first_class_or_av_pass(exam_score, gp_score, de_score):
    result = exam_score + gp_score + de_score
    return int(result)


def user_status(final_score):
    return "Passed" if final_score >= 80 else "Failed"


if __name__ == '__main__':
    username = user_name()
    read_file(username)
