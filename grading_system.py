#####################################################################################
# Start of global variable declarations

# list of grading system functions
sys_functions = ["Add", "Update", "Delete", "Search"]

# temporary storage of student ids
stud_ids = []

# temporary storage of student names
stud_names = []

# list of subjects 
stud_subjects = ["math", "science", "language", "history"]

# temporary var storage of grades
# should be multi dimentional array
stud_grades = []

#####################################################################################
# set of functions from here ---- to move to new py file once logic is done for OOP


# get the student id first then check the temp storage if it's there
# if it is, then get the index from the list and insert/add/update the value 

def verify_id(p_stud_id):
    for indx, id in enumerate(stud_ids):
        if(p_stud_id == id):
            user_choice = input("Student ID is already taken. Would you like to update the record instead? Y/N")

            # full while loop logic
            while user_choice.upper() != "Y" and user_choice.upper() != "N": user_choice = input("Please enter a valid choice: Y/N ")

            if user_choice.upper() == 'Y':
                #printing the value for debugging
                update_record(p_stud_id) #plan is to ask the user to update records when an id is already in the list
                #needs to have to loop through the list and get the index from the list so the other list can update accordingly
            elif user_choice.upper() == 'N':
                return False       
    
    return True

def add_record(stud_id, stud_name, stud_grade):
    stud_ids.append(stud_id)
    stud_names.append(stud_name)
    stud_grades.append(stud_grade)
    print(f"Record successfully saved! {stud_name} with a student Id of: {stud_id} has a grade average of: {stud_grade}!\n")

def update_record(stud_id):
    #update the record by looping through the list and getting the index
    for id in stud_ids:
        if id == stud_id:
            #get the index of the student id
            indx = stud_ids.index(id)
            #get the new name and grade
            new_name = input("Enter new name: ")
            new_grade = calc_grade()
            #update the values in the list
            stud_names[indx] = new_name
            stud_grades[indx] = new_grade
            print(f"Record successfully updated! {new_name} with a student Id of: {stud_id} has a grade average of: {new_grade}!\n")
            return
        
    print("Student not found.")

def delete_record(stud_id):
    #same thing - loop through the list and delete when found
    verify_id(stud_id)

def search_record(stud_id):
    #loop through the list and show record of students
    for indx, id in enumerate(stud_ids):
        if id == stud_id:
            print(f"Student found! {stud_names[indx]} with a student Id of: {stud_id} has a grade average of: {stud_grades[indx]}!\n")
        return
    print("Student not found.")

def calc_grade(): #loop through the list and add them all up - divide by the range of the list to get the average
    stud_grade = 0

    for i in stud_subjects:
        in_sub = int(input(f"Enter {i} grade: "))
        stud_grade+=in_sub

    return stud_grade/len(stud_subjects)

# - End of functions
#####################################################################################

def start_grading_system():
    user_choice = int(input("Hi, welcome to this school's grading system. How can I help you today?\n" \
    "1. Add student record\n" \
    "2. Update student record\n" \
    "3. Delete student recrod\n" \
    "4. Seach student record\n" \
    "5. Exit\n\n" \
    "Please enter the number of your choice:"))

    stud_id = int(input("Enter your student ID: "))

    #filter the input of the user - making sure it's not empty - never mind verifying if the characters are numerical or not

    while not stud_id: #if empty, don't proceed and keep asking until it's valid
        stud_id = input("Please enter a valid id.")

    if not verify_id(stud_id):
        if user_choice == 1:
            stud_name = input("Enter Student Name: ")
            grd_ave = calc_grade()
            add_record(stud_id, stud_name, grd_ave)
            user_choice = 0
        elif user_choice == 2:
            update_record(stud_id)
            user_choice = 0
        elif user_choice == 3:
            delete_record()
            user_choice = 0
        elif user_choice == 4:
            search_record()
            user_choice = 0
        elif user_choice == 5:
            print("Thank you for using the Grading System. Goodbye!")
            exit()
        else:
            user_choice = int(input("Please chooose between 1-5:"))
            #make this one a funtion
            #could have a function to reprint the user_choice so it just goes back to it when user input is invalid
            in_stud_name = input("Student's Full Name: ")
    start_grading_system()
    
start_grading_system()



    


