
#4)write a Python program to read the 5 subjects marks and calculate the average and display the grade?

subj1= input("enter first subject marks:")
subj2= input("enter second subject marks:")
subj3= input("enter third subject marks:")
subj4= input("enter fourth subject marks:")
subj5= input("enter fifth subject marks:")

average = int(subj1)+int(subj2)+int(subj3)+int(subj4)+int(subj5)
print(average)
avg= int(average)/5

if int(avg)>=70:
    print("Grade A")
elif int(avg)>=50:
    print("Grade B")
else :
    print("Grade C")

