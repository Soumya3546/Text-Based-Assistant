import pyttsx3
import os
pyttsx3.speak("Welcome to the world of programming")

print()
print("Press 1: to open chrome")
print("Press 2: to open notepad")
print("Press 3: to open wmplayer")
print()

print('Enter ur choice of program:',end=' ')
x=input()
print(x)
#os.system(p)

if int(x)==1:
  os.system('start chrome')
elif int(x)==2:
  os.system('notepad')
elif int(x)==3:
  os.system('start wmplayer')
else:
  print('dont support')