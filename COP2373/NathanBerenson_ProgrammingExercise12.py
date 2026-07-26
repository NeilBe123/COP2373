import numpy as np

#Loads the CSV and separates names from exam scores
def load_data(filename):

    #Opens the file and reads the header
    with open(filename, "r") as f:
        header = f.readline().strip().split(',')

    #Slices the exams
    exam_labels = header[2: ]

    #loads the first and last names as strings
    first_names = np.genfromtxt(filename, delimiter = ',', skip_header=1,
                          usecols= 0, dtype = str)

    last_names = np.genfromtxt(filename, delimiter = ',', skip_header=1,
                          usecols= 1, dtype = str)

    #counts how many colunms are in the header list
    num_cols = len(header)

    #loads the scores as float values
    scores = np.genfromtxt(filename, delimiter = ',',
                           skip_header=1, usecols=range(2,num_cols), dtype=float)

    return first_names, last_names, scores, exam_labels

#Displays the csv data
def print_data(first_names,last_names, scores, exam_labels, n=10):
    print("Exam columns:", exam_labels)

    #Prints a header row
    print(f"{'First Name':<10}", f"{'Last Name':<10}", *[f"{lbl:<8}" for lbl in exam_labels])

    #loops over every row
    for i in range(len(first_names)):

        #Prints the student's names and scores
        print(f"{first_names[i]:<10}", f"{last_names[i]:<10}",*[f"{scores[i][j]:<8}" for j in range(len(exam_labels))])

#prints the states for each exam
def per_exam_stats(scores, exam_labels):

    #loops over every exam
    for i, label in enumerate(exam_labels):

        #slices every row (:) and column (i)
        col = scores[:,i]

        #displays the information
        print(f"\nFor exam {i+1}: ")
        print(f"  Mean:   {np.mean(col):.2f}")
        print(f"  Median: {np.median(col):.2f}")
        print(f"  StdDev: {np.std(col):.2f}")
        print(f"  Min:    {np.min(col):.2f}")
        print(f"  Max:    {np.max(col):.2f}")

#Prints out the total stats
def total_stats(scores):

    #'flatten' collapses the information into one array
    flat = scores.flatten()

    #displays the information
    print("\nTotal exam Stats: ")
    print(f"Mean:   {np.mean(flat):.2f}")
    print(f"Median: {np.median(flat):.2f}")
    print(f"StdDev: {np.std(flat):.2f}")
    print(f"Min:    {np.min(flat):.2f}")
    print(f"Max:    {np.max(flat):.2f}")

#Displays how many passed and failed each exam
def pass_fail_per_exam(scores, exam_labels, passing_grade=60):

    #loops through each exam
    for i, label in enumerate(exam_labels):

        #splices the scores
        col  = scores[:, i]

        #filters the scores then displays them
        passed = np.sum(col >= passing_grade)
        failed = np.sum(col < passing_grade)
        print(f"{label}: Passed = {passed}, Failed = {failed}")

#Calculates the overall pass rate
def overall_pass_percentage(scores, passing_grade=60):

    #Combines every score into one array
    flat = scores.flatten()

    #'.size' gives the total number of element in flat
    total_grades = flat.size

    #filters the scores
    total_passed = np.sum(flat >= passing_grade)

    #Calculates the percentage and displays the info
    percentage = (total_passed / total_grades) * 100
    print(f"\nOverall Pass Percentage: {percentage:.2f}%")

#contains all the previous functions
def main():
    filename = "grades.csv"
    first_names, last_names, scores, exam_labels = load_data(filename)
    print_data(first_names,last_names, scores, exam_labels)
    per_exam_stats(scores, exam_labels)
    total_stats(scores)
    pass_fail_per_exam(scores, exam_labels)
    overall_pass_percentage(scores)

main()