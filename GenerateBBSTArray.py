def NodeCreator(a, result, point):
	print(point)
	print(result)
	if point == len(a)//2:
		return result
	less = []
	greater = []
	point_root = None
	root_root = None
	point_index = a.index(result[point])

	if point % 2 != 0:
		point_root = int((point-1)/2)
	else:
		point_root = int((point-2)/2)
	
	if point_root is not 0:
		if point_root % 2 != 0:
			root_root = int((point_root-1)/2)
		else:
			root_root = int((point_root-2)/2)

	else:
		point_root = len(a)//2
		if point % 2 != 0: 
			less = a[:point_index]
			print("LESS", less)
			greater = a[point_index+1:point_root]
			print("GREATER", greater)
			if less:
				result.append(less[len(less)//2])
			if greater:
				result.append(greater[len(greater)//2])
			point += 1
			return NodeCreator(a, result, point)
		else:
			less = a[point_root+1:point_index]
			print("LESS", less)
			greater = a[point_index+1:]
			print("GREATER", greater)
			if less:
				result.append(less[len(less)//2])
			if greater:
				result.append(greater[len(greater)//2])
			point += 1
			return NodeCreator(a, result, point)

	root_root = a.index(result[root_root])
	point_root = a.index(result[point_root])

	if result[point] < result[0]:
		if point % 2 != 0:
			less = a[:point_index]
			print("LESS", less)
			greater = a[point_index+1:point_root]
			print("GREATER", greater)
			if less:
				result.append(less[len(less)//2])
			if greater:
				result.append(greater[len(greater)//2])
			point += 1
			return NodeCreator(a, result, point)
		else:
			less = a[point_root+1:point_index]
			print("LESS", less)
			greater = a[point_index+1:root_root]
			print("GREATER", greater)
			if less:
				result.append(less[len(less)//2])
			if greater:
				result.append(greater[len(greater)//2])
			point += 1
			return NodeCreator(a, result, point)
	
	else:
		if point % 2 != 0:
			less = a[root_root+1:point_index]
			print("LESS", less)
			greater = a[point_index+1:point_root]
			print("GREATER", greater)
			if less:
				result.append(less[len(less)//2])
			if greater:
				result.append(greater[len(greater)//2])
			point += 1
			return NodeCreator(a, result, point)
		else:
			less = a[point_root+1:point_index]
			print("LESS", less)
			greater = a[point_index+1:]
			print("GREATER", greater)
			if less:
				result.append(less[len(less)//2])
			if greater:
				result.append(greater[len(greater)//2])
			point += 1
			return NodeCreator(a, result, point)

def GenerateBBSTArray(a):
	result = []
	less = []
	greater = []
	point = 0
	a.sort()
	pivot_point = None
	if a:
		pivot_point = len(a)//2
		result.append(a[pivot_point])
		less = a[:pivot_point]
		greater = a[pivot_point+1:]
		if less:
			result.append(less[len(less)//2])
		if greater:
			result.append(greater[len(greater)//2])
		point += 1

	return NodeCreator(a, result, point)
