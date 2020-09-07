import time
from os import system, name,getcwd
from playsound import playsound
from random import shuffle
import pickle


#ideas
#make prayer list on a file so can be loaded

#variables
time_length=25

parent_directory=getcwd()
print(parent_directory)
#opening file
if name=='nt':
    File = open(parent_directory+'\\todolist','rb')
else:
    File = open(parent_directory+'/todolist','rb')
db=pickle.load(File)
todolist=db['todolist']
File.close()
# define our clear function 
def clear(): 
      # for windows 
    if name == 'nt': 
        _ = system('cls') 
      # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')


def Lp():
    print('Ready to work!\n')
    time.sleep(2)


def s(todolist,time_length):
    i=0
    for i in range(0,time_length):
        for j in range(0,120):
                clear()
                print(str(i)+'/'+str(time_length))
                print('\n['+'#'*(i-1)+'\\'+'-'*(time_length-i)+']')
                time.sleep(0.125)
                clear()
                print(str(i)+'/'+str(time_length))
                print('\n['+'#'*(i-1)+'|'+'-'*(time_length-i)+']')
                time.sleep(0.125)
                clear()
                print(str(i)+'/'+str(time_length))
                print('\n['+'#'*(i-1)+'/'+'-'*(time_length-i)+']')
                time.sleep(0.125)
                clear()
                print(str(i)+'/'+str(time_length))
                print('\n['+'#'*(i-1)+'-'+'-'*(time_length-i)+']')
                time.sleep(0.125)

    clear()
    print('\nDone!')
    print('\n['+'#'*(i+1)+']')
    time.sleep(0.5)
    clear()
    if name=='nt':
        soundpath=parent_directory+'\\Reverie.wav'
    else:
        soundpath=parent_directory+'/Reverie.wav'
    shuffle(todolist)
    print('\nReady for '+todolist[0])  
    playsound(soundpath)
    ip2=input('\nDo you want to continue(Y/N)')
    if ip2=='y' or ip2=='Y':
        s(todolist,time_length)
    elif ip2=='n' or ip2=='N':
        menu(todolist,time_length)
    else:
        clear()
        print('\nYou have entered an invalid input redirecting to main menu')
        time.sleep(2)
    
    menu(todolist, time_length)     

def e(todolist,time_length):
    clear()
    ip2=input('''\n Enter an option
            \n1:add items
            \n2:remove items
            \n3:delete list
            \n4:view list
            \n5:return to previous menu
            \n6:quit
            \n''')
    if ip2=='1':
        clear()
        newEl=input('\nEnter new element:')
        todolist+=[newEl]
        
    elif ip2=='2':
        i=0
        clear()
        
        for i in range(0,len(todolist)):
            print('\n'+str(i)+' : '+todolist[i])
        ip3=int(input('\nEnter index which you want to delete'))
        del(todolist[ip3])
    elif ip2=='3':
        todolist=[]
    elif ip2=='4':
        i=0
        clear()
        for i in range(0,len(todolist)):
            print('\n'+str(i)+' : '+todolist[i])
        input('\n Type Enter to continue')
    elif ip2=='5':
        clear()
        menu(todolist, time_length)
    elif ip2=='6':
        exit()
    else:
        print('You have entered an invalid input try again')
        time.sleep(2)
        clear()
        menu(todolist, time_length)
    if name=='nt':
        File = open(parent_directory+'\\todolistwin','wb')
    else:
        File = open(parent_directory+'/todolist','wb')
    pickle.dump({'todolist':todolist},File)
    File.close()
    e(todolist,time_length)


def menu(todolist,time_length):
    clear()
    ip=input('''\n Enter an option
            \ns:Start
            \ne:Edit todo list
            \nl:change time duration:
            \nq:to Quit
            \n''')
    if ip=='s':
        s(todolist,time_length)    
    elif ip=='e':
        e(todolist,time_length)
    elif ip=='l':
        clear()
        time_length=int(input('\nEnter the no. of minutes you want the timer to last'))
        menu(todolist, time_length)
    elif ip=='q':
        exit(0)
    else:
        clear()
        print('\nYou have entered an inalid input please try again')
        menu(todolist, time_length)


Lp()
menu(todolist,time_length)

