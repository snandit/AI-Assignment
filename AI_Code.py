


l=[]
l1=[]
l2=[]
l3=[]
l4=[]
l5=[]
for p in range(2):            #p conjuction negation s
    for q in range(2):
        for r in range(2):
            for s in range(2,0,-1):
                if(p==1 and s==1):
                    l.append(1)
                else:
                    l.append(0)
                    
                    
                    

for p in range(2):             #p implies r
    for q in range(2):
        for r in range(2):
            for s in range(2):
                if(r==0 and p==1):
                    l1.append(0)
                else:
                    l1.append(1)

                    
                    
                    
for p in range(2):                #(q conjuction r) implies s
    for q in range(2):
        for r in range(2):
            for s in range(2):
                if(q==1 and r==1 and s==0):
                    l2.append(0)
                else:
                    l2.append(1)
                    
                    
                    
                    
                    
                    
for p in range(2):                    #p conjuction q conjuction r
    for q in range(2):
        for r in range(2):
            for s in range(2):
                if(p==0 or q==0 or r==0):
                    l3.append(0)
                else:
                    l3.append(1)
                    
                    
                    
for i in range(16):                               #combining all
    if(l1[i]==l2[i] and l2[i]==l[i]):
        l4.append(1)
    else:
        l4.append(0)
        
        
        
        

for i in range(16):                              #checking for argument validity
    if(l3[i]==0 and l4[i]==1):
        l5.append(0)
    else:
        l5.append(1)
        
        
        
count=0        
for i in range(16):
    if(l5[i]==1):
        count+=1
        

if(count==15):
    print("yes")
else:
    print("no")
        
        
                





