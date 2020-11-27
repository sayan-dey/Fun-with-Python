import json 
from array import array

# method to check if all elements of a list are same
def checkList(lst): 
  
    ele = lst[0] 
    chk = True
      
    for item in lst: 
        if ele != item: 
            chk = False
            break; 

    return chk        

def func(level, dicti):

    for x in range(0,num):    
        for lev,i in data.items():
            for j in i:
                for k,v in j.items():
                    if k == 'name' and v == inp[x+1]:
                        level.append(lev)
                        dicti.append(j)
                        break

# Opening JSON file 
f = open('org.json') 
  
data = json.load(f) 
  

inp = input().split()
num = int(inp[0]) # no. of employees whose common leader is to be found


init_inp = []
for x in range(1,num+1):
    init_inp.append(inp[x])  # all input emp ids copied in init_inp list 

level = []   #list of levels of input emp ids
dicti = []   #list of dictionaries of input emp ids

func(level, dicti)


level_i = []  #list storing integer form of elements in level[]
for x in range(0,num):
    level_i.append(int(level[x][1]))


init_level_i = [] 
for x in range(0,num):
    init_level_i.append(level_i[x])  # contents of level_i[] copied in init_level_i[]

min = level_i[0]   # min will store level of highest level emp id among input emp ids 
for x in range(1,num):
    if level_i[x] < min:
        min = level_i[x]


for x in range(0,num):

    while min < level_i[x]:

        count = 0
        for lev,i in data.items():
            if count > 0:
                break
            for j in i:
                if count > 0:
                    break
                for k,v in j.items():
                    if count > 0:
                        break
                    if k == 'name' and v == inp[x+1]:
                        level[x] = lev
                        dicti[x] = j
                        count = count + 1
                        break

        level_i[x] = int(level[x][1])

        if min < level_i[x]:
            count = 0
            for p,q in data.items():
                if count > 0:
                    break
                for i in q:
                    if count > 0:
                        break
                    if i == dicti[x]:
                        for k,v in i.items():
                            if count > 0:
                                break
                            if k == 'parent':
                                inp[x+1] = v
                                level_i[x] = level_i[x] - 1
                                count = count + 1
                                level[x] = 'L'+str(level_i[x])
                                break  

print('\n')
if min == 0:
    print ('Leader not found')
else:
    del inp[0]  #deleting it as it just contains no. of input emp ids
    count1 = 0
    boolchk = checkList(inp)
    while boolchk == False or count1 == 0:
        count1 = 1
        for x in range(0,num):
            count = 0
            for lev,i in data.items():
                if count > 0:
                    break
                for j in i:
                    if count > 0:
                        break
                    for k,v in j.items():
                        if count > 0:
                            break
                        if k == 'name' and v == inp[x]:
                            level[x] = lev
                            dicti[x] = j
                            count = count + 1
                            break

            level_i[x] = int(level[x][1])

            
            count = 0
            for p,q in data.items():
                if count > 0:
                    break
                for i in q:
                    if count > 0:
                        break
                    if i == dicti[x]:
                        for k,v in i.items():
                            if count > 0:
                                break
                            if k == 'parent':
                                inp[x] = v
                                level_i[x] = level_i[x] - 1
                                count = count + 1
                                level[x] = 'L'+str(level_i[x])
                                break                          
        boolchk = checkList(inp)
    
    
    # now, all elements of inp[] are same = empid of common leader
    # also now, all elements of level_i[] are same = level of common leader
    print('common leader: {}'.format(inp[0]))
    for x in range(0,num):
        print('leader {} is {} levels above employee {}'.format(inp[0], abs(level_i[0]-init_level_i[x]), init_inp[x]))
    

f.close() 
  
