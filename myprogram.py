import pyttsx3
import os
pyttsx3.speak("Welcome to the world of programming")

print()
print("What is ur requirement dude..chat with me how can i help u? ")
print()

x=input()
#print(x)
#os.system(p)

if (("run" in x) or ("launch" in x) or ("open" in x) or ("execute" in x)) and ("chrome" in x):
  os.system('start chrome')
elif (("run" in x) or ("launch" in x) or ("open" in x) or ("execute" in x)) and ("notepad" in x):
  os.system('notepad')
elif (("run" in x) or ("launch" in x) or ("open" in x) or ("execute" in x)) and ("wmplayer" in x):
  os.system('start wmplayer')
else:
  print('dont support')