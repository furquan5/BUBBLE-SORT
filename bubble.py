import time
def bubble(L):
    
    for i in range(len(L)-1):
        print('this is the ',i,'pass')
        time.sleep(1)
        for j in range(len(L)-1-i):
            time.sleep(1)
            print('j is',L[j],'j+1 is',L[j+1])
            if L[j]>L[j+1]:
                print('Swap hoga')
                L[j],L[j+1]=L[j+1],L[j]
                print('After swap',L)
        print('After the pass',L)
    print(L)

L=[12,34,11,10,45,100]
bubble(L)
