def GenerateBBSTArray(a):
	a.sort()
	result = []
	if not a:
		return result
	midPos = len(a)//2
	result.append(a[midPos])
	result = result + GenerateBBSTArray(a[:midPos]) + GenerateBBSTArray(a[midPos+1:])	
	return result
