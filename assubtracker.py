
import os

print(""" 
	   
	   _    __  _____  ____  _____ ____ _   _ ____  ___ _______   __
	   / \   \ \/ / _ \/ ___|| ____/ ___| | | |  _ \|_ _|_   _\ \ / /
	  / _ \   \  / | | \___ \|  _|| |   | | | | |_) || |  | |  \ V / 
	 / ___ \  /  \ |_| |___) | |__| |___| |_| |  _ < | |  | |   | |  
	/_/   \_\/_/\_\___/|____/|_____\____|\___/|_| \_\___| |_|   |_|  


	""")


print("SUBDOMAIN ENUMARATION AUTOMATION\nCREATED BY AXOSOLAMAN")


mk = "sudo mkdir $HOME/axosecurity"


knock = "knockpy domain | sudo tee /home/axosolaman/axosecurity/domain_knock.log"

domain = input("TARGET DOMAIN \n")

print(knock)

#path = input("GIVE A PATH FOR SAVEING FILES\n")

os.system(mk)



os.system("sudo apt install knockpy")

os.system("sudo knockpy " + domain + " | sudo tee $HOME/axosecurity/" + domain)

os.system("sudo ls $HOME/axosecurity | lolcat")

knock1 = "sudo subfinder -d domain | sudo tee /home/axosolaman/axosecurity/domain_subfinder.log"

#domain1 = input("TARGET DOMAIN \n")

print(knock1)

#path = input("GIVE A PATH FOR SAVEING FILES\n")

os.system(mk)



#os.system("go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest")



os.system("sudo subfinder -d " + domain + " | sudo tee $HOME/axosecurity/" + domain + "_subfinder.log")

os.system("sudo ls $HOME/axosecurity | lolcat")


#Automation of webapp pentesting

os.system("sudo cat $HOME/axosecurity/" + domain + "| sudo httprobe | sudo tee $HOME/axosecurity/" + domain + "_fnknock.log")



os.system("sudo cat $HOME/axosecurity/" + domain + "_subfinder.log " + "| sudo httprobe | sudo tee $HOME/axosecurity/" + domain + "_fn.log")












