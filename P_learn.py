import pyfiglet
import os
result = pyfiglet.figlet_format("Learn_Tech") 
print(result)
basic = 30

def basic_commmands():
    aa= False
    global basic
    print("let's learn the basics \n")
    while not aa:
       a=input("try typing 'cd Desktop' for changing the directory \n root@kali:~#")
       if a == "cd Desktop":
          os.chdir("Desktop")
          basic=basic+10
          print("It's good now your score is",basic)
          aa=True
          print("root@kali:~/Desktop#\n")
          aaa=input("now try ls for list directory contents")
          if aaa == "ls":
             os.system("ls")
          else:
             basic=basic-10    
             print("let's try again your score is reduced by 10 score=",basic)  
       
       else:    
          basic=basic-10    
          print("let's try again your score is reduced by 10 score=",basic)   
          aa=False
          if basic == 0:
             print("you loose")
             exit()
             

