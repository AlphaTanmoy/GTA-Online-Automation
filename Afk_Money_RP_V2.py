import time
from typing import Counter
from directkeys import ESC, K, LCTRL, PressKey, ReleaseKey, W, A, S, D, ENTER
Count = 0
def Auto():
    for x in range(5):
        #m = x+1
        for y in range(60):
            time.sleep(1)
            print(f"{x} Mint : {y} Secnds START")
        
    print("\n\n-------------------------------------------------------------\n")    
    print("-------------------------MAIN EVENT STARTED------------------------")       
    print("\n-------------------------------------------------------------\n\n") 

    PressKey(K)
    
    for x in range(16):
        #m = x+1
        for y in range(60):
            time.sleep(1)
            print(f"{x} Mint : {y} Secnds MAIN")
        
    ReleaseKey(K)
        
    print("\n\n-------------------------------------------------------------\n")    
    print("-------------------------MAIN EVENT ENDED------------------------")       
    print("\n-------------------------------------------------------------\n\n")      
    for x in range(4):
        #m = x+1
        for y in range(60):
            time.sleep(1)
            print(f"{x} Mint : {y} Secnds END")
    print("Buffering Ended")
    for x in range(40):
        time.sleep(1)
        s=39-x
        print(f"Last {s} Secnds END")
    print("Pressing the W")
    PressKey(W)
    ReleaseKey(W)
    time.sleep(1.4)
    print("Pressed W")
    print("Pressing the Enter")
    PressKey(ENTER)
    ReleaseKey(ENTER)
    print("Entered Replay Button\n")
    print("Buffering")
    for x in range(20):
        time.sleep(1)
        print(19-x)
    
    #confirmation selection
    PressKey(W)
    ReleaseKey(W)   
    for x in range(3):
        time.sleep(1)
        print(3-x)
    PressKey(ENTER)
    ReleaseKey(ENTER)
    print("Entered Confermation Button\n")
    #wait between two buffers 
    for x in range(4):
        time.sleep(1)
        print(4-x)
    #play selection
    #PressKey(D)
    #ReleaseKey(D)
    #time.sleep(3)#set to matchmacking closed
    #print("Set to Closed Matchmacking")
    PressKey(W)
    ReleaseKey(W)
    for x in range(3):
        time.sleep(1)
        print(3-x)
    PressKey(ENTER)
    ReleaseKey(ENTER)
    for x in range(3):
        time.sleep(1)
        print(3-x)
    PressKey(ENTER)
    ReleaseKey(ENTER)
    for x in range(3):
        time.sleep(1)
        print(3-x)
    print("Entered Confermation Button\n")
    print("Lap Complete\n\n\n\n................................................")
    

while(1):
    Count = Count + 1
    print(f"THE LAP NUMBER IS: {Count}")
    Auto()
    