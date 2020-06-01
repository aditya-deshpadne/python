def merge(arr,aux,hi,low,mid):
    #copyarr
    for x in range(low,hi+1):
        aux[x]=arr[x]
    
    
    i=low
    j=mid+1
    for x in range(low,hi+1):
        if(j>hi):
            arr[x]=aux[i]
            i+=1
        elif(i>mid):
            arr[x]=aux[j]
            j+=1    
        elif(aux[i]<aux[j]):
            arr[x]=aux[i]
            i+=1
        else:    
            arr[x]=aux[j]
            j+=1
    
def sort(arr,aux,hi,low):
    if(hi<=low):
        return
    mid=(hi+low)//2
    sort(arr,aux,mid,low)
    sort(arr,aux,hi,mid+1)
    merge(arr,aux,hi,low,mid)

def less(i,j):
    return i<j

def msort(arr):
    aux=[0]*len(arr)
    sort(arr,aux,len(arr)-1,0)

def main():
    arr = [101,200,4,1,77,2,3,75,5,7,64,9,76,11,99,22,43]
    print("----- Unsored Array -----")
    print(arr)
    msort(arr)
    print("----- Sored Array -----")
    print(arr)

main()