#"QuickSort"


def partition(arr,hi,low):
    
    lo = arr[low]
    i = low+1
    j = hi;
    while(True):
            
        while(True):
            if(isless(lo,arr[i])):
                i+=1
            else:
                break
            if(i>hi):
                break
        
        while(True):
            if(isless(arr[j],lo)):
                j-=1;
            else:
                break;
            if(j<low):
                break
        
    
        if(i>=j):
            break
        exch(arr,i,j)    
    
    exch(arr,low,j)
    
    return j

def isless(i,j):
    return i > j
  

def exch(arr,i,j):
    temp = arr[i]
    arr[i]=arr[j]
    arr[j]=temp
   

def sort(arr,hi,low):
    if(hi<=low):
        return;
    j=partition(arr,hi,low);
    sort(arr,j,low);
    sort(arr,hi,j+1);
    

def qsort(arr):
    sort(arr,len(arr)-1,0)

def main():
    arr = [101,200,4,1,77,2,3,75,5,7,64,9,76,11,99,22,43]
    print("----- Unsored Array -----")
    print(arr)
    qsort(arr)
    print("----- Sored Array -----")
    print(arr)
    


main()
