arr=[1,2,3,4,5,6,7]
# Binary Search

def bin(arr,x):
	low=0
	high=len(arr)-1
	mid=((low+high)//2)
	while low<=high:
		mid=((low+high)//2)
		# print(arr[mid])
		if x>arr[high] or x<arr[low]:
			return -1
		else:
			if x==arr[mid]:
				return mid
			elif x<arr[mid]:
				high=mid-1
			else:
				low=mid+1

	return -1


