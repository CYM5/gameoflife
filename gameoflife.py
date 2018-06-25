import os
import random
import time
def init_tab(rows,col):
    '''
    Initialize the first array
    @param1 int : The number of row
    @param2 int : The number of column

    Return the firt array. it is surrounded by zero
    '''
    tab=[]
    for i in range(rows+2):
        tab_row=[]
        if(i==0 or i==rows+1):
            tmp=col+2
            tab.append([0]*tmp)
        else:
            for j in range(col+2):
                if(j==0 or j==col+1):
                    tab_row+=[0]
                elif random.randint(0,5)==0:
                    tab_row+=[1]
                else:
                    tab_row+=[0]
            tab+=[tab_row]
    return tab

def print_life(row,col,tab):
    '''
    Print the array
    @param1 int : Number of row
    @param2 int : Number of column
    @param3 list : The array to print
    '''
    life=""
    row=row+2
    col=col+2
    for i in range(row):
        for j in range(col):
            if tab[i][j]==0:
                life+="  "
            else:
                life+="O "
        life+="\n"
    print(life)

def evolve(row,col,tab):
    '''
    Function wich make evolve the game
    @param1 int : Number of row
    @param2 int : number of column
    @param3 list : the array of the game

    Return the new array 

    In this function we use a array surrounded by zero, so the new array
    made as the same way
    '''
    new_tab=[]
    tmp=col+2
    new_tab.append([0]*tmp)
    for i in range(1,row+1):
        new_tab_row=[]
        for j in range(1,col+1):
            #How many cells are alive near the current cell
            sum_life=0
            if(j==1):
                new_tab_row+=[0]
            else:
                for k in [i-1,i,i+1]:
                    for l in [j-1,j,j+1]:
                        if(k==i and l==j):
                            continue #Don't count the current cell
                        else:
                            sum_life+=tab[k][l]

            # Apply the dead or alive rules
            if(tab[i][j]==0 and sum_life==3):
                new_tab_row+=[1]
            elif(tab[i][j]==1):
                if(sum_life==2 or sum_life==3):
                    new_tab_row+=[1]
                else:
                    new_tab_row+=[0]
            else:
                new_tab_row+=[0]
            if(j==col):
                new_tab_row+=[0]
        new_tab+=[new_tab_row]
    new_tab.append([0]*tmp)
    return new_tab


os.system("clear")

row=int(input("How many rows -> "))
col=int(input("How many columns -> "))
time=int(input("How many time -> "))
tab=init_tab(row,col)
for t in range(time):
    print_life(row,col,tab)
    tab=evolve(row,col,tab)
    os.system("sleep 2")
    os.system("clear")
