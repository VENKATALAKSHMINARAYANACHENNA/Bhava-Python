#OHM VIGNESWARAYANAMAHA
#OHM SRI LAKSHMI PADMAVATI SAMETHA VENKATESHAYANAMAHA
#OHM BHADRAVATHI SAMETHA BHAVANARAYANAYANAMAHA
def swasthik(n):
    for i in range(0,n):
        for j in range(0,n):
            if(((i==0)and(j<=n-1 and j>=n//2))or(j==n//2)or((i==n-1)and(j<=n//2 and j>=0))or((j==0)and (i>=0 and i<=n//2))or(i==n//2)or((j==n-1)and(i>=n//2 and i<=n-1))):
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()


def saptaswara(n):
    for i in range(0,n):
        c=['S','R','G','M','P','D','N','S']
        k=0
        for j in range(0,2*n-1):
            if(j<n-i-1 or j>n+i-1):
               print(' ',end=' ')
            if(j>=n-i-1 and j<n):
                print(c[k],end=' ')
                k=k+1
            if(j>=n and j<=n+i-1):
                if j==n:
                    k=k-2
                print(c[k],end=' ')
                k=k-1              
        print()


def swaraleftlower(n):
    """Prints Sapta Swara in Left Lower Traingle Pattern"""
    for i in range(0,n):
        c=['S','R','G','M','P','D','N','S']
        for j in range(0,i+1):
            print(c[j],end=' ')
        print()

def swaraleftupper(n):
    """Prints Sapta Swara in Left Upper Pattern"""
    for i in range(1,n+1):
        c=['S','R','G','M','P','D','N','S']
        k=0
        for j in range(n,i-1,-1):
            print(c[k],end=' ')
            k=k+1
        print()

def swarapascal(n):
    """Prints Sapta Swara  in right lower traingle Pattern"""
    for i in range(0,n):
        for j in range(0,n-i):
            print(end=' ')
        c=['S','R','G','M','P','D','N','S']
        for k in range(0,i+1):
            print(c[k],end=' ')
        print()
    print(end=' ')    
def swarareversepascal(n):
    """Prints Sapta Swara in right upper traingle Pattern"""
    for i in range(0,n):
        for j in range(0,i):
            print(end=' ')
        c=['S','R','G','M','P','D','N','S']   
        x=0
        for k in range(n,i,-1):
            print(c[x],end=' ')
            x=x+1
        print()               

def swarafull(n):
    """Prints Sapta Swara  in Arohana Avarohana Traingle Pattern"""
    c=['S','R','G','M','P','D','N','S']   
    for i in range(0,n):
        for j in range(0,n-i):
            print(end=' ')
        for k in range(0,i+1):
            print(c[k],end=' ')
        print()
    c.reverse()
    for i in range(0,n):    
        print(end=' ')
        for j in range(0,i):
            print(end=' ')
        x=0
        
        for k in range(n,i,-1):
            print(c[x],end=' ')
            x=x+1
        print()

def swaralowerupper(n):
    c=['S','R','G','M','P','D','N','S']
    for i in range(0,n):
        for j in range(0,i+1):
            print(c[j],end=' ')
        print()
    for i in range(0,n):
        k=0
        for j in range(n-1,i,-1):
            print(c[k],end=' ')
            k=k+1
        print()
