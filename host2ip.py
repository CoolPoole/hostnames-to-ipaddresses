# Python script to take hostnames as input and produce their associated IP address(es)
# Author: JustCooLpOOLe
# Version: 1.0
# License: (o^o)

# module import section
import socket
import time
from termcolor import colored
import argparse

# global variable declaration
date = time.strftime("%Y%m%d-%H%M%S")
file_out = ("domain2ipaddr-output-" + date + ".txt")

# argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-type","--type",required=True,help="Specifies the lookup type.  Type 1 for single domain, 2 for a file.")
ap.add_argument("-domain","--domain",required=False,help="Domain for lookup.")
ap.add_argument("-file","--file",required=False,help="File with multiple domains for lookup.")
ap.add_argument("-write","--write",required=False,help="Specifies writing output to a file. Y = Yes")
args = vars(ap.parse_args())

# functions
def single_lookup(domain):
    try:
        ip_address = socket.gethostbyname_ex(domain)
        print(colored(domain, 'blue'), "contains the following IP(s):", colored(ip_address[2], 'green'))
    except socket.gaierror:
        print(colored("Domain does not exist.",'red'))

def file_lookup(filename,writeout):
    try:
        with open(filename, "r") as ins:

            print(colored("[*] Importing File...", 'magenta'))

            if (writeout == "Y"):
                outF = open(file_out, "w")

                for line in ins:
                    try:
                        ip_address = socket.gethostbyname_ex(line.strip())
                        output = str(line + "contains the following IP(s):" + str(ip_address[2]))
                        outF.write(output)
                        outF.write("\n")
                    except socket.gaierror:
                        print(colored("Domain does not exist.",'red'))

                outF.close()

                print(colored("[-] Output file:",'magenta'), colored(file_out,'green'))
            else:
                print(colored("[-] Output...", 'cyan'))
                for line in ins:
                    try:
                        ip_address = socket.gethostbyname_ex(line.strip())
                        print(colored(line, 'blue'), "contains the following IP(s):", colored(ip_address[2], 'green'))
                    except socket.gaierror:
                        print(colored("Domain does not exist.",'red'))
    except IOError:
        print(colored("\nYour file does not exist. You may need to specify the full path.",'red'))
        
# main
choice = args['type']
domain = args['domain']
filename = args['file']
writeout = args['write']

if (choice == '1'):
    single_lookup(domain)
elif (choice == '2'):
    file_lookup(filename,writeout)

 

