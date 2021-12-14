import time , sys , os
os.system("clear")
print("\033[1;96m===Menu Enter===")
print("")
print("\033[1;95m[1] \033[1;92mยิงเบอร์")
print("\033[1;95m[2] \033[1;92mยิงเบอร์ VIP")
print("\033[1;95m[3] \033[1;92mยิงอีเมล์")
print("\033[1;95m[4] \033[1;92mแฮกเกอร์")
print("\033[1;95m[00] \033[1;92mออก")
print("")
print("\033[1;91m[*] By: 2008TH Sorecode Time: 14/12/2021")
print("")
verfly = input("\033[90m> \033[1;97mEnter the attack : \033[1;96m")
if verfly == '1':
	os.system("python aofA.py")
	
if verfly == '2':
	os.system("python aofA.py")
	
if verfly == '3':
	os.system("exit")
	
if verfly == '4':
	os.system("python aofB.py")
	
if verfly == '00':
	print("\033[1;96m2008TH")
	os.system("exit")