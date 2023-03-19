#!/usr/bin/env python
# coding: utf-8

# ## PART A 
# ## 1(a). Write a python program to print the multiplication for the given number

# In[1]:


n=int(input("Enter a number to find its multiple :"))
for i in range(1,11):
    print(n,'*',i,'=',i*n)


# ## 1(b).Write a python program to check whether the given number is prime or not?

# In[2]:


def prime(n):
    for i in range(2,n-1):
        if(n%i==0):
            return False
        return True
n=int(input("Enter a number to find if it is prime or not :"))
if n<=1 or not prime(n):
    print('Given number is not a prime number')
else:
    print('Given number is a prime number')


# ## 1(c). Write a python program to find factorial of the given number?

# In[3]:


while True:
    n=int(input("Enter a number to find its factorial :"))
    if (n>0):
        break
    print('Factorial not possible ,Entered number should be positive')
fac=1
for i in range (1,n+1):
    fac*=i
print('Factorial of ',n,'is ',fac)


# ## 2(a). Write a python program to implement List operations (Nested List, Length,Concatenation, Membership, Iteration, Indexing and Slicing)

# In[4]:


#Nested List
list=['a','b',['cc','dd',['eee',['pppp','rrrr'],'fff']],'g','h']
print(list[2])
print(list[2][2])
print(list[2][2][1])
print(list[2][2][1][0])


# In[5]:


#length
string='Hello World'
print(len(string))


# In[6]:


#Concatenation
s1=input('Enter first String  : ')
s2=input('Enter second String : ')
print('Concatenated String is ',s1+s2)


# In[7]:


#Iteration 
list=[4,7,0,3]
my_iter=iter(list)
print(next(my_iter))
print(next(my_iter))
print(my_iter.__next__())
print(my_iter.__next__())


# In[8]:


#Indexing
cars=['Aston','Audi','McLaren']
for i in range (len(cars)):
    print(cars[i])


# In[9]:


#Slicing
arr='Jyothy Institute of Technology'
print(arr[2:])         #slicing in list with 1 arguments
print(arr[:3])
print(arr[::2])
print(arr[1:4])        #slicing in list with 2 arguments
print(arr[0:10:3])     #slicing in list with 3 arguments
print(arr[::-1])       #reversing an string by slicing


# ## 2(b). Write a python program to implement List methods (Add, Append, Extend & Delete).

# In[10]:


#ADD
cars={'Audi','Honda','BMW'}
cars.add('Hyundai')
print(cars)


# In[11]:


#APPEND
my_list=['Hai','Good']
my_list.append('Morning')
print(my_list)


# In[12]:


#EXTEND
fruits=['Apple','Banana','Cherry']
car=['Ford','BMW','Volvo']
animals=['Dog','Elephant','Lion']
car.extend(fruits)
print('car :',car)
fruits.extend(animals)
print('fruits :',fruits)


# In[13]:


#DELETE
thislist=['Ford','BMW','Volvo']
del thislist[0]
print('thislist :',thislist)


# ## 3. Write a python program to implement simple Chatbot with minimum 10 conversations

# In[14]:


from tkinter import *
root=Tk()
root.title('Chat Bot')
def send():
    send='\nYou->'+e.get()
    txt.insert(END,send)
    user=e.get().lower()
    if(user=='hello'):
        txt.insert(END,'\nBot->Hi')
    elif(user=='hi' or user=='hii'):
        txt.insert(END,'\nBot->Hello')
    elif(user=='how are you'):
        txt.insert(END,'\nBot->Fine! and you')
    elif(user=='fine' or user=='i am good'  or user=='i am doing good'):
        txt.insert(END,'\nBot->Great! How can I help you?')
    elif(user=="what's your name?" ):
        txt.insert(END,'\nBot->My name is ChatBot')
    elif(user=="what's today's weather"):
        txt.insert(END,"\nBot->It's sunny today")
    elif(user=='are you a robot'):
        txt.insert(END,'\nBot->Yes,I am a robot with human feelings')
    elif(user=='bye'):
        txt.insert(END,'\nBot->Have a good day')
    elif(user=='do you have a physical body'):
        txt.insert(END,'\nBot->No')
    else:
        txt.insert(END,"\nBot->Sorry!I didn't gey you")
    e.delete(0,END)
txt=Text(root)
txt.grid(row=0,column=0,columnspan=2)
e=Entry(root,width=100)
e.grid(row=1,column=0)
send=Button(root,text='send',command=send).grid(row=1,column=1)
root.mainloop()


# ## 4. Write a python program to Illustrate Different Set Operations

# In[15]:


E={0,2,4,6,8}
N={1,2,3,4,5}
print('Union of E and N is                :',E|N)     #SET UNION
print('Intersection of E and N is         :',E&N)     #SET INTERSECTION
print('Difference of E and N is           :',E-N)     #SET DIFFERENCE
print('Symmetric Difference of E and N is :',E^N)     #SET SYMMETRIC DIFFERENCE


# ## 5(a). Write a python program to implement a function that counts the number of times a string(s1) occurs in another string(s2)

# In[16]:


def count(sub,s):
    M=len(sub)
    N=len(s)
    res=0
    for i in range(N-M+1):
        j=0
        while (j<M):
            if (s[i+j]!=sub[j]):
                break
            j+=1
        if(j==M):
            res+=1
            j=0
    return res
string='asdffghasdkljasdf'
substring='asdf'
print("Count :",count(substring,string))


# ## 5(b). Write a program to illustrate Dictionary operations([],in,traversal)and methods: keys(),values(),items()

# In[17]:


print('-----------------KEYS()-----------------------')
number={1:'One',2:'Two',3:'Three'}
dict_keys=number.keys()
print(dict_keys)
print('-----------------ITEMS()----------------------')
marks={'Physics':67,'Marks':87}
print(marks.items())
print(marks.keys())
print('-----------------VALUES()---------------------')
print(marks.values())


# # PART B
# ## 1.Implement and Demonstrate Depth First Search Algorithm on Water Jug Problem

# In[3]:


from collections import defaultdict
visited=defaultdict(lambda:False)
j1,j2,l=0,0,0
def water_jug_problem(x,y):
    global j1,j2,l
    if(x==l and y==0) and (x==0 and y==l):
        print('(',x,',',y,')',sep=" ")
        return True
    if visited[(x,y)]==False:
        print('(',x,',',y,')',sep=" ")
        visited[(x,y)]=True
        return( water_jug_problem(0,y)  or water_jug_problem(x,0) or
                water_jug_problem(j1,y) or water_jug_problem(x,j2)or
                water_jug_problem(x+min(y,(j1-x)),y-min(y,(j1-x)))or
                water_jug_problem(x-min(x,(j2-y)),y+min(x,(j2-y))))
    else:
        return False

    

j1,j2,l=5,3,4
print("path is as follows :")
water_jug_problem(3,0)


# ## 2. Implement and Demonstrate Best First Search Algorithm on any AI problem

# In[19]:


class Graph:
    def __init__(self,adjac_lis):
        self.adjac_lis = adjac_lis
    def get_neighbours(self,v):
        return self.adjac_lis[v]
    def h(self,n):
        H={'A':1,'B':1, 'C':1,'D':1}
        return H[n]
    def a_star_algorithm(self,start,stop):
        open_lst = set([start])
        closed_lst = set([])
        dist ={}
        dist[start] = 0
        prenode ={}
        prenode[start] =start
        while len(open_lst)>0:
            n = None
            for v in open_lst:
                if n==None or dist[v]+self.h(v)<dist[n]+self.h(n):
                    n=v;
            if n==None:
                print("path doesnot exist")
                return None
            if n==stop:
                reconst_path=[]
                while prenode[n]!=n:
                    reconst_path.append(n)
                    n = prenode[n]
                reconst_path.append(start)
                reconst_path.reverse()
                print("path found:{}".format(reconst_path))
                return reconst_path
            for (m,weight) in self.get_neighbours(n):
                if m not in open_lst and m not in closed_lst:
                    open_lst.add(m)
                    prenode[m] = n
                    dist[m] = dist[n]+weight
                else:
                    if dist[m]>dist[n]+weight:
                        dist[m] = dist[n]+weight
                        prenode[m]=n
                        if m in closed_lst:
                            closed_lst.remove(m)
                            open_lst.add(m)
            open_lst.remove(n)
            closed_lst.add(n)
        print("Path doesnot exist")
        return None
adjac_lis ={'A':[('B',1),('C',3),('D',7)],'B':[('D',5)],'C':[('D',12)]}
graph1=Graph(adjac_lis)
graph1.a_star_algorithm('A', 'D')


# ## 3. Implement AO* Search algorithm

# In[20]:


from heuristicsearch.ao_star import AOStar
print('Graph-A')
adj_list={
    'A':[[('C',2),('D',3)],[('B',4)]],
    'B':[[('E',1)],[('F',4)]],
    'C':[[('G',3)],[('H',2),('I',3)]],
    'D':[[('J',3)]]
}
Heuristic={
    'A': -1,
    'B': 4,
    'C': 2,
    'D': 3,
    'E': 6,
    'F': 8,
    'G': 2,
    'H': 0,
    'I': 0,
    'J': 0
}
graph=AOStar(adj_list,Heuristic,'A')
graph.applyAOStar()


# ## 4. Solve 8-Queens Problem with suitable assumptions

# In[21]:


print ("Enter the number of queens")
N = int(input())

board = [[0]*N for _ in range(N)]

def attack(i, j):
    for k in range(0,N):
        if board[i][k]==1 or board[k][j]==1:
            return True
    for k in range(0,N):
        for l in range(0,N):
            if (k+l==i+j) or (k-l==i-j):
                if board[k][l]==1:
                    return True
    return False

def N_queens(n):
    if n==0:
        return True
    for i in range(0,N):
        for j in range(0,N):
            if (not(attack(i,j))) and (board[i][j]!=1):
                board[i][j] = 1
                if N_queens(n-1)==True:
                    return True
                board[i][j] = 0
    return False

N_queens(N)
for i in board:
    print (i)


# ## 5. Implementation of TSP using heuristic approach

# In[4]:


from sys import maxsize
from itertools import permutations
V = 4
# implementation of traveling Salesman Problem
def travellingSalesmanProblem(graph, s):
 # store all vertex apart from source vertex
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)
 # store minimum weight
    min_path = maxsize
    next_permutation=permutations(vertex)
    for i in next_permutation:
        current_pathweight = 0
 # compute current path weight
    k = s
    for j in i:
        current_pathweight += graph[k][j]
    k = j
    current_pathweight += graph[k][s]
 # update minimum
    min_path = min(min_path, current_pathweight)
    return min_path

# Driver Code
if __name__ == "__main__":
 # matrix representation of graph
 graph = [[0, 10, 15, 20], 
          [10, 0, 35, 25],
          [15, 35, 0, 30], 
          [20, 25, 30, 0]]
 s = 0
 print(travellingSalesmanProblem(graph, s))


# ## 6. Implementation of the problem solving strategies: either using Forward Chaining or Backward Chaining

# In[2]:


factskw=[['croaks', 'frog'],['eats flies','frog'],['frog','green'],['chirps','canary'],['sing','canary'],['canary','yellow']]
def check(str, factOb):
    facts=[]
    flag=True
    while flag==True:
        flag=False
        for txt in str:
            for A1 in factOb:
                if A1[0] == txt:
                    tmp = [txt,A1[1]]
                    if not tmp in facts:
                        facts += [tmp]
                        str += A1[1]
                        flag = True
    return facts
result = check(['sing', 'canary'], factskw)
print(result)


# In[24]:


class Rule:
    def __init__(self, conclusion, *premises):
        self.conclusion = conclusion
        self.premises = premises
def backward_chaining(goal, rules):
    agenda = [goal]
    while agenda:
        goal = agenda.pop(0)
        print("Processing goal:", goal)
        found = False
        for rule in rules:
            if goal in rule.premises:
                print("Found a rule with goal in its Chaining:")
                print(rule.conclusion, rule.premises, sep='->')
                found = True
                for premise in rule.premises:
                    if premise not in agenda:
                        agenda.append(premise)
        if not found:
            print("No rules found for:", goal)
            return False
        return True
# Example usage
rules = [Rule("A", "C"), Rule("B", "C"), Rule("C", "D")]
backward_chaining("C", rules)
# Output: True


# ## 7. Implement resolution principle on FOPL related problems

# In[25]:


import re
def dnf(formula): 
    if re.fullmatch(r'[A-Z]|~[A-Z]|()""', formula):
        return formula
    if 'and' in formula or 'or' in formula:
        parts = re.split(r'(?<=[^\w])or(?=[^\w])|(?<=[^\w])and(?=[^\w])', formula)
        print(f"parts: {parts}")
        dnf_parts = [dnf(part) for part in parts]
        print(f"dnf_parts: {dnf_parts}")
        if 'or' in formula:
            return " or ".join(parts)
        elif 'and' in formula:
            return " and ".join(parts)
# Example usage
formula = "(A and B) or B"
dnf_formula = dnf(formula)
print(dnf_formula) # Outputs: "A or C or B or D or"


# In[20]:


pip install cfn_resource


# In[13]:


pip install cnf


# In[3]:


import re
def cnf(formula):
    if re.fullmatch(r'[A-Z]|~[A-Z]', formula):
        return formula
    if 'and' in formula and 'or' in formula:
        parts = re.split(r'(?<=\()or(?=\))|(?<=\()and(?=\))', formula)
        if 'and' in formula:
            return 'or '.join(parts)
        elif 'or' in formula:
            return 'and '.join(parts)
# Example usage
formula = "(A and B) and
(C and D)"
cnf_formula = cnf(formula)
print(cnf_formula) # Outputs: "A and B or C and D or"


# ## 8. Implement any Game and demonstrate the Game playing strategies

# In[27]:


#Tic-tac Program
board = [[" " for _ in range(3)] for _ in range(3)]

def draw_board():
    print("  0 1 2")
    for i, row in enumerate(board):
        print(i, " ".join(row))

def get_move(player):
    while True:
        col = input(f"{player}, enter column: ")
        row = input(f"{player}, enter row: ")
        if col.isdigit() and row.isdigit():
            col, row = int(col), int(row)
            if 0 <= col < 3 and 0 <= row < 3:
                if board[row][col] == " ":
                    board[row][col] = player
                    return
                else:
                    print("That space is already occupied. Try again.")
            else:
                print("Invalid move. Try again.")
        else:
            print("Invalid input. Try again.")

def has_winner():
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True
        if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
            return True
        if board[2][0] == board[1][1] == board[0][2] and board[2][0] != " ":
            return True
    return False

def main():
    while True:
        draw_board()
        get_move("X")
        if has_winner():
            print("X wins!")
            break
        draw_board()
        get_move("O")
        if has_winner():
            print("O wins!")
            break

main()


# In[ ]:




