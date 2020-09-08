#Project by: Viktoria Cseke
#This project is about getting users input that affects the stored data
import random

def load_data():#load in the file then place it in a list
    employee_id=[]
    first_name=[]
    last_name=[]
    email=[]
    salary=[]
    with open("employees.txt") as employee_file:
        for line in employee_file:
            line = line.split(',')
            employee_id.append(int(line[0]))
            first_name.append(line[1])
            last_name.append(line[2])
            email.append(line[3])
            salary.append(float(line[4]))
        return employee_id,first_name,last_name,email,salary

def show_menu(employee_id,first_name,last_name,email,salary):#menu that calls different functions
    print("Welcome! 😺")
    while True:
        #This is the menu for the user
        print("\n--------Menu--------")
        print("1. View all employees")
        print("2. View a particular employee")
        print("3. Edit the salary of an employee")
        print("4. Add a new employee")
        print("5. Delete an employee")
        print("6. Give a bonus to each employee, writing the details to a file")
        print("7. Generate report for management")
        print("8. Exit\n")

        try:# gets user input
            user_choice = int(input("Which option would you like?>>> "))
            if user_choice==1:
                show_all_employees(employee_id,first_name,last_name,email,salary)

            elif user_choice==2:
                show_one_employee(employee_id,first_name,last_name,email,salary)

            elif user_choice==3:
                change_salary(employee_id,salary)

            elif user_choice==4:
                add_employee(employee_id,first_name,last_name,email,salary)

            elif user_choice==5:
                remove_employee(employee_id,first_name,last_name,email,salary)

            elif user_choice==6:
                save_bonus_info(employee_id,first_name,last_name,salary)

            elif user_choice==7:
                generate_report(first_name,last_name,salary)

            elif user_choice==8:
                print("Goodbye!")
                break

            else:
                print("Only numbers from 1 to 8 please!")
        except ValueError:
            print("Must be a number!")

def save_data(employee_id,first_name,last_name,email,salary):#saves the data into the text file
    employees_file = open("employees.txt","w")
    for num,employee in enumerate(employee_id):
        employees_file.write("{},{},{},{},{:.2f}{}".format(employee_id[num], first_name[num], last_name[num], email[num], salary[num],"\n"))
    employees_file.close()

def show_all_employees(employee_id,first_name,last_name,email,salary):
    print("{:^7}|{:^20}|{:^20}|{:^30}|{:^15}".format("ID", "First name", "Last Name", "E-mail", "Salary(€)"))
    print("-" * 100)
    for num,employee in enumerate(employee_id):
        #prints all the needed data, ----------needs to be formated later--------
        print("{:^7}|{:^20}|{:^20}|{:^30}|{:^15.2f}".format(employee_id[num], first_name[num], last_name[num], email[num], salary[num]))

def find_employee(user_input,employee_id): #looks for specific employee and returns the position
    for num in range(0,len(employee_id)):
        if employee_id[num]==user_input:
            return num
    return -1

def show_one_employee(employee_id,first_name,last_name,email,salary):#as the function name suggests, it shows one employee
    while True:
        try:
            user_input=int(input("Employee number?>>"))
            num=find_employee(user_input,employee_id)
            if employee_id[num]==user_input:
                print("{} {} {} {} {:.2f}".format(employee_id[num], first_name[num], last_name[num], email[num], salary[num]))
                break
            else:
                print("\nUser not found!🙁")
                break
        except ValueError:
            print("Numbers only please!")

def change_salary(employee_id,salary):#looks for the employee id, then changes the salary
    while True:
        try:
            user_input=int(input("Employee number?>>"))
            num=find_employee(user_input,employee_id)
            if employee_id[num]==user_input:
                new_salary = read_nonnegative_float("Enter salary:>>>")
                salary[num] = new_salary
                return salary[num]
            else:
                print("\nUser not found! 🙁")
        except ValueError:
            print("Numbers only please!")

def read_nonnegative_float(prompt):#checks for negative number or 0
    while True:
        try:
            number = float(input(prompt))
            if number >0:
                break
            else:
                print("No zero and non-negative numbers please...")
        except ValueError:
            print("Must be numeric...")
    return number

def read_nonempty_string(prompt):#checks for non empty string
    something_is_wrong = True
    while something_is_wrong:
        word = input(prompt)
        if len(word) > 0:
            return word
        else:
            print("Please don't leave it empty")

def add_employee(employee_id,first_name,last_name,email,salary):
    new_id=generate_unique_id(employee_id)
    add_first_name = read_nonempty_string("Add first name:>>>")
    add_last_name = read_nonempty_string("Add second name:>>>")
    unique_email = generate_unique_email(add_first_name,add_last_name,email)
    add_salary = read_nonnegative_float("Enter salary:>>>")
    #----------------appends to the correct list the informations
    employee_id.append(new_id)
    first_name.append(add_first_name)
    last_name.append(add_last_name)
    email.append(unique_email)
    salary.append(add_salary)

def generate_unique_id(employee_id):
    new_id=random.randint(10000,99999)#random 5 digit ID generator
    while True:
        if new_id in employee_id:
            new_id=random.randint(10000,99999)#generates new 5 digit ID if already exists
        else:
            return new_id

def generate_unique_email(add_first_name,add_last_name,email):
    f_name=add_first_name.lower()#changes to lowercase so the email format will be the same
    s_name=add_last_name.lower()
    unique_email=f_name+"."+s_name+"@cit.ie"
    for num,mail in enumerate(email):#checks if email exists, if yes adds a number to it
        if unique_email in email:
            num+=1
            unique_email=f_name+"."+s_name+str(num)+"@cit.ie"
        else:
            return unique_email

def remove_employee(employee_id,first_name,last_name,email,salary):
    while True:
        try:
            user_input = int(input("Employee number?>>"))#checks for a specific id number then deletes the employee
            num = find_employee(user_input, employee_id)
            if employee_id[num] == user_input:
                del employee_id[num]
                del first_name[num]
                del last_name[num]
                del email[num]
                del salary[num]
                break
            else:
                print("User not found! 🙁")
        except ValueError:
            print("Numbers only please!")

def save_bonus_info(employee_id,first_name,last_name,salary):
    bonus_file = open("bonus.txt", "w")#creates a new text file and saves the information into it
    for num, employee in enumerate(employee_id):
        while True:
            try:
                user_percentage=int(input("{} {} {} (%):".format("End of the year bonus for",first_name[num],last_name[num])))
                if user_percentage>=0:#user can choose to add 0 as bonus if they want to
                    calc_bonus=(user_percentage*salary[num])/100 #calculates the bonus
                    bonus_file.write("{} {} {} {:.2f}{}".format(employee_id[num], first_name[num], last_name[num],calc_bonus, "\n"))
                    print("{} {} {} {:.2f}{}".format(employee_id[num], first_name[num], last_name[num], calc_bonus, "\n"))
                    break
                else:
                    print("No negative numbers please!")
            except ValueError:
                print("numbers only please")
    bonus_file.close()

def generate_report(first_name,last_name,salary):
    total=sum(salary)
    average=total/len(salary)#straight forward, just gets the average
    print("{}{}{}".format("-"*8,"Report","-"*8))
    print("{}{:.2f}".format("The average salary is:€ ", average))
    print("\nThe largest salary earned is:€ {}".format(max(salary)))
    print("\nThe name(s) of largest salary:")
    for num in range(0,len(salary)):
        if salary[num]==max(salary):#checks each for the highest salary and prints it
            print("{} {} ".format(first_name[num],last_name[num]))

def main():#the main function
    employee_id, first_name, last_name, email, salary=load_data()
    show_menu(employee_id,first_name,last_name,email,salary)
    save_data(employee_id, first_name, last_name, email, salary)
    exit()

main()