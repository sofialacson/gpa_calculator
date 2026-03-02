def get_num_courses():
        num_courses=int(input("Welcome to the GPA calculator! Please enter the number of courses you completed this semester. "))
        while num_courses<=0:
            print("Error. You must enter a number greater than zero.")
            num_courses=int(input("Welcome to the GPA calculator! Please enter the number of courses you completed this semester. "))
        return num_courses
         
def get_grades(num_courses):
    grades_list = []
    for i in range(num_courses):
        course_grade=float(input(f"Please enter the final mark you achieved in course {i+1}: " ))
        if course_grade>=0 and course_grade<=100:
                grades_list.append(course_grade)
                    
        else:
            print("Error. You must enter a valid grade from 0-100.")
            course_grade=float(input(f"Please enter the final mark you achieved in course {i+1}: " ))
    
    return grades_list

    
def calc_avg(grades_list,num_courses):
    
    sum_grades=sum((grades_list))
    student_average=round((sum_grades/num_courses),1)
    return student_average

def convert_letter(student_average):
        if student_average>=90:
            letter_grade="A+"
        elif student_average>=85:
            letter_grade="A"
        elif student_average>=80:
            letter_grade="A-"

        elif student_average>=77:
            letter_grade="B+"
        
        elif student_average>=73:
            letter_grade="B"

        elif student_average>=70:
            letter_grade="B-"

        elif student_average>=67:
            letter_grade="C+"
    
        elif student_average>=63:
            letter_grade="C"
        
        elif student_average>=60:
            letter_grade="C-"

        elif student_average>=50:
            letter_grade="D"

        else:
            letter_grade="F"
        return letter_grade


def convert_gpa(student_average):
    if student_average>=90:
        grade_point_average=4.0

    elif student_average>=85:
        grade_point_average=4.0

    elif student_average>=80:
        grade_point_average="3.7"

    elif student_average>=77:
        grade_point_average=3.3

    elif student_average>=73:
        grade_point_average=3.0

    elif student_average>=70:
        grade_point_average=2.7

    elif student_average>=67:
        grade_point_average=2.3

    elif student_average>=63:
        grade_point_average=2.0

    elif student_average>=60:
        grade_point_average=1.7

    elif student_average>=50:
        grade_point_average=1.0

    else:
        grade_point_average=0.0
    
    return grade_point_average

def read_previous_stats():
    infile=open("results.txt","r")
    grades = []
    infile.readline()
    line = infile.readline()
    while line!="":
        grades.append(line.strip())
        line = infile.readline()

        
    infile.close()
    return grades                


def main():
    user_choice = input('Would you like to calculate your grade or view your previous grades (c/v)? ')
    while user_choice.lower() != 'c' and user_choice.lower() != 'v':
        print('Error. You must enter a valid input. Please try again. ')
        user_choice = input('Would you like to calculate your grade or view your previous grades (c/v)? ')
    
    if user_choice.lower() == 'c':

        num_courses=get_num_courses()
        student_grades=get_grades(num_courses)
        student_avg=calc_avg(student_grades,num_courses)
        letter_grade=convert_letter(student_avg)
        student_gpa=convert_gpa(student_avg)
        
    

        if student_avg<=70:
            message="Time to lock in for next semester!"
        else:
            message="Great work!"
        print(f'Your average last semester was a {student_avg}. This is a {letter_grade}, so you achieved a GPA of {student_gpa}! {message}')
        
        outfile=open("results.txt","w")
        outfile.write("Student's Results:"+"\n")
        outfile.write(str(student_avg)+"\n")
        outfile.write(str(letter_grade)+"\n")
        outfile.write(str(student_gpa)+"\n")
    
    else:
        previous_grades = read_previous_stats()
        if previous_grades == []:
            print('You have not yet inputted any grades into the system.')
        
        print(previous_grades)

    
if __name__ == "__main__":
    main()