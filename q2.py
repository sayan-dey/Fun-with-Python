
import sys
import re 
import array as arr
  

class DayCount:  
    def __init__(self, d, m, y):  
        self.d = d             
        self.m = m    
        self.y = y    
  
monthDays = [31, 28, 31, 30, 31, 30,  
                        31, 31, 30, 31, 30, 31 ] 
   
def countLeapYears(d): 
      
    years = d.y  
      
    if (d.m <= 2) : 
        years-= 1
          
    return int(years / 4) - int(years / 100) + int(years / 400)
   
  
def getDifference(dt1, dt2) : 
   
    
    n1 = dt1.y * 365 + dt1.d  
  
    for i in range(0, dt1.m - 1) : 
        n1 += monthDays[i]  
  
     
    n1 += countLeapYears(dt1)  
  
    n2 = dt2.y * 365 + dt2.d  
    for i in range(0, dt2.m - 1) : 
        n2 += monthDays[i]  
    n2 += countLeapYears(dt2)  
  
    return (n2 - n1)  
   

arglen = len(sys.argv)
a=arr.array('i', [1, 2, 3])
count = 0
inputFile = open('date_calculator.txt','r')
Lines = inputFile.readlines() 
for line in Lines:
    if line.startswith('D'):
        line = line[7:]
    k = 0 
    s = line.strip()

    lis = re.split('th |rd |st |, | |/|-|\.',s)
    
    if lis[1] == 'Jan' or lis[1] == 'January':
        lis[1] = 1
    elif lis[1] == 'Feb' or lis[1] == 'February':
        lis[1] = 2    
    elif lis[1] == 'Mar' or lis[1] == 'March':
        lis[1] = 3
    elif lis[1] == 'Apr' or lis[1] == 'April':
        lis[1] = 4        
    elif lis[1] == 'May':
        lis[1] = 5
    elif lis[1] == 'Jun' or lis[1] == 'June':
        lis[1] = 6    
    elif lis[1] == 'Jul' or lis[1] == 'July':
        lis[1] = 7
    elif lis[1] == 'Aug' or lis[1] == 'August':
        lis[1] = 8
    elif lis[1] == 'Sep' or lis[1] == 'September':
        lis[1] = 9
    elif lis[1] == 'Oct' or lis[1] == 'October':
        lis[1] = 10
    elif lis[1] == 'Nov' or lis[1] == 'November':
        lis[1] = 11
    elif lis[1] == 'Dec' or lis[1] == 'December':
        lis[1] = 12                    

    for i in lis:
        a[k] = int(i)
        k = k + 1

    if arglen > 1:
        if sys.argv[1][1] == 'm' or sys.argv[1][1] == 'M':
            temp = a[0]
            a[0] = a[1]
            a[1] = temp 

    if count == 0:       
        dt1 = DayCount(a[0], a[1], a[2])
    else:
        dt2 = DayCount(a[0], a[1], a[2])
    count = count + 1            

outputFile = open('output.txt', 'w')
outputFile.write('Date Difference: {} Day'.format(abs(getDifference(dt1, dt2))))

outputFile = open('output.txt', 'r')
readFile = outputFile.read()
print(readFile)

inputFile.close()
outputFile.close()

     
    