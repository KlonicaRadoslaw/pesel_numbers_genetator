
import threading

#Operation on file
text_file = open("pesel.txt", "a")

#Functions to generate numbers before 2000
def part1():
    for a in range(0,10): #R1
        for b in range(0, 10): #R2
            for d in range(1, 3): #M2
                for e in range(0, 4): #D1
                    for f in range(0, 10): #D2
                        if (d==2 and e==2 and f>8) or (e==3 and f>1):
                            continue
                        else:
                            for g in range(0, 10): #P1
                                for h in range(0, 10): #P2
                                    for i in range(0, 10): #P3
                                      for j in range(0, 10): #P4
                                            text_file.write(str(a)+str(b)+str(0)+str(d)+str(e)+str(f)+str(g)+str(h)+str(i)+str(j)+str((a*1+b*3+d*9+e*1+f*3+g*7+h*9+i*1+j*3)%10)+"\n")

def part2():
    for a in range(0,10): #R1
        for b in range(0, 10): #R2
            for d in range(3, 5): #M2
                for e in range(0, 4): #D1
                    for f in range(0, 10): #D2
                        if e==3 and f>1:
                            continue
                        else:
                            for g in range(0, 10): #P1
                                for h in range(0, 10): #P2
                                    for i in range(0, 10): #P3
                                      for j in range(0, 10): #P4
                                            text_file.write(str(a)+str(b)+str(0)+str(d)+str(e)+str(f)+str(g)+str(h)+str(i)+str(j)+str((a*1+b*3+d*9+e*1+f*3+g*7+h*9+i*1+j*3)%10)+"\n")

def part3():
    for a in range(0,10): #R1
        for b in range(0, 10): #R2
            for d in range(5, 7): #M2
                for e in range(0, 4): #D1
                    for f in range(0, 10): #D2
                        if e==3 and f>1:
                            continue
                        else:
                            for g in range(0, 10): #P1
                                for h in range(0, 10): #P2
                                    for i in range(0, 10): #P3
                                      for j in range(0, 10): #P4
                                            text_file.write(str(a)+str(b)+str(0)+str(d)+str(e)+str(f)+str(g)+str(h)+str(i)+str(j)+str((a*1+b*3+d*9+e*1+f*3+g*7+h*9+i*1+j*3)%10)+"\n")

def part4():
    for a in range(0,10): #R1
        for b in range(0, 10): #R2
            for d in range(7, 9): #M2
                for e in range(0, 10): #D1
                    for f in range(0, 10): #D2
                        if e==3 and f>1:
                            continue
                        else:
                            for g in range(0, 10): #P1
                                for h in range(0, 10): #P2
                                    for i in range(0, 10): #P3
                                      for j in range(0, 10): #P4
                                            text_file.write(str(a)+str(b)+str(0)+str(d)+str(e)+str(f)+str(g)+str(h)+str(i)+str(j)+str((a*1+b*3+d*9+e*1+f*3+g*7+h*9+i*1+j*3)%10)+"\n")

def part5():
    for a in range(0,10): #R1
        for b in range(0, 10): #R2
            for d in range(9, 10): #M2
                for e in range(0, 4): #D1
                    for f in range(0, 10): #D2
                        if e==3 and f>1:
                            continue
                        else:
                            for g in range(0, 10): #P1
                                for h in range(0, 10): #P2
                                    for i in range(0, 10): #P3
                                      for j in range(0, 10): #P4
                                            text_file.write(str(a)+str(b)+str(0)+str(d)+str(e)+str(f)+str(g)+str(h)+str(i)+str(j)+str((a*1+b*3+d*9+e*1+f*3+g*7+h*9+i*1+j*3)%10)+"\n")

def part6():
    for a in range(0,10): #R1
        for b in range(0, 10): #R2
            for d in range(1, 4): #M2
                for e in range(0, 4): #D1
                    for f in range(0, 10): #D2
                        if e==3 and f>1:
                            continue
                        else:
                            for g in range(0, 10): #P1
                                for h in range(0, 10): #P2
                                    for i in range(0, 10): #P3
                                      for j in range(0, 10): #P4
                                            text_file.write(str(a)+str(b)+str(1)+str(d)+str(e)+str(f)+str(g)+str(h)+str(i)+str(j)+str((a*1+b*3+d*9+e*1+f*3+g*7+h*9+i*1+j*3)%10)+"\n")


part1 = threading.Thread(target=part1)
part2 = threading.Thread(target=part2)
part3 = threading.Thread(target=part3)
part4 = threading.Thread(target=part4)
part5 = threading.Thread(target=part5)
part6 = threading.Thread(target=part6)
try:
    part1.start()
    part2.start()
    part3.start()
    part4.start()
    part5.start()
    part6.start()
except:
   print ("Error: unable to start thread")