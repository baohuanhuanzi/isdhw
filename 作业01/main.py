for i in range(1,10):
    s=''
    t=''
    for j in range(i,10):
         s+=str.format("{0:1}*{1:1}={2:<2}",i,j,i*j)
    t+=s
    print(t.rjust(54," "))
 
                                                       
