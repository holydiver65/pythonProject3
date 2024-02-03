# weighted exam score average

# entering how many exams you have done

number_of_exams = int(input("enter number of exams:"))
print(number_of_exams)
# enter how many credits these exam covers
total_credits = int(input("enter how many credits these exams  cover:"))
# begin with average of 0 and then add up percentages

average = 0
for exam in range(number_of_exams):
    score = int(input("enter exam score"))
    exam_credits = int(input('enter how many credits this exam covered:'))
    average = average + score*exam_credits/total_credits
print("your average is", average)
