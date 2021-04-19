def hollowDiamondPattern(n) : 
    k = 0
    stars_count=0
    total_count=0
    for i in range(1,n+1) : 

        for j in range(1,n-i+1) : 
            print("*",end="")
            stars_count+=1
              
        while (k != (2 * i - 1)) : 
            if (k == 0 or k == 2 * i - 2) : 
                print("*",end="")
                stars_count+=1
            else : 
                print(" ",end="") 
            k = k + 1
        for l in range(1,n-i+1) : 
            print("*",end="")
            stars_count+=1
              
        k = 0
        print("-",stars_count,end="")
        total_count+=stars_count
        stars_count=0
        print(""), 
      
    n = n - 1
    for m in range (n,0,-1) : 
        for p in range(0,n-m+1) : 
            print("*",end="")
            stars_count+=1
              
        k = 0
        while (k != (2 * m - 1)) : 
            if (k == 0 or k == 2 * m - 2) : 
                print("*",end="")
                stars_count+=1
            else : 
                print(" ",end="") 
            k = k + 1
        for l in range(1,n-m+2) : 
            print("*",end="")
            stars_count+=1
        print("-",stars_count,end="")
        total_count+=stars_count
        stars_count=0
        print(" ",)
    print("total no of stars are ",total_count)
              
row = int(input('Enter number of row: '))

hollowDiamondPattern(row) 