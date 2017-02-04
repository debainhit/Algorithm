#-*-utf-8-*-
def InsertSort(array):
    for i in range(len(array)):
        tmp = array[i]
        index = i#!!!!!!
        for j in range(i-1,-1,-1): #!!!!!!!!!!!!!
            if array[j]>tmp:
                array[j+1] = array[j]
                index = j
            else:
                break
        array[index] = tmp
    return array
def BubbleSort(array):
    for i in range(len(array)):
        for j in range(i-1,-1,-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1],array[j] #!!!!!!!!!!!!
            else:
                break # ......
    return array



def ShellSort(array):
    n = len(array)
    gap =n//2
    while gap:
        for i in range(gap,n):
            j = i
            tmp = array[j]
            while(j>=gap and array[j-gap]>tmp):
                array[j] = array[j-gap]
                j = j-gap
            array[j] = tmp
        gap = gap//2
    return array

def SelectSort(array):
	for i in range(len(array)):
		index = i
		cur = array[i]
		for j in range(i+1,len(array)):
			if array[j] <cur:
				cur = array[j] 
				index = j
		array[i],array[index] = array[index],array[i]
	return array

def QuickSort(array,left,right):
    if left>=right:
    	return array
    tmp = array[left]
    i,j = left,right
    while i<j:
    	while j>i and array[j]>=tmp:
    	    j -=1
    	while j>i and array[i]<=tmp:
    		i +=1
    	array[i],array[j]= array[j],array[i]
    array[left],array[i] = array[i],array[left]
    QuickSort(array,left,i-1)
    QuickSort(array,i+1,right)
    return array

def mergesort(array):
	if len(array)<=1:
		return array
	mid = len(array)//2
	left = mergesort(array[:mid])
	right= mergesort(array[mid:])
	return merge(left,right)
def merge(left,right):
	new = []
	i = 0
	j =0
	while i<len(left) and j<len(right):
		if left[i]<right[j]:
			new.append(left[i])
			i +=1
		else:
			new.append(right[j])
			j+=1
	new += left[i:]
	new += right[j:]
	return new
def heapsort(array):
	n = len(array)
	first = len(array)//2
	for start in range(first,-1,-1):
		maxheap_adjust(array,start,n-1)
	#print(array)
	for end in range(n-1,0,-1):
		array[end],array[0]=array[0],array[end]
		maxheap_adjust(array,0,end-1)
	return array

def maxheap_adjust(array,start,end):
	root = start
	while 1:
		child = root*2+1
		if child>end: break
		if child+1<=end and array[child]<array[child+1]:
			child = child+1
		if array[root]<array[child]:
			array[root],array[child]= array[child],array[root]
			root = child
		else:
			break

kk = [3,8,6,7,9,1,10,2]
kkk = heapsort(kk)
print(kkk)

# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput,k):
        # write code here
        n = len(tinput) -1
        first = (k-1)//2
        for start in range(first,-1,-1):
            self.maxheapajust(tinput,start,k-1)
        print(tinput[0:k])
        print("sbbbb")
        for i in range(k,n+1,1):
            print(".....")
            print(tinput[i])
            print(tinput[0])
            print("....")
            print(tinput)
            if tinput[0]>tinput[i]:
                tinput[0],tinput[i]=tinput[i],tinput[0]
                self.maxheapajust(tinput,0,k-1)
            else:
            	continue
        m = tinput[0:k]
        m.sort()
        print m
    def maxheapajust(self,array,start,end):
        root = start
        while 1:
            child = 2*root+1
            if child>end: break
            if child+1<=end and array[child] <array[child+1]:
                child = child + 1
            if array[root]<array[child]:
                array[root],array[child] = array[child],array[root]
                root = child 
            else:
                break
          
kk = [4,5,1,6,2,7,3,8,0]
ss = Solution()

res = ss.GetLeastNumbers_Solution(kk,4)