import ast
import sys 
import array as arr
import glob
import re

# method to check if all elements of a list are same
def checkList(lst): 
  
    ele = lst[0] 
    chk = True
      
    for item in lst: 
        if ele != item: 
            chk = False
            break; 

    return chk  

def convert24(str1): 
	
    if str1[-2:] == 'AM' and str1[:2] == '12': 
        return '00' + str1[2:-2] 
			 
    elif str1[-2:] == 'AM': 
        return str1[:-2] 
	 
    elif str1[-2:] == 'PM' and str1[:2] == '12': 
        return str1[:-2] 
		
    else: 
		  
        if len(str1) == 7:
            return str(int(str1[:2]) + 12) + str1[2:5]
        else:
            return str(int(str1[:1]) + 12) + str1[1:4]



flis = glob.glob('Employee*.txt')  # list of Employee*.txt files in current directory

num = len(flis)  # stores no. of files to read
dicti = []  # list of dictionaries (every file is read as a dictionary)
name = []  # list to store names of employees
date = []  # list to store given dates
busy = []  # list where each element = list of busy slots of an employee
avl = []  # list where each element = list of available slots of an employee

for x in range(0,num):
    fl = open (flis[x],'r')
    contents = fl.read()
    dicti.append(ast.literal_eval(contents))
    fl.close()

    for i in dicti[x]:
        name.append(i)
    for i in dicti[x].values():
        date.append(i.keys())
        for j in i.values():
            busy.append(j)

    avl_temp = []  # an element of avl[]
    count = 1

    for i in busy[x]:
        tlis = re.split(' - |-|- | -',i)
        st=''
        if count == 1:
            if tlis[0] != '9:00AM':
                st+='9:00AM - '
                st+=tlis[0]
                avl_temp.append(st)
            t1=tlis[1]

        else:
            t2=tlis[0]
            if t1 != t2:
                st+=t1 + ' - ' + t2
                avl_temp.append(st)
            t1=tlis[1]

        count = count + 1    

    if tlis[1] != '5:00PM':
        avl_temp.append(tlis[1]+' - '+'5:00PM')

    avl.append(avl_temp)    


outputFile = open('output.txt', 'w')
outputFile.write('Available slot \n') 
outputFile.close() 

outputFile = open('output.txt', 'a')
for x in range(0,num):
    outputFile.write(name[x]+': ') 
    outputFile.write(str(avl[x])+'\n')
outputFile.write('\n')    


outputFile.write('Slot Duration: '+sys.argv[1]+' hour\n')
boolchk = checkList(list(date))
if boolchk == False:
    outputFile.write('No slot available')
    outputFile.close()
else:
    dur = float(sys.argv[1])
    slots = []  # its each element is a list containing 16 digits (each being 0 or 1) 
    for x in range(0,num):
        slot_temp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # an element of slots[]
        for i in range (0,len(avl[x])):
            tlis = re.split(' - |-|- | -',avl[x][i])
            strt = convert24(tlis[0])
            l = strt.split(':')
            if l[1] == '30':
                l[1] = '50'
            strt =''+l[0]+l[1] 

            end = convert24(tlis[1])
            l = end.split(':')
            if l[1] == '30':
                l[1] = '50'
            end =''+l[0]+l[1]

            for j in range(int(strt), int(end), 50) :
                slot_temp[ int((j-900)/50) ] = 1   # 1 means available from that time till next 30 mins

        slots.append(slot_temp)   
        
    
    count = 0
    y = (int)(dur/0.5)
    for i in range(0,16):
        sum = 0
        for x in range(0,num):
            sum = sum + slots[x][i] 
        if sum == num:    
            count = count + 1
            if count == 1:
                strt = i
        else:
            count = 0     

        if count == y:
            end = i
            break  
    
    if count != y:
        outputFile.write('No slot available')
        outputFile.close()  
    else:
        if strt == 0:
            s1 = '9:00AM'
        if strt == 1:
            s1 = '9:30AM'
        if strt == 2:
            s1 = '10:00AM'    
        if strt == 3:
            s1 = '10:30AM'
        if strt == 4:
            s1 = '11:00AM'
        if strt == 5:
            s1 = '11:30AM'            
        if strt == 6:
            s1 = '12:00PM'
        if strt == 7:
            s1 = '12:30PM'
        if strt == 8:
            s1 = '1:00PM'    
        if strt == 9:
            s1 = '1:30PM'
        if strt == 10:
            s1 = '2:00PM'
        if strt == 11:
            s1 = '2:30PM'    
        if strt == 12:
            s1 = '3:00PM'
        if strt == 13:
            s1 = '3:30PM'
        if strt == 14:
            s1 = '4:00PM'     
        if strt == 15:
            s1 = '4:30PM'       

        if end == 0:
            s2 = '9:30AM'
        if end == 1:
            s2 = '10:00AM'
        if end == 2:
            s2 = '10:30AM'    
        if end == 3:
            s2 = '11:00AM'
        if end == 4:
            s2 = '11:30AM'
        if end == 5:
            s2 = '12:00PM'            
        if end == 6:
            s2 = '12:30PM'
        if end == 7:
            s2 = '1:00PM'
        if end == 8:
            s2 = '1:30PM'    
        if end == 9:
            s2 = '2:00PM'
        if end == 10:
            s2 = '2:30PM'
        if end == 11:
            s2 = '3:00PM'    
        if end == 12:
            s2 = '3:30PM'
        if end == 13:
            s2 = '4:00PM'
        if end == 14:
            s2 = '4:30PM'     
        if end == 15:
            s2 = '5:00PM'  

        slot = s1+' - '+s2
        lis = []
        lis.append(slot)  
        res = {list(date[0])[0] : lis}
        outputFile.write(str(res))
        outputFile.close()       


outputFile = open('output.txt', 'r')
readFile = outputFile.read()
print(readFile)
outputFile.close()














