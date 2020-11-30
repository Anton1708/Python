# MultiSig.py : Multiplication of 2 discret signals

        #Example
        import matplotlib.pyplot as plt
        import numpy as np
        plt.subplots_adjust(left=0.09,bottom=0.1,right=0.94,top=0.95,wspace=None,hspace=0.53)

        x1 = [2, 3, 4,5,6,7,8,9] #first signal
        t1 = [0, 1, 2,3,4,5,6,7] #time vector for first signal
        x2 = [1, 2, 3,4,5] #second signal
        t2 = [-4,-3,-2,-1,0] #time vector for second signals

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

        (y,t) = MultiSig(t1,x1,t2,x2)

        plt.subplot(3,1,1)
        plt.stem(t1,x1)
        plt.title('X1(t)')

        plt.subplot(3,1,2)
        plt.stem(t2,x2)
        plt.title('X2(t)')

        plt.subplot(3,1,3)
        plt.stem(t,y)
        plt.title('x1(t) * x2(t)')
        plt.show()
