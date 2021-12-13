import time
from directkeys import K, PressKey, ReleaseKey, W, A, S, D, ENTER
#Time: 20mints
#Money: $48750
#Name: NinjaCat Solo afk



#count = 1

def automation_ninja():
    print("\n\n\nBuffering Time")
    for x in range(15):
        time.sleep(1)
        print(15-x)
    print("\n\n\nLap Started")   
    for x in range(20):
        time.sleep(1)
        print(20-x)
    print("waiting completed")
    #pressing a+s for not going afk for 20 Mints
    PressKey(K)
    for x in range(20):
        print(x+1)
        print("Wave Running")
        time.sleep(29.8)
        print("half the way")
        time.sleep(29.8)
    ReleaseKey(K)
    #releasing s and a after main event completion
    print("End of main event\nwaiting for replay window pop up\n")
    #wait for rp and moneyt screen hover
    
    print("Extras")
    time.sleep(35)
    for x in range(35):
        print(34-x)
        time.sleep(1)
    #pressing replay button and wait for 20 sec to download buffer
    #one down
    PressKey(S)
    ReleaseKey(S)
    time.sleep(0.5)
    
    #two down
    PressKey(S)
    ReleaseKey(S)
    time.sleep(0.5)
    
    #pressing the enter
    PressKey(ENTER)
    ReleaseKey(ENTER)
    print("Entered Replay Button\n")
    #waiting for another 8 secs for confirmation and play pop up
    for x in range(15):
        time.sleep(1)
        print(15-x)
    
    #confirmation selection
    PressKey(W)
    ReleaseKey(W)
    time.sleep(2)
    PressKey(ENTER)
    ReleaseKey(ENTER)
    print("Entered Confermation Button\n")
    #wait between two buffers
    time.sleep(3)    
    
    #play selection
    PressKey(D)
    ReleaseKey(D)
    time.sleep(3)#set to matchmacking closed
    print("Set to Closed Matchmacking")
    PressKey(W)
    ReleaseKey(W)
    time.sleep(3)
    PressKey(ENTER)
    ReleaseKey(ENTER)
    time.sleep(3)
    PressKey(ENTER)
    ReleaseKey(ENTER)
    print("Entered Confermation Button\n")
    print("Waitting for download buffer\n")
    print("Lap Complete\n\n\n\n................................................")   

while(1):
    automation_ninja()  
    count=count+1
    
    
    