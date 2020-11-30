def MultiSig(t1,x1,t2,x2):

    max = np.max([np.max(t1),np.max(t2)]) #check for max (in t1 & t2)
    min = np.min([np.min(t1),np.min(t2)]) #check for min (in t1 & t2)

    t = np.arange(min,max+1) #vector time in max range of two signals
    y = np.zeros(t.size) #zeros vector in max range for y 
    j=0
    k=0

    for i in range(t.size): #multiplication of signals
        print(i)
        if(t[i]==t1[j]):
            y[i]+=x1[j]
            if(t1[j]<np.max(t1)):
                 j+=1
            if(t[i]==t2[k]):
                y[i]*=x2[k]
                if(t2[k]<np.max(t2)):
                    k+=1
                
        if(t[i]==t2[k] & t2[k]<np.max(t2)):
            y[i]+=x2[k]
            if(t2[k]<np.max(t2)):
                k+=1

    return y,t
