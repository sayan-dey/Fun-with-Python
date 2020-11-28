# SSD Assignment 3

### For Question 1,
First of all, I have treated Employee IDs as strings.
Submitted only the file: `q1.py` for this question.
Assuming the input file: `org.json` will be present in same directory where `q1.py` will be present.
Just run it as `python q1.py`. It will automatically read the input file.

* Input format:

number_of_employees(n) empid1 empid2 ..... empidn

\(all inputs are in same line , separated by space)


* Output format:

common leader: empid

leader empid is num levels above employee empid1 
\.
\.
\.

leader empid is num levels above employee empidn



In case someone inputs the employee ID of topmost leader, printed "Leader not found".
Also, assumed "name" and "parent" will remain as keys of dictionaries (except for L0, where only "name" will be present).

* Average cyclomatic complexity: A


### For Question 2,
Submitting only the file: `q2.py` for this question.
Assuming the input file: `date_calculator.txt` will be present in same directory where `q2.py` will be present.
We need to run it as `python q2.py date_format`. 
For eg, run it as `python q2.py mm/dd/yyyy` if the date format in the input file is : mm/dd/yyyy.
(Although, no command line argument is required if the dates are like: 10th September, 2020 or 10th Sep, 2020).

Also, I have printed the contents of `output.txt`, that will be created while running the program.
Also, please note that, I have printed absolute value of the difference of two dates.

* Average cyclomatic complexity: A


### For Question 3,
Here, meeting slot duration should be given as command line input.
So, if slot duration = 1.5 hours,
run the program as `python q3.py 1.5`
Similarly, if slot duration = 2 hours,
run the program as `python q3.py 2`

I have submitted only the file: `q3.py` for this question.
Assumed that the input files will be present in same directory where the .py file will be present.
The program will automatically read them and also print the contents of `output.txt` at the end.
Please provide the input files exactly in the same format as given in question.

* Average cyclomatic complexity: A


