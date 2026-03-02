
# Design Report

# Introduction
The purpose of this program is to allow users to input their final marks from their previous term, and calculate their overall average, lettered grade, and GPA using the 4.0 grading system. This was implemented through utilizing fundamental coding techniques such as variables, conditional statements, loops, operators, functions, lists, reading and writing text files, as well as automated testing. 

# Design
This program was effectively composed of smaller functions to simplify complex logic. The GPA calculator is broken up into three specific types of functions; collecting user input, performing calculations using this input, as well as reading into a "results.txt" file that stores previously stored data. The input functions include get_num_courses(), and get_grades(). The calculation functions utilized in this program are: calc_avg(), convert_letter(), and convert_gpa(), which each take the user's input as parameters (number of courses completed in the previous term or the student's calculated average) to complete these calculations. The file reading function utilized in this program is "results.txt", which also stores the student's average, lettered grade, and GPA, one per line.  
    
For example, the student's overall average is calculated using the following function: 

def calc_avg(grades_list,num_courses):

    sum_grades=sum((grades_list))
    student_average=round((sum_grades/num_courses),1)
    return student_average
    
The code above essentially takes the list of final grades inputted by the user, as well as the number of courses completed, as parameters to compute the student's average. To calculate the student's average, the sum of grades is taken by utilizing the sum (list method), and dividing this by the number of courses completed. 

Generally all program logic in the code is separated from the user interface so that the logic can be tested automatically. The main function is used to assign variables which are processed through input functions, as well as providing the output for the user. 

For example, the main function is defined as followed: 

def main():
    user_choice = input('Would you like to calculate your grade or view your previous grades (c/v)? ')
    while user_choice.lower() != 'c' and user_choice.lower() != 'v':
        print('Invalid input. Try again')
        user_choice = input('Would you like to calculate your grade or view your previous grades (c/v)? ')
    
    if user_choice == 'c':

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
            print('You have not entered any grades yet.')
        
        print(previous_grades)
    
Variables are assigned at the beginning of the function. Then the print function is utilized to provide the user a message in the terminal which contains the output of the program.

By separating the logic code from the main (user interface) code, the logic can be tested much simpler through automated testing. Streamlining the code into smaller functions allowed for more ease in identifying the root cause of bugs or syntax errors as the test cases identified the cause of program bugs.

# Design Highlights 
One aspect of the design that I am proud of is how I was able to effectively simplify my code to make it easier for people to comprehend. Beginning the project, I initially started with one large block of code in order to organize my ideas on how I would like to approach the design. From there I simplified the code into more succinct and clear logic within smaller functions. Not only did it make it easier for me to trace through the code myself, but it also made it much easier to test the program when broken into smaller pieces of code. 
 
Furthermore, one area of complexity in the design that I had to overcome was determining the ranges in my conditional statements when converting the final grade into a lettered grade and GPA. Initially, I had planned to explicitly code in ranges that the student average would fall under, ie:
    if student_avg<=85 and student_avg>=90:
        letter_grade="A"

Subsequently, I realized this would be problematic if the student's average fell between these boundary hardcoded endpoints, provided their calculated average for the previous term was a float number. To overcome this challenge, I used elif statements after my first if conditional, and started with the greatest possible grade range they could achieve (>=90), and incremented downwards from there. By doing this I was able to account for all numbers in all ranges, including floats, rather than explicitly hardcoding ranges. 

# Areas For Improvement
 If provided more time, one component I would like to implement into my program is giving the user different conversion options to calculate GPA. Many Canadian schools follow different grading systems. For example at McMaster University, they follow a 12 point system, where 12 corresponds to a 4.0 on a typical grading system. Most schools such as the University of Waterloo, and University of Toronto follow the 4.0 grading system, but it would be an interesting feature to implement if given more time. 


# Lessons Learned
One lesson I learned as I designed this program was the importance of manual testing throughout writing the code. Many bugs in my code were identified through manual testing. For instance, inputting floats or negative values for the number of courses and final marks allowed me to manually test the program's behaviour when provided unexpected inputs. 

Another lesson learned through this project was that designing a program is like a cycle. Similar to the engineering design process, it is necessary to brainstorm ideas, create a plan, determine the most promising plan, implement, and reiterate. Specifically going back into the code to simplify and identify logic errors was key in implementing my design. 
    
    