import requests
from bs4 import BeautifulSoup
import os ,sys
import argparse
import bcolors


def banner():
    print("""

            ██╗░░██╗██╗██████╗░██████╗░███████╗███╗░░██╗░░░░░░███████╗██╗░░██╗████████╗██████╗░░█████╗░░█████╗░████████╗███████╗██████╗░
            ██║░░██║██║██╔══██╗██╔══██╗██╔════╝████╗░██║░░░░░░██╔════╝╚██╗██╔╝╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
            ███████║██║██║░░██║██║░░██║█████╗░░██╔██╗██║█████╗█████╗░░░╚███╔╝░░░░██║░░░██████╔╝███████║██║░░╚═╝░░░██║░░░█████╗░░██████╔╝
            ██╔══██║██║██║░░██║██║░░██║██╔══╝░░██║╚████║╚════╝██╔══╝░░░██╔██╗░░░░██║░░░██╔══██╗██╔══██║██║░░██╗░░░██║░░░██╔══╝░░██╔══██╗
            ██║░░██║██║██████╔╝██████╔╝███████╗██║░╚███║░░░░░░███████╗██╔╝╚██╗░░░██║░░░██║░░██║██║░░██║╚█████╔╝░░░██║░░░███████╗██║░░██║
            ╚═╝░░╚═╝╚═╝╚═════╝░╚═════╝░╚══════╝╚═╝░░╚══╝░░░░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝                                                                                 
                                                                                                                             Code by NG          
              """)

if len(sys.argv) > 1:
    banner()
    if(sys.argv[1] == '-u'):
        try:
          input_url = sys.argv[2]
          if(os.path.exists(input_url)==True):
           input_file = open(input_url,'r')
           line= input_file.readlines()
           for text in line:
               lines = text.rstrip()
               print(bcolors.OKMSG + 'URL:' + lines)
               parser = argparse.ArgumentParser()
               parser.add_argument("-u", required=True)
               args = parser.parse_args()
               file_text = requests.get(lines).text
               try:
                      input_fileSoup= BeautifulSoup(file_text,'html.parser')
                      for form_tag in input_fileSoup.find_all('form'):
                           hidden_tag = form_tag.find(type="hidden")
                           print(bcolors.OKMSG+ 'Hidden Values exist in the given URL:: ',hidden_tag)
                           print(bcolors.OKMSG + 'Value:',hidden_tag.get('value'))
               except:
                   print(bcolors.ERRMSG + 'URL not valid')
          elif (os.path.exists(input_url) == False):
                       print(bcolors.OKMSG + 'URL:' + input_url)
                       file_text = requests.get(input_url).text
                       parser = argparse.ArgumentParser()
                       parser.add_argument("-u", required=True)
                       args = parser.parse_args()
                       try:
                           input_fileSoup = BeautifulSoup(file_text, 'html.parser')
                           for form_tag in input_fileSoup.find_all('form'):
                               hidden_tag = form_tag.find(type="hidden")
                               print(bcolors.OKMSG + 'Hidden Values exist in the given URL:: ', hidden_tag)
                               print(bcolors.OKMSG + 'Value:', hidden_tag.get('value'))
                       except:
                           print(bcolors.ERRMSG + 'Please enter valid url')

        except:
             print('Please enter python hidden.py -u <URL>')

    elif ((sys.argv[1] == '-h') | (sys.argv[1] == '--help')):
        print(bcolors.BOLD + 'usage: hidden.py [-h] -u URL' '\n' 'OPTIONS:' '\n' '-h,--help    '
                             'show this help message and exit' '\n''-u Url,   --url URL For which you want to search hidden fields')
else:
    banner()
    print(bcolors.ERR + 'Please select atleast 1 option from -u or -h, with a valid url')


