# Import modules
import time
from pyfiglet import figlet_format
from termcolor import colored
import os
import system

# Banner and Signature
os.system('clear')
print(colored(figlet_format('DeathSeraph'), color='magenta'))
print('By: Sh0gun')

# Workflow
url = input ('Enter target: ')
menu = int(input('''Enter option: 
[1] - Recon + Varredura de XSS em subdomínios
[2] - Recon + Mineração de XSS em URLs
[3] - Recon + Varredura Total em subdomínios
[4] - Recon + Análise de vulnerabilidades
[5] - Recon + Análise de CWEs
[6] - Recon + Varredura Total em URLs
[0] - Exit

>>> '''))

if menu == 1:
    os.system('clear')
    os.system('bash recon.sh {}'.format(url))
    os.system('./subs.sh {}'.format(url))
    os.system('bash XSScrapper.sh subs.txt')
if menu == 2:
    os.system('clear')
    os.system('./recon.sh {} '.format(url))
    os.system('./XSScrapper.sh actives.txt')
if menu == 3:
    os.system('clear')
    os.system('./recon.sh {} '.format(url))
    os.system('bash subs.sh {}'.format(url))
    os.system('nuclei -l subs.txt')
if menu == 4:
   os.system('clear')
   os.system('./recon.sh {} '.format(url))
   os.system('bash subs.sh {}'.format(url))
   os.system('nuclei -l subs.txt -t nuclei-templates/vulnerabilities')
   os.system('./recon.sh {}'.format(url))
   os.system('bash subs.sh {}'.format(url))
   os.system('nuclei -l subs.txt -t nuclei-templates/cwes')
   os.system('./recon.sh {}'.format(url))
   os.system('bash subs.sh {}'.format(url))
   os.system('nuclei -l subs.txt -t nuclei-templates/exposures')
   os.system('./recon.sh {}'.format(url))
   os.system('bash subs.sh {}'.format(url))
   os.system('nuclei -l subs.txt -t nuclei-templates/takeovers')
   os.system('./recon.sh {}'.format(url))
   os.system('bash subs.sh {}'.format(url))
   os.system('nuclei -l subs.txt -t nuclei-templates/misconfiguration')
if menu == 5:
   os.system('clear')
   os.system('./recon.sh {} '.format(url))
   os.system('bash subs.sh {}'.format(url))
   os.system('nuclei -l subs.txt -t nuclei-templates/vulnerabilities')
   os.system('./recon.sh {}'.format(url))
   os.system('bash subs.sh {}'.format(url))
   os.system('nuclei -l subs.txt -t nuclei-templates/cwes')
   os.system('./recon.sh {}'.format(url))
   os.system('bash subs.sh {}'.format(url))
   os.system('nuclei -l subs.txt -t nuclei-templates/exposures')
   os.system('./recon.sh {}'.format(url))
   os.system('bash subs.sh {}'.format(url))
   os.system('nuclei -l subs.txt -t nuclei-templates/takeovers')
   os.system('./recon.sh {}'.format(url))
   os.system('bash subs.sh {}'.format(url))
   os.system('nuclei -l subs.txt -t nuclei-templates/misconfiguration')
if menu == 6:
   os.system('clear')
   os.system('./recon.sh {} '.format(url))
   os.system('bash subs.sh {}'.format(url))
   os.system('nuclei -l actives.txt -t nuclei-templates/vulnerabilities')
   os.system('./recon.sh {}'.format(url))
   os.system('bash subs.sh {}'.format(url))
   os.system('nuclei -l actives.txt -t nuclei-templates/cwes')
   os.system('./recon.sh {}'.format(url))
   os.system('bash subs.sh {}'.format(url))
   os.system('nuclei -l actives.txt -t nuclei-templates/exposures')
   os.system('bash recon.sh {}'.format(url))
   os.system(' ./subs.sh {}'.format(url))
   os.system('nuclei -l actives.txt -t nuclei-templates/takeovers')
   os.system('bash recon.sh {}'.format(url))
   os.system(' ./subs.sh {}'.format(url))
   os.system('nuclei -l actives.txt -t nuclei-templates/misconfiguration')
if menu == 0:
    exit()
