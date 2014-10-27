inv = 0

def countInversion(n):
    global inv    # Needed to modify global copy of inv
    inv += n

def inversion(fHalfArray, sHalfArray):
	i = 0
	j = 0
	finalArray = []

	while i < len(fHalfArray) and j <len(sHalfArray):
		if fHalfArray[i] > sHalfArray[j]:
			countInversion(len(fHalfArray[i:]))
			finalArray.append(sHalfArray[j])
			j += 1
		else:
			finalArray.append(fHalfArray[i])
			i += 1

	finalArray += fHalfArray[i:]
	finalArray += sHalfArray[j:]

	return finalArray

def mergeSort(unsortedArray):
    sortedArray = []

    if len(unsortedArray) < 2:
        return unsortedArray
    
    mid = int(len(unsortedArray)/2)

    firstHalfArray = mergeSort(unsortedArray[:mid])
    secondHalfArray = mergeSort(unsortedArray[mid:])
    sortedArray = inversion(firstHalfArray, secondHalfArray)
    
    return sortedArray

#Execution
x = [1,3,5,2,4,6]
mySortedArray = mergeSort(x)
#print sortArray
print inv