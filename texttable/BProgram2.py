
import socket
import httplib
import subprocess
import sys
from datetime import datetime
import time
import texttable
from texttable import Texttable

#subprocess.call('clear', shell=True)

msg="""\x1b[33m
  _____   _____                 
 |  __ \ / ____|                 [#] PScan credit 
 | |__) | (___   ___ __ _ _ __       by MonTav
 |  ___/ \___ \ / __/ _` | '_ \  [#] v1.01
 | |     ____) | (_| (_| | | | | [#] -v selectRSIP
 |_|    |_____/ \___\__,_|_| |_|       """
 
msg2="""
  __  __        _____      
 |  \/  |___ _ |_   _|_ _        [#] -t select Req
 | |\/| / _ \ ' \| |/ _` |            Delay
 |_|  |_\___/_||_|_|\__,_|              
                 [#] -i select PORTS
                                 [#] www.github.com/Monta_0 [#]

\033[97m"""
print "{:<10}\r {:<10}\r".format(msg,msg2)
print "\x1b[49m" 


msg3="""Error ! \033[97m\nPScan [ARG] [TARGET SITE] --[OPTION] \nARGUMENTS:\n\t-v --victimHost   : give the url adress of the target host\nOPTION:\n\t-t --Time_Out     :give the value of timeout in secends\n\t-i --interval     :give the interval of ports begin and end to try "exemple: \n -v www.targetHost.com -i 23 84 "\n\nExemple:  PScan -v www.hostname.com -t 0.5\n\n\t\t \033[91mcredit by MonTassar_Dhouibi\n\t\tuploaded in www.github.com/Monta_0\033[97m"""



l=sys.argv
del l[0]
if len(l)==0:
        print msg3
        exit()
site='';i,time_out,VL,VH=0,0,0,0;a,p=False,False
while len(l)!=0:
    if l[i]=='-v' and len(l)>1:
        site =l.pop(i+1)
        del l[i]
        if l[i]=='-p':
            p=True
            while len(l)!=0:
                if  len(l)>2 and l[i]=='-i' :
                    VL=int(l.pop(i+1))
                    VH=int(l.pop(i+1))
                    del l[i]
                elif len(l)>1 and l[i]=='-t' :
                    time_out=float(l.pop(i+1))
                    del l[i]
                else:
                    print msg3
                    exit()
        elif l[i]=='-a':
            a=True
            del l[i]
            if l[i]=='-s' and len(l)>1:
                type=l.pop(i+1)
                del l[i]
            else:
                print msg3
                exit()
        else :
            print 'no such attack selected'
            print msg3
            exit()
                
                        
                    
                    
    else:
        print msg3
        exit()




tab = Texttable()
header = ['Ports']
tab.header(header)
tab.set_deco(tab.HEADER |tab.BORDER)
tab.set_cols_width([5])
tab.set_cols_align(["l"])
tab.set_cols_dtype(['a']) # automatic





"""print "\n"*2
print "\t","#"*35
print "\t######    [#]   AdminFinder   [#] #####   #"
print " "*20,"[+] MonTa_Ssar [+] "
print "\t","#"*35
print "\n"
print "#"*35
print "\n"*2"""
try:
    site = site.replace("http://","")
    print ("\tChecking website " + site + "...")
    conn = httplib.HTTPConnection(site)
    conn.connect()
    print "\t\033[32m[$] Yes... Server is Online.\033[97m"
    RSIP  = socket.gethostbyname(site)
except (httplib.HTTPResponse, socket.error) as Exit:
    raw_input("\t \033[91m[!] Oops Error occured, Server offline or invalid URL\033[97m")
    exit()

    
if p :
    print "-" * 40
    print "Scanning remote host\033[95m", RSIP
    print "\033[97m-" * 40

    t1 = datetime.now()
    def check(remoteServerIP,t_out,val_L,val_H):
        try:
            for port in range(val_L,val_H+1):
                print "\033[94m[",datetime.now().strftime("%H:%M:%S"),"]","\033[97m[#] cheaking... ",remoteServerIP,":",port
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(t_out)
                result = sock.connect_ex((remoteServerIP, port))
                if result == 0:
                    print "\n"
                    print "\033[32m[ {} ] [++] {} is Open\033[97m".format(datetime.now().strftime("%H:%M:%S"),port)
                    row=[port]
                    tab.add_row(row)
                    print "\n"
                    sock.close()
        except KeyboardInterrupt:
            print "You pressed Ctrl+C"
            sys.exit()
        except socket.gaierror:
            print 'Hostname could not be resolved. Exiting'
            sys.exit()

        except socket.error:
            print "Couldn't connect to server"
            sys.exit()


    if a :

        file=(open("ALL.txt","r")).readlines()
        drag =False
        list=[]
        for element in file:
            element=element.replace("\n","")
            if x =="all":
                    if not( element.find("/.end")!=-1 or element.find("++//")!=-1):
                            list.append(element)
            else:
                            if element.find("/.end")!=-1:
                                    drag=False
                            if drag :
                                    list.append(element)
                            if element.find('++//'+x)!=-1:
                                    drag =True
              
              
              
              
        print("\t [+] Scanning " + site + "...\n\n")
        try :
            for admin in list:
                admin = admin.replace("\n","")
                admin = "/" + admin
                host = site + admin
                print ("\t [#] Checking " + host + "...")
                connection = httplib.HTTPConnection(site)
                connection.request("GET",admin)
                response = connection.getresponse()
                var2 = var2 + 1
                if response.status == 200:
                        var1 = var1 + 1
                        print "%s %s" % ( "\n\n[+]>>>" + host, "Admin page found!")
                        raw_input("Press enter to continue scanning.\n")
                elif response.status == 404:
                        var2 = var2
                elif response.status == 302:
                        print "%s %s" % ("\n>>>" + host, "Possible admin page (302 - Redirect)")
                else:
                        print "%s %s %s" % (host, " Interesting response:", response.status)
                connection.close()
            print("\n\nCompleted \n")
            print var1, " Admin pages found"
            print var2, " total pages scanned"
            raw_input("[/] Press Enter to Exit")
        except (httplib.HTTPResponse, socket.error):
            print "\n\t[!] Session Cancelled; Error occured. Check internet settings"
        except (KeyboardInterrupt, SystemExit):
            print "\n\t[!] Session cancelled"

        


        t2 = datetime.now()


        total =  t2 - t1




        print('{}'.format(tab.draw()))

        print 'Scanning Completed in:      {:7.7}'.format(total)
if time_out==0:
    time_out=1
if VL==0:
    VL=1
if VH==0:
    VH=1025
check(RSIP,time_out,VL,VH)

