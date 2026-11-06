#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 23:06:27 2024

@author: arinabasai

Project name: TutorAdvice

"""

#If the user is still studying and would like to use the tutoring services, this list will be essential for the code execution

list_grades = []

#The hourly pay is the only constant used in this code:
    
h_p = 40 #Euros

#The final output for the user who chooses to use the tutoring services will be displayed as a text file. To work with text files, the io module is imported and the file created with a writing permission:
 
import io

w_file = io.open('study_plan', 'w') 

#Functions, used for the code:
    
    #Since the current average can be both calculated and entered by the user manually, it is better to check student's eligibility for the programs using a function:
    
def check_eligibility (cur_av: float):   
   if 1 <= cur_av < 5.5:
      return "Seems like you'll have minimum options."
   elif 5.5 <= cur_av < 6.5:
       return "You have a good chance to apply to a decent program!"
   elif 6.5 <= cur_av <  7.5:
       return "You can apply to a very good university!"
   elif 7.5 <= cur_av <= 10:
       return "You can get into any school you choose if you play your cards right!"
   else:
       raise ValueError
       
    #Since the average is calculated and recalculated several times within the code, the following function can be used:
        
def calculate_av(list_grades):
  sum = 0
  for i in list_grades:
    sum +=i
    cur_av = sum/len(list_grades)
  return cur_av
           
    #If the user would like to use the tutoring services, to calculate the achievable grade, three minimum grades need to be counted and eliminated from the list, provided by the student previously:
        
def minimum_grade (list_grades):
 min_grade = list_grades[0]
 for g in list_grades:
  if g < min_grade:
    min_grade = g
 list_grades.remove(min_grade)
 return min_grade

        
    
print("Hello, student!", "Welcome to the TutorAdvice tool!", "It seems that you've made a choice to apply for a postgraduate program.", "Using this tool, you can evaluate the level of your future university based on your current average and, if you would like to, see how you can improve using our tutoring services", sep = "\n")
print()
print("Now we should see if your grade can be changed. Are you still getting your degree?", "[1] - I'm still studying", "[2] - I'm done with my BSc", sep = "\n")
while True:
    try:
        choice1 = int(input("I choose the option:\n"))
        print()
        if choice1 == 1: 
        #Since there is no known average yet, the program helps the user calculate it
          print("Let's calculate your current average: put a minimum of three grades")
          while True:
              try:
                  grade = float(input("Enter your grades from 1 to 10, when finished, put '0'':\n"))
                  if grade == 0:
                      #Because at least 3 grades need to be included in the list for the later operations, the user is not allowed to move forward unless this requirement is met
                      if len(list_grades) >= 3:
                       break
                      else:
                       print("We need at least 3 grades to proceed")
                  elif 1<= grade <=10:   
                      list_grades.append(grade)  
                  else:
                      print("The grade should be from 1 to 10\n")
              except ValueError:
                  print("Please, enter a number", "\n")
          cur_av = calculate_av(list_grades)
          print("Your current average is: " + str(cur_av), "\n", check_eligibility(cur_av), "\n")     
          #Despite being able, the user may choose not to improve the grade
          print("You can improve your score if needed. The opportunities are almost limitless. Would you like to use our tutoring services?", "[1] - I want to reach for the stars", "[2] - I'm fine with my current grade", sep="\n") 
          while True:
              try:
                  choice2 = int(input("I choose the option:\n"))
                  print()
                  if choice2 == 1:
                    #Here, the opportunities of grade improvement by using tutoring services are illustrated. For that, 3 lowest grades are eliminated and substituted by 10s - the maximum achievable result
                    print("Ambitious! Now, let's see how your grade could be improved. We can change only 3 of your grades with a guaranteed result of a 10.") 
                    min_grade1 = minimum_grade(list_grades)
                    min_grade2 = minimum_grade(list_grades)
                    min_grade3 = minimum_grade(list_grades)
                    print("Your minimum grades are: ", str(min_grade1), ", ", str(min_grade2),", ", str(min_grade3))
                    print("Now, let's see what your average could be")
                    list_grades.extend([10, 10, 10])
                    cur_av = calculate_av(list_grades)
                    print("With our help, your average could be ", cur_av)
                    print("With such a result, ", check_eligibility (cur_av))
                    print("Now, let's develop a study plan. We can provide up to 10 hours of weekly training. The minimal duration of one lesson is 1 hour.")
                    #This section is used not only for scheduling purposes but also to calculate the intermediate and full payments
                    sum_hours = 0
                    while sum_hours <= 10:  
                        try:
                            day = input("What day of the week would you like to use for your studies?\n")
                            while True:
                                try:
                                    hours = int(input("How many hours would you like to study during that day (1-10)?\n"))
                                    if 1 <= hours <= 10 and (sum_hours + hours) <= 10:
                                        break
                                    else:
                                        if (sum_hours + hours) > 10:
                                            print("You can't exceed a total of 10 hours. You have " + str(10 - sum_hours) + " hours remaining.")
                                        else:
                                            print("Please enter a valid number between 1 and 10.")
                                except ValueError:
                                    print("Please, choose a valid option")         
                            daily_price = hours * h_p
                            sum_hours += hours
                            w_file.write(day + ": " + str(hours) + " hours for " + str(daily_price) + " euros\n")
                            if sum_hours < 10:
                                while True:
                                    try:
                                        print("Would you like to continue?", "[1] - Yes", "[2] - No", sep="\n")
                                        choice3 = int(input("I choose the option:\n"))
                                        if choice3 ==1 or choice3 == 2:
                                            break
                                        else:
                                            print("The number should be either 1 or 2")
                                    except ValueError:
                                        print("Please, choose a valid option")
                                if choice3 == 2:
                                    break
                            else:
                                print("You have reached the maximum of 10 hours.")
                                break 
                        except ValueError:
                            print("Put a valid number from 1 to 10")
                    total_price = sum_hours * h_p
                    w_file.write("Your overall payment is: " + str(total_price) + " euros\n")
                    w_file.close()
                    #Here, the user has an opportunity to see the full receipt
                    print("Your schedule and corresponding receipt are ready. Would you like to see the schedule?", "[1] - Yes", "[2] - No", sep="\n")
                    while True:
                        try:
                            choice4 = int(input("I choose the option:\n"))
                            if choice4 == 1:
                                r_file = io.open('study_plan', 'r')
                                while True:
                                 result = r_file.read()
                                 r_file.close()
                                 print(result)
                                 print("Thank you for using our services. Good luck with studying!")
                                 break
                                break
                            elif choice4 == 2:
                                print("Thank you for using our services. Good luck with studying!")
                                break
                            else:
                                print("The number should be either 1 or 2")
                        except ValueError:
                            print("Please, choose a valid option")
                    break
                  elif choice2 == 2: 
                    print ("Good luck with your application. Just try not to drop the score!")
                    break
                  else:
                    print("The number should be either 1 or 2", "\n")
              except ValueError:
                        print("Please, choose a valid option", "\n")
          break  
        elif choice1 == 2: 
          print ("This may limit your choices, as you can't change your average anymore. Let's figure out what programs are feasible for you")
          while True:
              try:
                  cur_av = float(input("What was your average grade from 1 to 10:\n"))
                  print("\n", check_eligibility(cur_av), "Good luck with your application!")
                  break
              except ValueError:
                 print("Please, enter a number", "\n")           
          break
        else:
          print("The number should be either 1 or 2", "\n")
    except ValueError:
        print("Please, choose a valid option", "\n")