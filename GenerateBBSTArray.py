def GenerateBBSTArray(a):
	a.sort()
	result = []
	if not a:
		return result
	midPos = len(a)//2
	result.append(a[midPos])
	result = result + GenerateBBSTArray(a[:midPos]) + GenerateBBSTArray(a[midPos+1:])	
	return result

def F(a,res,count):
    print("COUNT")
    print(count)
    print("RES")
    print(res)
    cont = True
    less = []
    greater = []
    x = a.index(res[count])
    if count == 0:
        less = a[:x]
        greater = a[x+1:]
        print("LESS =", less)
        res.append(less[len(less)//2])
        res.append(greater[len(greater)//2])
        count += 1
    else:
        
        if res[count] < res[0]:
            y = a.index(res[(count-1)//2])
            less = a[:x]
            greater = a[x+1:y]
            print("LESS =", less)
            print("GREATER =", greater)
            if less:
                res.append(less[len(less)//2])
            else:
                res.append(None)
            if greater:
                res.append(greater[len(greater)//2])
            else:
                res.append(None)
        else:
            y = a.index(res[(count-2)//2])
            less = a[y+1:x]
            greater = a[x+1:]
            print("LESS =", less)
            print("GREATER =", greater)
            if less:
                res.append(less[len(less)//2])
            else:
                res.append(None)
            if greater:
                res.append(greater[len(greater)//2])
            else:
                res.append(None)  
        count += 1
    print()
    if count < len(a)-1:
        return F(a,res,count)
    else:
        for i in range(res.count(None)):
            res.remove(None)
        return res

a = [1,2,3,4,5,6,7,8,9,10]
res = [6]
count = 0
