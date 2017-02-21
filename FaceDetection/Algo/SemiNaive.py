# -*- coding: utf-8 -*-
"""
Created on Tue Sep 06 09:24:11 2016

@author: user
"""

import os
from PIL import Image
from pylab import *
import numpy as np
from Preprocessing import *
from TrainSemiNaive import *
from Model import *




class SemiNaive:
    def __init__(self,shape,Cutoff,Subsize): 
       
        self._data=shape
        self._data1=Cutoff
        self._data2=Subsize
    def train(self,faces,nonfaces,model):
        print self._data
        print self._data1
        print self._data2

# Counting occurance Matrix
        p=4
        q=2
        faces=np.array(faces).T
        nonfaces=np.array(nonfaces).T
        pCoefficientTableClass=np.zeros((4,2),dtype=np.float)
        nCoefficientTableClass=np.zeros((4,2),dtype=np.float)
        for i in range(0,len(faces)):
            list1=faces[i]
            #list2=nonfaces[i]
#            print 'i'
#            print i
            #print list1
            #print list2
            for j in range(0,len(list1)):
                pterm=list1[j]
#                print 'ptem'
#                print ptem
#                print 'j'
#                print j
                pCoefficientTableClass[j][pterm]= pCoefficientTableClass[j][pterm]+1
        print pCoefficientTableClass
        for i in range(0,len(nonfaces)):
            list2=nonfaces[i]
#            print 'i'
#            print i
            #print list1
            #print list2
            for j in range(0,len(list1)):
                nterm=list2[j]
#                print 'ptem'
#                print ptem
#                print 'j'
#                print j
                nCoefficientTableClass[j][nterm]= nCoefficientTableClass[j][nterm]+1
        print nCoefficientTableClass
     

# Coefficient Matrix

        n=4
        m=4
        p=2
        q=2
        pCoefficientPairTable=np.zeros((m,n,p,q),dtype=np.float)
        nCoefficientPairTable=np.zeros((m,n,p,q),dtype=np.float) 
        for i in range(0,len(faces)):
            list1=faces[i]
            #list2=faces[1]
            for j in range(0,len(list1)):
                x=list1[j]
#                print 'kk'
#                print kk
                for k in range(0,len(list1)):
                    y=list1[k]
#                    print 'pp'
#                    print pp
                    pCoefficientPairTable[j][k][x][y]=pCoefficientPairTable[j][k][x][y]+1
        print pCoefficientPairTable            
        for i in range(0,len(nonfaces)):
            list1=nonfaces[i]
            for j in range(0,len(list1)):
                x=list1[j]
                for k in range(0,len(list1)):
                    y=list1[k]
                    nCoefficientPairTable[j][k][x][y]=nCoefficientPairTable[j][k][x][y]+1
        print nCoefficientPairTable                        
#                    


#computing probablity matrix
                
        m=4
        n=4
        p=4
        q=4
        n1=2
        n2=2
        epsilon=np.finfo(np.float).eps
        c1_error_equ=np.zeros((p,q),dtype=np.float)
#        faces1=faces[0]
#        faces2=faces[1]
#        nfaces1=nonfaces[0]
#        nfaces2=nonfaces[1]
        for i in range(0,4):
            for j in range(0,4):
                for m in range(0,2):
                    for n in range(0,2):
                        ri1=pCoefficientTableClass[i][m]
                        #print ri1
                        probxiw1= ri1/n1
                        ri2=nCoefficientTableClass[i][m]
                        #print ri2
                        probxiw2=ri2/n2
                        rj1=pCoefficientTableClass[j][n]
                        #print rj1
                        probxjw1=rj1/n1
                        rj2=nCoefficientTableClass[j][n]
                        #print rj2
                        probxjw2=rj2/n2
#                        list10=faces[0]
#                        list11=faces[1]
                        q1=pCoefficientPairTable[i][j][m][n]
                        #print 'q1'                        
                        #print q1
#                        listn10=nonfaces[0]
#                        listn11=nonfaces[1]
                        q2=nCoefficientPairTable[i][j][m][n]
                        #print 'q2'
                        #print q2
                        #print (q1+q2)/(n1+n2)
                        probxixj=(q1+q2)/(n1+n2)
                        #print probxixj
                        probxixjw1=q1/n1
                        probxixjw2=q2/n2
#                        print 'pxjw1'
#                        print probxjw1
#                        print 'pxjw2'
#                        print probxjw2
#                        print max(probxixjw1,epsilon)
                        first_cal=math.log(max(probxixjw1,epsilon)/max(probxixjw2,epsilon))
#                        print 'first'
#                        print first
                        second_cal=math.log(max(probxiw1*probxjw1,epsilon)/max(probxiw2*probxjw2,epsilon))
#                        print 'second'
#                        print second
#                        print 'abs'
                        abs1=abs(first_cal-second_cal)
#                        print abs1
#                        print 'total'
                        total=probxixj*abs1
#                        print total
                        c1_error_equ[i][j]=c1_error_equ[i][j]+total
#                        
        print c1_error_equ                 
#                        r1= math.log(max(probxjw1,epsilon))-math.log(max(probxjw2,epsilon))
#                        r2=math.log(max(probxiw1*probxjw1,epsilon))-math.log(max(probxiw2*probxjw2,epsilon))
#                        #r2=max(probxjw2,epsilon)
#                        print r2
#                        #print probxjw1/r2
#                        print math.log(epsilon)
#                        r1=math.log(max(probxjw1/probxjw2 , epsilon))
#                        print r1
#                        r3=max(probxiw2*probxjw2 , epsilon)
#                        print r3
#                        r4=max((probxiw1*probxjw1)/r3 , epsilon)
#                        print r4                            
#                        print 'clequ'                        
#                        print clequ
#                        r3=probxixj*abs(r1-r2)
#                        print r3
#                        clequ[i][j]=clequ[i][j]+r3 
                        
#                       # clequ[i][j]=probxixj * abs((math.log(max((probxjw1/max(probxjw2,epsilon),epsilon)))-math.log(max((probxiw1*probxjw1/max(probxiw2*probxjw2,epsilon)),epsilon)))            
#                         
#                        
       # clequ=[0.693,0.0,9.184,17.675]
#        
#        for i in range(0,len(classfaces1)):
#            for j in range(0,2):
#                ri1=pCoefficientTableClass[i][j]
#        print ri1
#        probxiw1=math.log(max(ri1/n1,epsilon))
#        classfaces2=faces[1]
#        for i in range(0,len(classfaces2)):
#            for j in range(0,2):
#                rj1=pCoefficientTableClass[i][j]
#        print rj1
#        probxjw1=math.log(max(rj1/n1,epsilon))
#        classnfaces2=nonfaces[0]
#        for i in range(0,len(classnfaces2)):
#            for j in range(0,2):
#                ri2=nCoefficientTableClass[i][j]
#        print ri2
#        probxiw2=math.log(max(ri2/n1,epsilon))
#        classnfaces2=nonfaces[1]
#        for i in range(0,len(classnfaces2)):
#            for j in range(0,2):
#                rj2=nCoefficientTableClass[i][j]
#        print rj2
#        probxjw2=math.log(max(rj2/n1,epsilon))
#        list1=faces[0]
#        list2=faces[1]
#        for i in range(0,len(list1)):
#            for j in range(0,len(list2)):
#                for k in range(0,2):
#                    for p in range(0,2):
#                        q1=pCoefficientPairTable[list1[i]][list2[j]][k][p]
#        print q1
#        listn1=nonfaces[0]
#        listn2=nonfaces[1]
#        for i in range(0,len(listn1)):
#            for j in range(0,len(listn2)):
#                for k in range(0,2):
#                    for p in range(0,2):
#                        q2=pCoefficientPairTable[listn1[i]][listn2[j]][k][p]
#        print q2
#        print (q1+q2)/(n1+n2)
#        probxixj=math.log(max((q1+q2)/(n1+n2),epsilon))
#        print probxixj
#        probxjw1=q1/n1
#        probxjw2=q2/n2
#       from here     
        
#                        
##building probablity matrix based on subgroups
                        
        p=4
        q=2
        c=0
        prob=np.zeros((p,q),dtype=np.int)
        for i in range(0,4):
            s1=d1=c1_error_equ[i][i]
            prob[i][0]=i
            for j in range(0,4):
                cv=c1_error_equ[i][j]
#                print 'cv'
#                print cv
                if(i!=j):
                    #print 'yes'
                    if((s1==d1)and(s1<cv)):
#                        print 'not'
                        c=j
                        s1=cv
#                        print 's1'
#                        print s1
#                        print 'c'
#                        print c
#                        print 'probT'
#                        print probT
                    else:
                        if(s1!=d1):
                            if(s1<cv):
                                if(d1<cv):
                                    c=j
                                    s1=cv
                                  
                                    
                                  
            prob[i][1]=c
        print prob

## Classification matrix

        
        m=4
        n=4
        psubprob=np.zeros((m,n),dtype=np.float)
        nsubprob=np.zeros((m,n),dtype=np.float)
        for i in range(0,2):
            list1=faces[i]
            for j in range (0,4):
                p=prob[j][0]
                pp=list1[p]
                k=prob[j][1]
                kk=list1[k]
                
                if((pp==0)and(kk==0)):
                    psubprob[j][0]=psubprob[j][0]+1
                if((pp==0)and(kk==1)):
                    psubprob[j][1]=psubprob[j][1]+1
                if((pp==1)and(kk==0)):
                    psubprob[j][2]=psubprob[j][2]+1
                if((pp==1)and(kk==1)):
                    psubprob[j][3]=psubprob[j][3]+1 
                    
        for i in range(0,2):
            list1=nonfaces[i]
            for j in range (0,4):
                p=prob[j][0]
                pp=list1[p]
                k=prob[j][1]
                kk=list1[k]
                if((pp==0)and(kk==0)):
                    nsubprob[j][0]=nsubprob[j][0]+1
                if((pp==0)and(kk==1)):
                    nsubprob[j][1]=nsubprob[j][1]+1
                if((pp==1)and(kk==0)):
                    nsubprob[j][2]=nsubprob[j][2]+1
                if((pp==1)and(kk==1)):
                    nsubprob[j][3]=nsubprob[j][3]+1 
        print psubprob
        print nsubprob
#        smaple=[1,1,1,1]
#        for i in range(0,4):
#            list1=probT[i]
#            for j in range (0,len(list1)):
#                first=sample[list[0]]
#                second=sample[list[1]]
#                total=first+second
#                firsterror=psubprobT[list[0]]
#                seconderror=psubprobT[list[1]]
                
                
#            s1w1=psubprobT[0][3]/2
#            s2w1=psubprobT[1][3]/2
#            s3w1=psubprobT[2][3]/2
#            s4w1=psubprobT[3][3]/2
#            s1w2=nsubprobT[0][3]/2
#            s2w2=psubprobT[1][3]/2
#            s3w2=psubprobT[2][3]/2
#            s4w2=psubprobT[3][3]/2
#            log1=math.log(max(s1w1,epsilon)/max(s1w2,epsilon))
#            print log1
#            log2=math.log(max(s2w1,epsilon)/max(s2w2,epsilon))
#            print log2
#            log3=math.log(max(s3w1,epsilon)/max(s3w2,epsilon))
#            print log3
#            log4=math.log(max(s4w1,epsilon)/max(s4w2,epsilon))
#            print log4
#            loglikely=log1+log2+log3+log4
      

##Log likelyhood ratio

      
        data_set=[0,1,1,0]
        p=len(data_set)
        data=np.zeros((p,p),dtype=np.float)
        for i in range(0,p):
            for j in range(0,p):
                data[i][j]=data_set[j]
        prob_sum=0
        for j in range(0,4):
            p=prob[j][0]
            k=prob[j][1]
            r=max(data[j][p]+data[j][k],epsilon)
            if((data[j][p]==0)and(data[j][k]==0)):
                a=max(psubprob[j][0]/r,epsilon)
                b=max(nsubprob[j][0]/r,epsilon)
            if((data[j][p]==0)and(data[j][k]==1)):
                a=max(psubprob[j][1]/r,epsilon)
                b=max(nsubprob[j][1]/r,epsilon)
            if((data[j][p]==1)and(data[j][k]==0)):
                a=max(psubprob[j][2]/r,epsilon)
                b=max(nsubprob[j][2]/r,epsilon)
            if((data[j][p]==1)and(data[j][k]==1)):
                a=max(psubprob[j][3]/r,epsilon)
                b=max(nsubprob[j][3]/r,epsilon)
#            print a
#            print b
#            print math.log(a/b)
            prob_sum=prob_sum+math.log(a/b)
        print prob_sum        
            
#        model = Model(GetCurrentPath() + '/Models/ProbabilityTables.pkl')    
#        model.read()  
#        model.write()
#        
    
        
                
        
        
       
       

