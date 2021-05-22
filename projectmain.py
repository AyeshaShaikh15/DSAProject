class Node:
   def __init__(self,course_code='NA',course_name="NA",credit_hours=0.0):
       self.course_code=course_code
       self.course_name=course_name
       self.credit_hours=credit_hours
       self.next=None

class LinkedList: #class that creates the linked list
   def __init__(self):
       self.headval=None
       self.current=None

   def addNode(self,node): #creates the head node and adds data to the link list changing the nodes to the next node

       if(self.headval==None):
           self.headval=node
           self.current=node
       else:
           self.current.next=node
           self.current=node


   def printlist(self): #initially prints the linked list data showing courses
       print("Courses Offered:\n")
       current=self.headval
       print("Course Code".center(40," "),end="")
       print('|'+"Course Name".center(40," "),end="")
       print('|'+"Credit Hours ".center(40," "))

       while(current!=None):
           print(str(current.course_code).center(40," "),end="")
           print('|'+str(current.course_name).center(40," "),end="")
           print('|'+str(current.credit_hours).center(40," "))
           current=current.next

   def findcourses(self,search): #searches the course in the linked list
       current=self.headval
       try:
           search=(search)
           while(current!=None):
               if(current.course_code==search):
                   return current
               current=current.next

       except Exception as e:
           while(current!=None):
               if(current.course_name==search):
                   return current
               current=current.next
       return None


def quicksort(lst, num): #sorts the new list according to credit hours or course names
    if num == '1':

        for i in lst:
            i[2]=float(i[2])

        length = len(lst)
        if length <=1:
            return lst
        else:
            pivot = lst.pop(0)
            pivotcredit = pivot[2]
        i_greater = []
        i_lower = []
        for i in lst:
            if i[2] > pivotcredit:
                i_greater.append(i)
            else:
                i_lower.append(i)
        return quicksort(i_lower, num) + [pivot] + quicksort(i_greater, num)
    elif num =='2':
    
        length = len(lst)
        if length <=1:
            return lst
        else:
            pivot = lst.pop(0)
            pivotcredit = pivot[1]
        i_greater = []
        i_lower = []
        for i in lst:
            if i[1] > pivotcredit:
                i_greater.append(i)
            else:
                i_lower.append(i)
        return quicksort(i_lower, num) + [pivot] + quicksort(i_greater, num)

def printsortedlist(lst):   #prints the sorted list in the same manner as it was initially 
    print("Courses Offered:\n")
       
    print("Course Code".center(40," "),end="")
    print('|'+"Course Name".center(40," "),end="")
    print('|'+"Credit Hours".center(40," "))

    for i in lst:
        print(str(i[0]).center(40," "),end="")
        print('|'+str(i[1]).center(40," "),end="")
        print('|'+str(i[2]).center(40," "))

lst = []               #reads the file and adds courses into a list 
file=open("data.txt","r")
produced_list=LinkedList()
for line in file:
   line=line.replace("\n","")
   line=line.split(" ")
   lst.append(line)

file=open("data.txt","r")   # reads file and addds courses into a linked list
produced_list=LinkedList()
for line in file:
   line=line.replace("\n","")
   line=line.split(" ")
   
   produced_list.addNode(Node((line[0]),line[1],float(line[2])))
produced_list.printlist()
print("To see the above courses sorted according to credit hours(ascending) enter 1: ")
print("To see the above courses sorted according to course names(alphabetically) enter 2: ")
print('To skip this part, type skip:')
x = input()
if x == '1':
    printsortedlist(quicksort(lst, '1'))
elif x == "2":
    printsortedlist(quicksort(lst, '2'))
elif x == 'skip':
    pass
print("Enter the course codes in a new line type quit to create cart:")
purchased_list=LinkedList()
while(True):
   n=input()
   if(n=="quit"):
       break
   else:
       product=produced_list.findcourses(n)   #checks if course is available 
       if(product==None):
           print("Course not found")
       else:
           purchased_list.addNode(Node(product.course_code,product.course_name,product.credit_hours))

print("\nCart:")
print("Courses".ljust(40," "),end="")
print("Credit Hours".ljust(40," "))
current=purchased_list.headval
total_credit_hours=0
while(current!=None):
    
    total_credit_hours+=current.credit_hours    #gives the sum of credit hours 
    
    print(current.course_name.ljust(40," "),end="")
    print(str(current.credit_hours).ljust(40," "))
    current=current.next
print("")
if total_credit_hours>40:
    print('Warning, your credit hours have exceeded the limit!')
print("Total credit hours:".ljust(40," "),end="")
print(str(total_credit_hours).ljust(40," "))
