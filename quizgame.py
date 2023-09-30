import mysql.connector
from pwinput import pwinput

dbconnection=mysql.connector.connect(host="localhost",user="root",password="2727",database="Admin")
cursor =dbconnection.cursor()

def create_question():
    question=input("Enter the Question:")
    option1=input("Enter the option 1: ")
    option2=input("Enter the option 2: ")
    option3=input("Enter the option 3: ")
    option4=input("Enter the option 4: ")
    correct_option=input("Enter the correct option (1/2/3/4):")

    insert_query="INSERT INTO questions(question, option1, option2, option3, option4,correct_option) VALUES (%s,%s ,%s,%s,%s,%s)"
    cursor.execute(insert_query,(question,option1,option2,option3,option4,correct_option))
    dbconnection.commit()
    print("Question added successfully!")
    
    choice1=input("Insert another question:(yes/no)")
    if choice1=="yes":
        create_question()
    else:
        print("Thank you!...")

def delete_all_questions():
    confirm=input("Are you sure to delete all the existing questions(yes/no)").lower()
    if confirm=="yes":
        query="DELETE FROM questions"
        cursor.execute(query)
        dbconnection.commit()
        print("All the questions are deleted...")
    else:
        print("Deletion Cancelled")


def admin_authentication(admin_username,admin_password):
    print("Please wait untill the unthentication completed ...")

    try:
        query="SELECT COUNT(*) FROM admindetails WHERE username = %s AND password = %s"
        cursor.execute(query,(admin_username,admin_password))
        result=cursor.fetchone()

        if result[0]==1:
            print("Authentication successfull!")
            while True:
                 print("*"*30)
                 print("Admin Menu")
                 print("*"*30)
                 print("1. Create Question")
                 print("2. Delete All Questions")
                 print("3. Logout")
                 admin_choice = input("Select an option:")   
                 if admin_choice == "1":
                     create_question()
                 elif admin_choice == "2":
                     delete_all_questions()
                 elif admin_choice == "3":
                     break
                 else:
                     print("Invalid choice. Please try again.")   
                
        else:
            print("Authentication Failed.Invalid username or password...")

    except Exception as e:
        print(e)

def take_quiz(student_id):
    cursor.execute("SELECT * FROM questions")
    result=cursor.fetchall()
    score=0
    

    for quest in result:
        question,option1,option2,option3,option4,correct_option=quest
        print("Que):"+question)
        print("1."+option1)
        print("2."+option2)
        print("3."+option3)
        print("4."+option4)

        student_answer=input("Enter your answer(1/2/3/4):")
        if student_answer==correct_option:
            score+=1
    print("Your Score is:",score)
    scores_query=("INSERT INTO scores (student_id,score) VALUES(%s,%s)")
    cursor.execute(scores_query,(student_id,score))
    dbconnection.commit()
    print("QUIZ is completed!...\n Thankyou!!!")


def student_authentication(student_id,student_username,student_password):
    print("Please wait untill we process your credentials....")
    
    query1="SELECT COUNT(*) FROM studentdetails WHERE student_username=%s AND student_password=%s"
    cursor.execute(query1,(student_username,student_password))
    result=cursor.fetchone()
    if result[0]==1:
        print("Student Authenticated Successfully!..")
        while True:
            print("*"*30)
            print("Student Menu")
            print("*"*30)
            print("1. Take Quiz")
            print("2. Logout")
            choice2=input("Enter the action to be performed(1/2):")
            if choice2== "1":
                take_quiz(student_id)
            else:
                break
        
    else:
        print("Authentication Failed!...,Invalid username or password...")





while True:
    print("*"*30)
    print("Welcome to the Quiz Game")
    print("*"*30)
    print("1. Admin")
    print("2. Student")
    print("3. Exit")
    choice=input("Enter your appropriate authentication:")


    if choice== "Admin":
        admin_username=input("Enter your username for validation:")
        admin_password=pwinput("Enter your password for validation:")
        admin_authentication(admin_username,admin_password)

    elif choice=="Student":
        student_username=input("Enter your username for validation:")
        student_password=pwinput("Enter your password for validation:")
        student_id=input("Enter your Regestration Number:")
        student_authentication(student_id,student_username,student_password)

    elif choice=="Exit":
        print("Thank you for visiting... Bye!")
        break

    else:
        print("Invalid Choice!...")
        print("Choose the correct one.")


