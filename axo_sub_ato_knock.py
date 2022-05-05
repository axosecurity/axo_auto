
import os

mk = "sudo mkdir $HOME/axosecurity"


knock = "knockpy domain | sudo tee /home/axosolaman/axosecurity/domain_knock.log"

domain = input("TARGET DOMAIN \n")

print(knock)


#path = input("GIVE A PATH FOR SAVEING FILES\n")

os.system(mk)



os.system("sudo apt install knockpy")

os.system("sudo knockpy " + domain + " | sudo tee $HOME/axosecurity/" + domain)

os.system("sudo ls $HOME/axosecurity | lolcat")

print("Result has been saved in $HOME/axosecurity ")

input()



















