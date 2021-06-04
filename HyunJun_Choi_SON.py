
from __future__ import unicode_literals

from __future__ import print_function


from pyspark import SparkContext
from operator import add
from itertools import groupby
from collections import Counter



import sys
import re
import string
import os.path
import os
import operator
import itertools

import collections

def extr(x):
    """x = x.encode('ascii', 'ignore').decode('ascii') """
    """print(x)"""


    "For apostrophe and dash, you simply remove it (without replacing it with space)."
    key=re.sub("'","",x)
    key=re.sub("-","",key)


    
    
    x=re.sub(r'[^\x00-\x7F]+','', x)
    x=x.lower()

    idNum=x.split(',')[0]
    key=x.split(',')[3]
    

    pageCount=x.split(',')[18]
    
    """print("%s %s" % (key, pageCount))"""

    
    
    """if {(key!='') | (idNum !='i')}:"""
    "Lower-case the tokens."
        
    """key=key.encode('utf-8')"""
    """key = key.encode('ascii', 'ignore').decode('ascii')"""
    key=key.lower()
        
        

    "For apostrophe and dash, you simply remove it (without replacing it with space)."
    "origin"
    "-||'"
    key=re.sub("'","",key)
    key=re.sub("-","",key)
    
    "Replace all punctuation characters (except for apostrophe ' and dash -) in the event value with white spaces. "
    removePun= string.punctuation
    patternPun = r"[{}]".format(removePun)
    
    key=re.sub(patternPun," ",key) 
    
    "If there are continuous multiple white spaces within the text, consider them as a single space and then tokenize."
    key=re.sub(" +"," ",key)
    
    "Remove leading and trailing white spaces if any."
    key=key.strip()

                                        

    """if (key!="") and (key!="event") and (idNum !="id") and (pageCount!="page_count"):"""

    """print("%s %i" % (key, int(pageCount)))"""
    """print("%s %s" % (key, pageCount))"""

    """if (key!="") """
         

    if (key=="event") and (idNum =="id") and (pageCount=="page_count"):
        pageCount='0'
        
    intPageCount=int(pageCount)

    return(key,intPageCount)


def summa(iterator):
    add,count=0,0
    for (k,v) in iterator:
        add += v
    
    yield (k,add)

   

def printf(part):
    print (list(part))



def printPartBasket(part):
    tempL=len(part)

    print ("%d" %(tempL))


def numByKey(part):
    
    
    
     
    
   
    "part=list(part)"

    "partiLen=len(part)"

    "partiLen=part.count() "


        



    part=list(part)  

    "print(part)"
    data=[]
    eachLineElement=[]
    ibasketNum=0

    
    for key,value in part:
    
    
        
        ibasketNum=ibasketNum+1

        supRatio=float(value)

    
        eachLineElement+=(key.split(','))
        
            

    

        """
        eachLineElementSet=set(eachLineElement)
        
        """

        "eLen=len(eachLineElementSet)"
            
        
    
        
        """
        for index in range(0,list(a)):
            data = [(key, val) for (key, val) in a]
        """

        """
        print (part[0])
        """
       
        """ 
        print (eachLineElement)     
        """
     
        """
        print (eachLineElementSet)  
        print (eLen)
        """

    "print(part)"
 
    countEachElement=Counter(eachLineElement).items()

    "print(countEachElement)"
    
    indexA=-1
   
    localSupThre=float(supRatio)*(ibasketNum)    
    
    "print (localSupThre)"
    "Making freqent one set" 

    
    freqOne=[]
    for (key,count) in countEachElement:
        indexA+=1
        
        """
        print ((float(supRatio)*(ibaketNum)))
        """
        "print (key,count)"
        if count >= localSupThre:
        
            freqOne+=[int(key)]
            
    freqOne=sorted(freqOne)     

     
    "print (freqOne)"
    

    
    "Tri=0"
    sizeSet=0
    countSubsetInPar=0


    currentFre=[]

    """

    while Tri==1
        sizeSet+=1
        
        "Checking frequency from pair to "
        for subset in itertools.combinations(freqOne,sizeSet):
            countSubsetInPar=0
            for bID in range(0,ibasketNum): 
                if set(part[bID]).intersection(subset)!=set([]):
                    countSubsetInPar+=1
                    print(part[bID])
                    
    """
    tempIncreasingSet=[]
    localFreq=[]
    element=[]
    tempIncreasingSet=freqOne
    localFreq+=freqOne
    

    check=1
    candAllList=[]
    candAllListLen=0
    
    numOfpassExam=1    

    """
    for indT in range(0,len(freqOne)):
        
        yield(freqOne,1)

    """


    "while sizeSet<10:"
    while numOfpassExam!=0:
        sizeSet+=1
    
        element=[]
        check=0
    
        
        numOfpassExam=0

        
            
        tea= list(itertools.combinations(tempIncreasingSet,sizeSet))
        
        
        for subset in itertools.combinations(tempIncreasingSet,sizeSet):
            "subset=list(subset)"

            countSubsetInPar=0
            
            "print(subset)"

            for bID in range(0,ibasketNum):
                "print(part[bID])"
            
                
                tempFS=sorted(subset)
            
                
                 
                "tempFS=set(tempFS)"

                tempBS=eval(part[bID][0])
                if type(tempBS)==type(int()):
    
                    tempBS=[tempBS]
                    "print(type(tempBS))"
                
                if type(tempFS)==type(int()):
                    tempFS=[tempFS]

    
                b3 = [val for val in tempFS if val in tempBS]
                
                               
                b3=list(b3)
                b3=sorted(b3)
                "print ('b3' )"  
                "print (b3)"
            
                "print (tempFS)"
                "print (part[bID][0])"
                "Tri=1"

                "print(tempBS)"
                "tempInter=set(tempFS) & set(b3) "
                if ((tempFS)==(b3)):
                    
                    countSubsetInPar+=1
                    check=1
                
                    "print ('same')"
                    "print (tempInter)"
                


                    
                    "print((tempFS))"
                    "print(b3)"
                    

                    "print(subset,countSubsetInPar)"
            
                    "print(part[bID][0])"

                    "print (ibasketNum*float(supRatio))"

    
            if (countSubsetInPar >= localSupThre):

                numOfpassExam+=1
            
        
                "Tri=0"
                "print(sorted(subset),countSubsetInPar)"
                "freqOne+=(sorted(subset),countSubsetInPar)"
                currentFre+=[tuple(sorted(subset))]
                element+=list(subset)
                "print(currentFre)"
                
                a=[(subset,countSubsetInPar)]
            
        
                "yield(subset,countSubsetInPar)"
                yield(subset,1)
                "print(freqOne)"

        localFreq+=(currentFre)
        "print(list(set(localFreq)))"
        tempIncreasingSet=currentFre
        "print (element)"
        element=sorted(list(set(element)))
        "print (element)"
        
        tempIncreasingSet=element
        "print (element)"
        
    "print(freqOne)"
    
    currentFre=freqOne+currentFre    
    "print(sorted(list(set(localFreq))))"
    

    "yield(sorted(list(set(localFreq))))"
    
    

    "print (ibasketNum*float(supRatio))"
    s=[]
    s=tuple(localFreq)
    
    "s=sorted(s,key=len)"
    "print((s))"



    """
    print (freqOne)
    """

    """print ("The number of baket in each partition:%d" %(ibaketNum))"""

    

    

    
    "supThres=(float (ibasketNum)*(supRatio))"
    
    """
    print("supThreshoul:%f" %(supThres))
    """
    """
    for key, grp in groupby(sorted(part), key=operator.itemgetter(0)):
        "print (key,map(operator.itemgetter(1),grp))"

        summa=sum(map(operator.itemgetter(1),grp))

        summa=summa*10

        if (summa > supThres ):
            "yield (key,int(summa))"
        
    """


    




def checkItem(part):
 

    candVic=[] 
    "print(part[1][0][0])"

    part=list(part)
    
    "print(part)"
    
    lenPart=len(part)

    for indTeP in range(0,lenPart):
        eachBasket=part[indTeP][0]
        allCandi=part[indTeP][1]


    


        partNum=len(allCandi)
        "print(partNum)"
        
        for indj in range(0, partNum):
            
            "print(allCandi[indj])"
            
            eachPartCand=allCandi[indj]

            "print(type(eachPartCand))"
            "print(localFreqSet)"
            first=localFreqSet
            """
            if type(eachPartCand)==type(int()):
                eachPartCand=[eachPartCand]
            
            if type(eachPartCand)==type(tuple()):
                eachPartCand=[eachPartCand]
            """
            
            eachPartCand=[eachPartCand]
         
            eachPartCandLen=len(eachPartCand)
            
            "print('index')"
            "print(indj)"
            "print('eachCan')"
            "print(allCandi[1])" 
            
            for idxB in range(0,eachPartCandLen):
                
                if len(eachBasket)==1:
                    eachBasketList=[int(eachBasket)]                

                if len(eachBasket)!=1:
                    eachBasketList=list(eval(eachBasket))
                 
                
                if type(eachPartCand[idxB])==type(int()):
                
            
                    found=True
                    """
                    print(eachBasketList)
                    print(eachPartCand[idxB])
                    """

                    try: eachBasketList.index((eachPartCand[idxB]))
                    except ValueError: found = False  
                    
                    if found==True:
                        """ 
                        print('int True')
                        print((eachPartCand[idxB],1))
                        """
                        
                        teTup=(str(eachPartCand[idxB]),1)
                        "print(teTup)"
                        yield(teTup)
                        
                        "candVic+=[str(eachPartCand[idxB])]"
                         
                        "candVic+=[(str(eachPartCand[idxB]),1)]"
                        "candVic+=([str(eachPartCand[idxB]),1])"
                  
                        "yield(eachPartCand[idxB],1)"
        
                if type(eachPartCand[idxB])==type(tuple()):
                
            
                    """
                    print(eachBasketList)
                    print(eachPartCand[idxB])
                    """
                    
                    eachPartCandConvertedToList=list(eachPartCand[idxB])
                    "print ('tuple')"
                    
                    checkEachTupleCount=0
                    for indU in range(0,len(eachPartCandConvertedToList)):
                        "checkInd=eachBasketList.index(eachPartCandConvertedToList[indU])"
                        found=True

                        try: eachBasketList.index(eachPartCandConvertedToList[indU])
                        except ValueError: found = False

                        if found==True:
                            
                            checkEachTupleCount+=1
                    

                    if checkEachTupleCount==len(eachPartCandConvertedToList):
                        
                        "print((eachPartCand[idxB],1))"
                        "return((eachPartCand[idxB],1))"
                        "candVic+=[(str(eachPartCand[idxB]),1)]"
                           
                        
                        teJo=",".join(map(str,eachPartCand[idxB]))  
                                       
                        teTup=(teJo,1)
            
                        yield(teTup)
                        "candVic+=[str(eachPartCand[idxB])]"
                    
                    "candVic+=([str(eachPartCand[idxB]),1])"
                    "yield(eachPartCand[idxB],1)"
                "return(tuple(eachPartCand[idxB],1))"
                 
            
            """
            "inter=[set(eachBasketList).intersection(eachPartCandList)]"
            print ('eachBasketList') 
            print (eachBasketList)
            
            print ('eachPartCandList')
            print (type(eachPartCandList))

            print('inter')
            print (inter)
            "print (CheckPoint')"
            """
    
            
            """
            found=True
            try: eachBasketList.index((eachPartCand[idxB]))
            except ValueError: found = False
            """
            
        
                
            

            "print('key')"
            "print(eachPartCand[idxB])"            


            """    
            if found==False:
                print("Falsue")
                print(eachPartCand[idxB])
                print(eachBasketList)

            if found==True:
                print('True')
                "print(idxB)"
                print(eachPartCand[idxB])
                "yield ((eachPartCand[idxB],1))"
            """

            "print ('start')"
            "ind = [(i,x) for i,x in enumerate(test) if x== eachPartCand[idxB]]"
            
            "t = set(test).intersection(set(eachPartCand[idxB]))"
            
            "print (t)"   
                
            "if t=="
            "yield ((eachPartCand[idxB],1))"


    "print('candVic!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')"
    "print(candVic)"

    """
    total=[]
    total=('a',list(candVic))    
    
    return(total)
    """

def cle(part):
    
    print(part)
    print(len(part))
    
    """
    for index in range(0, len(part)):
        print(part[index]) 
    """    

def keyVa(part):

        
    return(part[0],1)

def lenSort(x):
    v=x[0]
    
    if type(v)==type(int()):
        v=[v]

    """
    print("lenSort \n")
    print(v)
    """
    return (len(v))

def valueSort(x):
    v=x
    """
    print("valueSort \n")
    print(x)
    """
    return (v)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: HyunJun_Choi_SON.py <Input file> <support ratio> <output file>", file=sys.stderr)
        exit(-1)


    sc = SparkContext(appName="inf553")
   


    "The number of partitions"
    numOfPart=2

    "Input file: baskets.txt"
    lines = sc.textFile(sys.argv[1],numOfPart)
    
    totalFile =sc.textFile(sys.argv[1])
    "lines.foreachPartition(printPartBasket)"

    "Support thereshol"
    totalNumOfBaskets=lines.countByKey()
    
    "print(totalNumOfBaskets)"
    supportRatio=sys.argv[2]
    
    "supportRatio=float(supportRatio)"
    
    "globalSupportThre=float(totalNumOfBaskets[1])*(supportRatio)"
    
    """ 
    print ("%.3f" %(supportRatio))
    """ 
    
    "Writing result in output-dir"
    cwd=os.getcwd()

    direc = sys.argv[3]
    
    """
    if not os.path.exists(direc):
        os.makedirs(direc)
    """

    """
    outputFileName="output.txt"
    """
    
    """
    realAddr=direc+"\\"+outputFileName
    """

    """String whiteSpaceRegex="\\s";"""
    """
    realAddr=realAddr.replace("\\","\\")
    """

          

    "Phase 1"
    firstPass = lines.flatMap(lambda x: x.split(', |')) \
                    .map(lambda x:((x),float(supportRatio)))\
                    .mapPartitions(numByKey)\
                    .groupByKey()\
                    .mapValues(list)\
                    .map(keyVa)


                        
    
    first=firstPass.collect()
 
    totalCL=[]

    for indX in range(0,len(first)):
        cL=first[indX][0]

        if len(cL)==1:
            cL=" ".join(map(str,cL))
            cL=int(cL)
        
        totalCL.append(cL)
         
    

    localFreqSet=totalCL
    
    localFreqSet=set(localFreqSet)
     
    "Phase 2"
    globalFre = lines.flatMap(lambda x: x.split(', |'))\
                    .map(lambda x:((x), list(localFreqSet)))\
                    .mapPartitions(checkItem)\
                    .groupByKey()\
                    .mapValues(list)    

    
    """
    localFreqSet=set(first[0])
    for indFi in range(0, len(first)):
        localFreqSet=localFreqSet.union(first[indFi])
        
    


    globalFre = totalFile.flatMap(lambda x: x.split(', |'))\
                    .map(lambda x:((x), list(localFreqSet)))\
                    .map(checkItem)\
                    .groupByKey()\
                    .mapValues(list)
    

    """    





















    """                
                    \
                    .reduceByKey(fiCheck)

    """          
                           

    """
                
                \
                .foreachPartition(printf)
    """
                

 
    """
    counts = lines.flatMap(lambda x: x.split(',')) \
                .map(lambda x:(x,1))\
                .foreachPartition(printf)
    """
    



    
    """
    counts = lines.flatMap(lambda x: x.split(',')) \
                .map(lambda x:(x,1))\
                .reduceByKey(add)\
                .sortByKey()
    
    """




    """
    counts = lines.flatMap(lambda x: x.split(', |')) \
                .map(extr)\
                .groupByKey()\
                .map(lambda x:(x[0],list(x[1],len(list(x[1])))))\
                .sortByK
    """




    "output = firstPass.collect()"
    
       
    output = globalFre.collect()
    
    "output=first"
    

    
    
    """
    print (len(output[0][1]))
    
    
    tempList=[]
    
    for index in range(0,len(output[0][1])):
        tempList+=list(set(output[0][1][index]))      
    
    tempList=sorted(tempList)
    
    counter=collections.Counter(tempList)
    
    print(counter)

 
    localFreq=[]


    temSup=float(supportRatio)
    tempNumB=totalNumOfBaskets['1']
    
    
    min_SupportThreshold=(int(tempNumB))*(temSup)
    
    print(min_SupportThreshold)
    
    for key,cnts in list(counter.items()):
        if cnts < min_SupportThreshold:
    
            del counter[key]    
 
    print(counter)

    """
    
    temSup=float(supportRatio)
    tempNumB=totalNumOfBaskets['1']


    min_SupportThreshold=(int(tempNumB))*(temSup)


        
    "print (min_SupportThreshold)"
        

    """    
    outputFile=open(direc+'//'+outputFileName,'a')
    """

    outputFile=open(direc,'a')


    "output.sort(key=lamb"

    "output=sorted(output,key=keySeFun)"
    
    "-------------------------------------------"
    "output=sorted(output,key=valueSort)"
    "output=sorted(output,key=lenSort)"
    
    tempKC=[]
    
    for(key,count) in output:
        "print (type(key))"
        key=eval(key)
        tempKC.append((key,count))

    "------------------------------------------"

    output=tempKC
    output=sorted(output,key=valueSort)
    output=sorted(output,key=lenSort)



    for (key,count) in output:
        
        sumCount=(sum(count))
        if type(key)==type(int()):
            key=[key]        


        if len(key)==1:
            key=" ".join(map(str,key))

        strKey=str(key)
        

        if len(strKey)<=2:
            if sumCount >=min_SupportThreshold:
                strKey=strKey.replace(" ","")        
    
                outputFile.write(strKey+'\n')
        if len(strKey)>2:
            if sumCount >=min_SupportThreshold:    
                "strKey='('+strKey+')'"
                strKey=strKey.replace(" ","")

                outputFile.write(strKey+'\n')
        
    outputFile.close()
    
    

    
    "print(output)"

    
    """
    for (a,v) in output:
        print(a)
    """

    sc.stop()
