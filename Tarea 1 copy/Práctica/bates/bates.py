from sys import stdin


def dict(fullCh): #Función para llenar el diccionario de la cadena grande.
    dictionary = {}
    for c in range(len(fullCh)-1):
        tmp = dictionary.get(fullCh[c])
        if tmp == None:
            listTmp=[c]
            dictionary[fullCh[c]]=listTmp
        else:
            values = dictionary[fullCh[c]]
            values.append(c)
            dictionary[fullCh[c]]=values
    return dictionary

def binarysearchGT(arr, lt):
    minV = 0
    maxV = len(arr)
    while minV + 1 < maxV:
        mid = (minV + maxV)>>1
        if lt >= arr[mid]: 
            minV = mid 
        else:
            maxV = mid
    ans=-1
    if ((arr[minV]<= lt) and ((minV + 1) < len(arr))):
        ans= arr[minV+1] 
    elif ((arr[minV]> lt) and (minV < len(arr))):
        ans= arr[minV]
    return ans

def findMatch(dictionary,fullCh, query):
    lp=-3
    c=0
    ans,first = None,None
    totalSize= len(query)-1
    while (lp != -1 and c < totalSize):
        dictt = dictionary.get(query[c])
        if (dictt != None):
            lp=binarysearchGT(dictt,lp)
            if (c == 0):
                first = lp
            if (lp != -1):
                c+=1
        else:
            lp = -1 
    if (c == totalSize):
        ans= "Matched"
    return (ans,first,lp)

def main():
    fullCh = stdin.readline() 
    inputT = int(stdin.readline())
    dictionary = dict(fullCh)
    while inputT!=0:
        query = stdin.readline()
        ans,first,last = findMatch(dictionary,fullCh,query)
        if ans: print('Matched {0} {1}'.format(first, last))
        else: print('Not matched')
        inputT -= 1

main()