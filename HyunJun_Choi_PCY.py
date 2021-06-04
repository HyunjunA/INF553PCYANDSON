'''
Created on Jan 8, 2018

@author: User

INF 553 Task 1 code
'''
import sys
import re
import itertools
import os
import errno


from collections import Counter
from operator import itemgetter
def keyfunction(x):
    v=x
    
    return (v)

def main():
    script = sys.argv[0]
    filename = sys.argv[1]
    aCons = sys.argv[2]
    bCons = sys.argv[3]
    NCons = sys.argv[4]
    sTh = sys.argv[5]
    outputDir = sys.argv[6]

#     filename = "C:/Users/User/workspace/Hello_Test/src/basketsLecture.txt"
#    filename = "C:/Users/User/workspace/Hello_Test/src/baskets.txt"
#    outputDir = "output-dir"
#    aCons = "6"
#    bCons = "7"
    
#     NCons = "10000000"
#    NCons = "100000" 
#     sTh = "11452"
#    sTh = "90000"
    
    f = open(filename, 'r')
    
    numText=f.read()
    numTextSplitL=numText.splitlines()
    numTextExB = numText.replace('\n',',' )
    
    wordcount = Counter(numTextExB.split(","))

    i=0
    candPair=[]
    prunedCandPair=[]
    realCandPair=[]
    for (key,value) in sorted(wordcount.items()): 
        i+=1
        
        if value>=int(sTh):
            value=1
        else:
            value=0
            
            
        key=int(key)
        
        if i==1:
            tempFirstKV=[(key,value)]
        
        if i==2:
            tempSecondKV=(key,value)
            kv=tuple(list(tempFirstKV)+[tempSecondKV])
            
        if i>=3:
            tempSecondKV=(key,value)
            kv=tuple(list(kv)+[tempSecondKV])
        
    kv=list(kv)
    
    kv.sort(key=lambda x:x[0])
    
    """    
    for(key,value) in kv:
        print (key,value)
    """
    
    #Count Table
#     freqOneBitmap=kv
    freqOneBitmap=[]
    nonfreqOneBitmapKey=[]
    realNonFreqCandPairCount=[]
    
    for (key,value) in kv:
        if value==0:
            nonfreqOneBitmapKey.append(key)
            
        else:
            freqOneBitmap.append(key)
    
            
#     for subset in itertools.combinations(freqOneBitmapKey, 2):
#         print(subset)
#         aTemp=list(subset,0)
#         candPair=kv=tuple(list(candPair)+[aTemp])


    intA = int(aCons) 
    intB = int(bCons)
    intN = int(NCons)

    hashTable=[0]*intN
    
#     for index in range(0,intN):
#         hashTable.append(0)
#         
        
        
    ############################################################################################################
    

    #Implementing HashTable 
    for lineNum in range(0,len(numTextSplitL)):
        listItemInEachBasket=map(int, numTextSplitL[lineNum].split(','))
        
        
        
        for subset in itertools.combinations(listItemInEachBasket, 2):

            h=(intA*int(subset[0])+intB*int(subset[1]))%intN
            hashTable[h]=hashTable[h]+1
    
    
    
    
    #######################################################################################################################    
        
    #Implementing HashTable-Bitmap
    for indexJ in range(0,intN):
        if hashTable[indexJ]>=int(sTh):
            hashTable[indexJ]=1
            
            
        else:
            hashTable[indexJ]=0
            
            
            
            
    eachLineLen=0
    totalNumOfPairs=0
#     subset=[]
    
    #Basket pairs Count         
    for lineNum in range(0,len(numTextSplitL)):
        
        
        
        listItemInEachBasket=map(int, numTextSplitL[lineNum].split(','))

        listItemInEachBasket=sorted(listItemInEachBasket)
        
        eachLineLen=len(listItemInEachBasket)
        
        totalNumOfPairs+=(eachLineLen*(eachLineLen-1))/2
        
        
        listItemInEachBasket=set(listItemInEachBasket).difference(nonfreqOneBitmapKey)

        listItemInEachBasket=sorted(listItemInEachBasket)
        
        for subset in itertools.combinations(listItemInEachBasket, 2):
            
#             print(subset)
            
            #fisrt, count Table pass
            if set([])==set(subset).intersection(nonfreqOneBitmapKey):
                
                h=(intA*int(subset[0])+intB*int(subset[1]))%intN
                
                
                
#                 hashTable[h]=hashTable[h]+1    
                if hashTable[h]==1:
                    if subset[0]> subset[1]:
                        subset=list(subset)
                        tempB=subset[0]
                        tempF=subset[1]
                        subset[0]=tempF
                        subset[1]=tempB
                        
                        subset=tuple(subset)
                    
                        
                    aTemp=(subset,0)
                    candPair=tuple(list(candPair)+[aTemp])   
                    candPair=set(candPair)
#                     print hashTable[h]
        
                #second, by using hash, prune
                else:
                    if subset[0]> subset[1]:
                        subset=list(subset)
                        tempB=subset[0]
                        tempF=subset[1]
                        subset[0]=tempF
                        subset[1]=tempB
                        
                        subset=tuple(subset)
                    
                    aTemp=(subset)
                    prunedCandPair=tuple(list(prunedCandPair)+[aTemp]) 
                    prunedCandPair=set(prunedCandPair)  
#                     print hashTable[h]
     
     
    
        
    #print "1"
    
    candPair=set(candPair)
    candPair=list(candPair)
    #candidate pairs that pass count table and hash table 
    candPair.sort(key=lambda x:(x[0][0],x[0][1]))


    
    prunedCandPair=set(prunedCandPair)
    prunedCandPair=list(prunedCandPair)
    #prunded Candidate Pair
    prunedCandPair.sort(key=lambda x:(x[0],x[1]))
    
    
    
    
  
    
    ###################################################################################################################
    #Basket pairs Count         
    for lineNum in range(0,len(numTextSplitL)):
        
        
        
        listItemInEachBasket=map(int, numTextSplitL[lineNum].split(','))
        
        listItemInEachBasket=set(listItemInEachBasket).difference(nonfreqOneBitmapKey)

        listItemInEachBasket=sorted(listItemInEachBasket)
        
        for subset in itertools.combinations(listItemInEachBasket, 2):
            
#             print(subset)
            
            if subset[0]> subset[1]:
                subset=list(subset)
                tempB=subset[0]
                tempF=subset[1]
                subset[0]=tempF
                subset[1]=tempB
                subset=tuple(subset)
            
            
            
            #fisrt, count Table pass
            if set([])==set(subset).intersection(nonfreqOneBitmapKey):
                for indexC in range(0, len(candPair)):
                    if subset==candPair[indexC][0]:
                        
                        candPair[indexC]=list(candPair[indexC])
                        
                        candPair[indexC][1]=candPair[indexC][1]+1
                        break
#                     print "1"
#                 print "1"
#             print "1"           
#         print "1"        
#     print "1"
     
    for indexC in range(0, len(candPair)):
        if candPair[indexC][1]>=int(sTh):
            
#             realCandPair[indexC]=candPair[indexC]
            
            #pair and count 
#             aTemp=candPair[indexC]
#             realCandPair=tuple(list(realCandPair)+[aTemp]) 
            
            
#             pair  
            aTemp=candPair[indexC][0]
            realCandPair=tuple(list(realCandPair)+[aTemp])  

        else:
            aTemp=candPair[indexC]
            realNonFreqCandPairCount=tuple(list(realNonFreqCandPairCount)+[aTemp])
                      


    if not os.path.isdir(outputDir):
         os.mkdir(outputDir)

    freOut=outputDir+'/'+'frequentset.txt'
    frequentTXT=open(freOut,'w')

     
     
     
    candOut=outputDir+'/'+'candidates.txt'
    candidatesTXT=open(candOut,'w')




            
    #print "frequent"

    for indexA in range(0,len(freqOneBitmap)):
         #print freqOneBitmap[indexA]
         frequentTXT.write(str(freqOneBitmap[indexA]))
         frequentTXT.write('\n')
         
    for indexNj in range(0,len(realCandPair)):
         #print realCandPair[indexNj]

         tempStr=str(realCandPair[indexNj])
         tempStr=tempStr.replace(" ", "")
        
         frequentTXT.write(tempStr)
         frequentTXT.write('\n')

    frequentTXT.close()
    


#     print "False Positive Set"
# 
#     for indexHQ in range(0,len(realNonFreqCandPairCount)):
#          print realNonFreqCandPairCount[indexHQ]
#  




    #print "candidates"

    for indexB in range(0,len(prunedCandPair)):
         #print prunedCandPair[indexB]

         tempStr=str(prunedCandPair[indexB])
         tempStr=tempStr.replace(" ", "")
        
         candidatesTXT.write(tempStr)
         candidatesTXT.write('\n')
         
    candidatesTXT.close()




    


     
         
         
    
    
    
    
    
    
    
    
    fp=float(sum(hashTable))/len(hashTable)
     
    print ("False Positive Rate: %.3f" %(fp))
    
#    print "1"
#     print f.read()
    
    
    
if __name__ == '__main__':
    main()
