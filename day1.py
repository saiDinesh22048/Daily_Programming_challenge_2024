def sortlist(List):
    l=List.count(0)
    m=List.count(1)
    h=List.count(2)
    for i in range(len(List)):
        if l>0:
            List[i]=0
            l=l-1
            continue
        if m>0:
            List[i]=1
            m=m-1
            continue
        if h>0:
            List[i]=2
            h=h-1
    return List
newlist=sortlist([1,2,0,0,2,1,1,2])
print(newlist)
