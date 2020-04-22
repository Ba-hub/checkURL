#!/usr/bin/python
#########################################################################
# SCRIPT : checkURL                                                     #
# JOB    : Check IF URL IS MALICIOUS URL OR NOT                               #
# Codedby: ghosthub (b@b@y)                                                 #
#########################################################################
# LIBRARIES #
import mechanize,re,socket,optparse
from os import system as sy; from time import sleep as se;from webbrowser import open as op
sy("cls||clear") # Clear screen
# Check Internet Connection #
def cnet():
    try:
        ip = socket.gethostbyname("google.com")
        con = socket.create_connection((ip, 80), 2)
        return True
    except socket.error:
        pass
    return False
# CheckURL Function #
def checkURL(url):
    if cnet() !=True:
        print("\033[1;31m[\033[1;33m!\033[1;31m]\033[1;33m Error:\033[1;37m Please Check Your Internet Connection \033[1;31m!!!")
        exit(1)
    try:
        br = mechanize.Browser()
        br.set_handle_robots(False)
        br.addheaders = [("User-agent","Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.13) Gecko/20101206 Ubuntu/10.10 (maverick) Firefox/3.6.13")]
        br.open("https://safeweb.norton.com/")
        br.select_form(nr=0)
        br["url"]=url
        br.method="get"
        res = br.submit()
        response = res.get_data()
        ch = "This site has not been tested yet."
        if "Unknown" in response:
            loc = "Unknown"
        else:
            try:
             loc = re.findall(r'</img>&nbsp;[^>]*', response)
             loc = loc[0].strip('</img>&nbsp;')
             loc = loc.strip('</div')
            except:
                loc = "???"
        try:
          status = re.findall(r'<b>[^>]*</b></br>',response)[0].strip('<b></b></br>')
        except:
            status = "???"
        try:
          com = re.findall(r'<label>[^>]*</label>', response)[3].strip('<label></label>')
        except:
            com = "0.0"
        try:
            ratedby = re.findall('<small><div class="marginTopM15">[^>]*</div></small>', response)[0].split()
            ratedby = ratedby[3]
        except:
            ratedby ="0"
        if ch not in response:
         tr1 = re.findall(r'Computer Threats: [^>]*', response)[0].strip('Computer Threats: </li>')
         tr2 = re.findall(r'Identity Threats: [^>]*', response)[0].strip('Identity Threats: </li>')
         tr3 = re.findall(r'Annoyance factors: [^>]*', response)[0].strip('Annoyance factors: </li>')
         tot = re.findall(r'Total threats</b> on this site: [^>]*',response)[0].strip('\t\n              \t\t\t</div')
         tot = tot.strip('Total threats</b>')
         totp = tot.strip('n this site:')
         tot = tot[13:]
        else:
            tr1 = "???"
            tr2 = "???"
            tr3 = "???"
            totp = "???"
        print("\n\033[1;32m[\033[1;37m*\033[1;32m] CheckURL[ \033[1;33m{}\033[1;32m ]\033[1;37m ...\033[1;32mBy[\033[1;37mghosthub(b@b@y)\033[1;32m]".format(url))
        se(2)
        if status =="UNTESTED":
            se(0.10)
            print("\n\033[1;33m[\033[0;33m?\033[1;33m] WebSite Location :\033[1;31m "+loc)
            se(0.10)
            print("\n\033[1;33m[\033[0;33m?\033[1;33m] WebSite STATUS     :\033[1;31m UNTESTED\033[1;33m ?")
            se(0.10)
            print('  \033[1;33m[\033[1;31m?\033[1;33m] Computer Threats   :\033[1;31m '+tr1)
            se(0.10)
            print('  \033[1;33m[\033[1;31m?\033[1;33m] Identity Threats   :\033[1;31m '+tr2)
            se(0.10)
            print('  \033[1;33m[\033[1;31m?\033[1;33m] Annoyance factors  :\033[1;31m '+tr3)
            se(0.10)
            print('\n\033[1;33m[\033[1;31m?\033[1;33m] Total Site threats :\033[1;31m '+totp)
            se(0.10)
            print('\n  \033[1;33m[\033[1;31m?\033[1;33m] Website Rated    :\033[1;31m '+com)
            se(0.10)
            print('  \033[1;33m[\033[1;31m?\033[1;33m] Rated by         :\033[1;31m '+ratedby+" \033[1;33mUsers")
            se(0.10)
            print("\n\033[1;33m=====> \033[0;33mResult\033[1;33m <=====:\n\033[1;31m[\033[1;33m!\033[1;31m]\033[1;33m This \033[1;31m[ \033[1;33m"+url+"\033[1;31m ]\033[1;33m Website Has Not been Tested Yet\033[1;31m!\n")
        elif int(tot) ==0:
            se(0.10)
            print('\n\033[1;32m[\033[1;37m?\033[1;32m]\033[1;37m Website Location   :\033[1;32m '+loc)
            se(0.10)
            print("  \033[1;32m[\033[1;37m+\033[1;32m]\033[1;37m STATUS : \033[1;32m"+status)
            se(0.10)
            print('  \033[1;32m[\033[1;37m+\033[1;32m]\033[1;37m Computer Threats   :\033[1;32m '+tr1)
            se(0.10)
            print('  \033[1;32m[\033[1;37m+\033[1;32m]\033[1;37m Identity Threats   :\033[1;32m '+tr2)
            se(0.10)
            print('  \033[1;32m[\033[1;37m+\033[1;32m]\033[1;37m Annoyance factors  :\033[1;32m '+tr3)
            se(0.10)
            print('\n\033[1;32m[\033[1;37m+\033[1;32m]\033[1;37m Total Site threats :\033[1;32m '+totp)
            se(0.10)
            print('\n  \033[1;32m[\033[1;37m+\033[1;32m]\033[1;37m Website Rated  :\033[1;32m '+com)
            se(0.10)
            print('  \033[1;32m[\033[1;37m+\033[1;32m]\033[1;37m Rated By       :\033[1;32m '+ratedby+"\033[1;37m Users")
            se(0.10)
            print("\n\033[1;32m=====> \033[1;36mResult\033[1;32m <=====:\n\033[1;32m[\033[1;37m+\033[1;32m]\033[1;37m Secure And Trusted URL[ \033[1;32m"+url+"\033[1;37m ]\n")
            ask = raw_input("\n\033[1;36m~\033[1;32mOPEN[\033[1;37m {} \033[1;32m]\033[1;33m ?(\033[1;37mY:n\033[1;33m)>\033[1;32m ".format(url))
            while ask=="" or ask is None or ask not in ['Y',"y","yes","YES","n","N","NO","no"]:
                ask = raw_input("\033[1;33m!?~\033[1;31mOPEN[\033[1;37m {} \033[1;31m]\033[1;33m ??(\033[1;37mY:n\033[1;33m)>\033[1;31m ".format(url))
            if ask in ["Y","y","yes","YES"]:
		if "https://" in url or "http://" in url:
                 print("\n\033[1;32m[\033[1;37m+\033[1;32m] \033[1;37mOpening....[ \033[1;32m{}\033[1;37m ]".format(url))
                 se(1)
                 op(url)
                 print("\n\033[1;36m~Done\033[1;32m :)")
		else:
                  print("\n\033[1;32m[\033[1;37m+\033[1;32m] \033[1;37mOpening....[ \033[1;32m{}\033[1;37m ]".format(url))
		  url = "https://"+url
                  se(1)
                  op(url)
                  print("\n\033[1;36m~Done\033[1;32m :)")
            else:
                print("\n\033[1;36m~Done\033[1;32m :)")
                exit(1)
        else:
            se(0.10)
            print('\n\033[1;31m[\033[1;33m@\033[1;31m]\033[1;33m Website Location   :\033[1;31m '+loc)
            se(0.10)
            print("  \033[1;31m[\033[1;33m!\033[1;31m]\033[1;33m STATUS : \033[1;31m"+status)
            se(0.10)
            print('  \033[1;31m[\033[1;33m-\033[1;31m]\033[1;33m Computer Threats   :\033[1;31m '+tr1)
            se(0.10)
            print('  \033[1;31m[\033[1;33m-\033[1;31m]\033[1;33m Identity Threats   :\033[1;31m '+tr2)
            se(0.10)
            print('  \033[1;31m[\033[1;33m-\033[1;31m]\033[1;33m Annoyance factors  :\033[1;31m '+tr3)
            se(0.10)
            print('\n\033[1;31m[\033[1;33m!\033[1;31m]\033[1;33m Total Site threats :\033[1;31m '+totp)
            se(0.10)
            print('\n  \033[1;31m[\033[1;33m-\033[1;31m]\033[1;33m Website Rated      :\033[1;31m '+com)
            se(0.10)
            print('  \033[1;31m[\033[1;33m-\033[1;31m]\033[1;33m Rated By           :\033[1;31m '+ratedby+"\033[1;33m Users")
            se(0.10)
            print("\n\033[1;31m=====>\033[1;33mResult\033[1;31m<=====\n\033[1;31m[\033[1;33m!\033[1;31m]\033[1;33m Not Secure Bad URL[ \033[1;31m"+url+"\033[1;33m ]\n")         
    except KeyboardInterrupt:
        print("\n\033[1;31m[\033[1;33m!\033[1;31m]\033[1;33m Exiting...")
        se(1.5)
        print("\033[1;36m~\033[1;32mBye: )")
        exit(1)
    except IndexError:
        print("\n\033[1;33m[\033[1;31m!\033[1;33m] Error:\033[1;37m Please Check Your URL\033[1;31m !!!")
        exit(1)
parse = optparse.OptionParser("""
/============================+====================================\ 
|			     |					                             |
| [*] SCRIPT  : CheckURL     |   [~] JOB: URL Security Checker    |
| [+] Version : 1.0          |   [~] Author : ghosthub (b@b@y)    |
|----------------------------+------------------------------------|
|								                                   |
)USAGE:								                             |
|     +))))) python2 checkURL.py -u/--url <[WEBSITE URL]>	     |
|								                                   |
)Example:							                               |
|       +)))))) python2 checkURL.py -u https://www.google.com     |
|                                                                 |
\=================================================================/
""")
def Main():
    parse.add_option("-u","-U","--url","--URL", dest="URL", type="string")
    (opt, args) = parse.parse_args()
    if opt.URL !=None:
        url = opt.URL
        checkURL(url)
    else:
        print(parse.usage)
        exit(1)

if __name__=="__main__":
    Main()

    
