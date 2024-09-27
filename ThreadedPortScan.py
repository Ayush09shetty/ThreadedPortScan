import socket
import time
import threading
TARGET=input("Enter the target:")
START_PORT=input("Enter the START_PORT:")
END_PORT=input("Enter the END_PORT:")
sav=input("Do you wish to save this file[Y/N]")
s=sav.capitalize()
sav=s[0]
if(sav=='Y'):
    filename=input("Enter a file name with extension:")
    f=open(filename, 'a')
    print("Saved successfully")
    print("File Name: ", f.name)
print("-"*70)
print("Python port scanner")
print("-"*70)
start_time=time.time()
try:
    target=socket.gethostbyname(TARGET)
except socket.gaierror:
    print("Name resolution error")
start_port = int(START_PORT)
end_port=int(END_PORT)
print("Scanning target",target)
def scan_port(port):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #socket.AF_INET is used address family of internet IPv4 socket.
    #socket.SOCK_STREAM is used decide tcp or udp connection we used tcp
    s.settimeout(2)
    conn=s.connect_ex((target,port))
    if(not conn):
        print("Port {} is OPEN".format(port))
        if(sav=='Y'):
            f.write("Port {} is OPEN\n".format(port))
        s.close()
for port in range(start_port,end_port+1):
    thread=threading.Thread(target=scan_port,args=(port,))
    thread.start()

end_time=time.time()
print("Time elapsed:",end_time - start_time)