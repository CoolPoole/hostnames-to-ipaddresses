# Python script to take hostnames as input and produce their associated IP address(es)
# Author: JustCooLpOOLe
# Version: 1.0
# License: (o^o)

# module import section
import socket
import time
import pyfiglet

# global variable declaration
again = 'Y'
date = time.strftime("%Y%m%d-%H%M%S")
file_out = ("hostnames-to-ipaddress-output-" + date + ".txt")

# methods section
def single_input():
    single_domain = input("\nPlease enter your domain: ")
    print("\nLooking up", single_domain, "...\n")
    time.sleep(1)

    try:
        ip_address = socket.gethostbyname_ex(single_domain)
        print("The IP for", single_domain, "is", ip_address, "\n")
    except socket.gaierror:
        print("Your domain does not exist.")

def file_input():
    filename = input("\nWhat is your filename to be read: ")

    try:
        
        # open() function to read filename variable
        with open(filename, "r") as ins:
            print("\nImporting file(s)...\n")
            time.sleep(3)

            print(" ")

            outF = open(file_out, "w")
            for line in ins:
                
                try:
                    ip_address = socket.gethostbyname_ex(line.strip()) # strip() will strip any trailing or leading blank spaces
                    print("The IP for", line, "is", ip_address, "\n")
                    outF.write(str(ip_address))
                    outF.write("\n")
                except socket.gaierror:
                    print("Domain does not exist.")

            outF.close()

        print("\nNote: Your output was written to", file_out, "\n")
    except IOError:
        print("\nYour file does not exist. You may need to specify the full path.")


def quitter():
    ascii_closing_banner = pyfiglet.figlet_format("Smell Ya Later!\n")
    print(ascii_closing_banner)
    time.sleep(3)

# title header
ascii_banner = pyfiglet.figlet_format("\nLet's Convert Hostnames to IP Addresses!")
print(ascii_banner)

while (again != 'N'):
    
    try:
        choice = int(input("\nEnter \n (1) for single domain\n (2) for a file\n (3) to quit \r\n\n Choice: "))
    except ValueError:
        print("Invalid Choice!")
        break

    if (choice == 1):
        single_input()
    elif (choice == 2):
        file_input()
    else:
        quitter()
        break

    again = input("\nWould you like to look up more? (Y/N) ")

else:
    quitter()



              

