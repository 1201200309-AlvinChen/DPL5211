#Display the student names in reverse order studnames
 
studnames = ["Alvin Chen", "Mei You Chen", "Hen You Chen"]
studnames.append("Alvin")

num = [3,6,9,12,23]
square = []

for studindex in range(2,-1,-1) :   #2,1,0
    print(studnames[studindex])

# studnames.reverse ...reverse list
# studnames.append ...to add a new value
# studnames.remove ...to remove the value

# given an array 0f 3,6,9,12,23 create another array containing the squared number of each number from the first array and display the second array 