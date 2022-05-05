
import os

mk = "sudo mkdir $HOME/axosecurity"


knock = "sudo subfinder -d domain | sudo tee /home/axosolaman/axosecurity/domain_subfinder.log"

domain = input("TARGET DOMAIN \n")

print(knock)

#path = input("GIVE A PATH FOR SAVEING FILES\n")

os.system(mk)



#os.system("go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest")

os.system("sudo subfinder -d " + domain + " | sudo tee $HOME/axosecurity/" + domain + "_subfinder.log")

os.system("sudo ls $HOME/axosecurity | lolcat")



















