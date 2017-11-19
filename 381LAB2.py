# -*- coding: utf-8 -*-
"""

@author: LONGCHENG
"""
import random
def proberror():
    p0 = 0.4
    e0 = 0.02
    e1 = 0.03
    count = 0
    for x in range(100000):
        m = random.uniform(0, 1)
        #Send message == 0 if m <= p0
        #Send message == 1 if m > p0
        if m > p0:
            sent = 1
        else:
            sent = 0
        #Get received
        if sent==0:
            #Receive == 0 if S == 0 and t > prob
            #Receive == 1 if S == 0 and t <= prob
            t = random.uniform(0,1)
            if t > e0:
                received = 0
            else:
                received = 1
            
        else:
            #Receive == 0 if S == 1 and t <= prob
            #Receive == 1 if S == 1 and t > prob
            t = random.uniform(0,1)
            if t > e1:
                received = 1
            else:
                received = 0
            
        #Compare sent and received
        if sent == received:
            count = count + 1
            
    print("Estimated probability of failure is: " , 1-(count / 100000))
    print("\n")

def CPgivenS():
    p0 = 0.4
    e0 = 0.02
    e1 = 0.03
    count = 0
    for x in range(100000):
        sent = 1
        t = random.uniform(0,1)
        #Receive == 0 if S == 1 and t <= prob
        #Receive == 1 if S == 1 and t > prob
        if t > e1:
            received = 1
        else:
            received = 0
        #Compare sent and received
        if sent == received:
            count = count + 1
            
    print("The Conditional of Probability P(R=1|S=1) is: " , (count / 100000))
    print("\n")

def CPgivenR():
    p0 = 0.4
    e0 = 0.02
    e1 = 0.03
    count = 0
    count2 = 0
    count3 = 0
    for x in range(100000):
        m = random.uniform(0, 1)
        #Send message == 0 if m <= p0
        #Send message == 1 if m > p0
        if m > p0:
            sent = 1
            count3 = count3 + 1
            t = random.uniform(0,1)
            if t > e1:
                received = 1
                count = count + 1
            else:
                received = 0
        else:
            sent = 0
            t = random.uniform(0,1)
            if t > e0:
                received = 0
            else:
                received = 1
                count2 = count2 + 1
    print(count)
    print(count2)
    print(count3)
            
    print("The Conditional of Probability P(S=1|R=1) is: " , ((count+count2) / count3))
    print("\n")
    
def Etrans():
    p0 = 0.4
    e0 = 0.02
    e1 = 0.03
    count = 0
    for k in range(100000):
        sent = []
        received = []
        #for x in range(0,3):
        m = random.uniform(0, 1)
        #Send message == 0 if m <= p0
        #Send message == 1 if m > p0
        if m > p0:
            sent.append(1)
            sent.append(1)
            sent.append(1)
            for x in range(0,3):
                t = random.uniform(0,1)
                #Receive == 0 if S == 1 and t <= prob
                #Receive == 1 if S == 1 and t > prob
                if t > e1:
                    received.append(1)
                else:
                    received.append(0)
        else:
            sent.append(0)
            sent.append(0)
            sent.append(0)
            for y in range(0,3):
                t = random.uniform(0,1)
                #Receive == 0 if S == 0 and t > prob
                #Receive == 1 if S == 0 and t <= prob
                if t > e0:
                    received.append(0)
                else:
                    received.append(1)
        #Check the majority rule
        if sum(sent) >= 2:
            Ds = 1
        else:
            Ds = 0
        
        if sum(received) >= 2:
            Dr = 1
        else:
            Dr = 0
        #If the D(sent) == D(received) means success
        if Ds == Dr:
            count = count +1
            
 
    print("Estimated probability of failure is: " , 1-(count / 100000))
    print("\n")
    
def main():
    #proberror()
    #CPgivenS()
    #CPgivenR()
    Etrans()
    
	
if __name__ == '__main__':
	main()

exit