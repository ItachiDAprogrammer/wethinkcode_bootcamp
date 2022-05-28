def user_name():
    username = input("Enter username: ")
    return username


def read_file(username):
    student_results_file = open("student_results.txt", "rt")
    file_content = student_results_file.read()
    

    
    


def calculate_exam_av():
    pass


def calculate_group_project_av():
    pass


def calculate_daily_exercise():
    pass


def first_class_or_av_pass():
    pass


def user_status():
    pass


if __name__ == '__main__':
    username = user_name()
    read_file(username)
