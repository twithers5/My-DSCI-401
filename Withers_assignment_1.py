# Flatten function
def flatten(list):
    output = []
    for i in list:
        if type(i) == type([]):
            output.extend(flatten(i))
        else:
            output.append(i)
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
	#s = spiralOrder(spi,end_corner,n)
	#return 
	
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
#	matrix = []
#	for i in range(n):
#		list = []
#		for j in range(n):
#			list.append(j)
#		matrix.append(list)
# I made a matrix of random numbers to start off and I was going to somehow figure out
# how to replace those numbers with the numbers that I created in the spiralNums function.	
		
		
		
		
			