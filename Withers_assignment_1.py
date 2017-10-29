# Flatten function
def flatten(list):
    output = []
    for item in list:
        if type(item) == type([]):
            output.extend(flatten(item))
        else:
            output.append(item)
    return output    	

# Power set function
def powerset(list):
	output = [[]]
	for i in list:
		output.extend([x + [i] for x in output])
	return output

# All permutations function
def all_perms(list):
    if len(list) == 0:
        return []
    if len(list) == 1:
        return [list]
    newList = []
    for i in range(len(list)):
       remLst = list[:i] + list[i+1:]
       for p in all_perms(remLst):
           newList.append([list[i]] + p)
    return newList

# Number spiral function		
def spiral(n, end_corner):
	arr = range(n**2)
	spi = []
	spi = spiralNums(arr,n,spi)
	return spi
	
def spiralNums(list,n,arr):
	for i in range(4):
		if len(list) == 0:
			return arr	
		else:
			arr.append(list[-(n-1):])
			list = list[:-(n-1)]
	spiralNums(list,n-2,arr)
	return arr
	
#def spiralOrder(arr, corner, n):
#	list = []
#	if corner == 1:
#	if corner == 2:
#		list.append(arr[1][0] + arr[0])
		
		
		
		
			