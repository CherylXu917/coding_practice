"""
Input: [1, 2, [3, 4, [5], [], 6], [7, 8], 9]
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
"""

def flat_array(arr):
    res = []
    for num in arr:
        if isinstance(num, int):
             res.append(num)
             continue
        tmp = flat_array(num)
        res += tmp
    return res


def flat_array2(arr):
    """
    complexity: O(m * n), where m is the maximum depth of the inner array
    :param arr:
    :return:
    """
    res = arr
    is_finish = False
    while not is_finish:
        is_finish = True
        tmp = []
        for num in res:
            if isinstance(num, int):
                tmp.append(num)
                continue
            is_finish = False
            for e in num:
                tmp.append(e)
        res = tmp
    return res


def flat_array3(arr):
    """
    complexity: O(n + m), where m is total depth of the inner array
    :param arr:
    :return:
    """
    res = []
    cur = arr
    is_finish = False
    while not is_finish:
        is_finish = True
        for i in range(len(cur)):
            if isinstance(cur[i], int):
                res.append(cur[i])
                continue
            cur = cur[i] + cur[i + 1:]  # complexity is O(N + M)
            is_finish = False
            break
    return res

def flat_array4(arr):
    res = []
    stack = [arr]
    while stack:
        cur = stack.pop()
        for i, num in enumerate(cur):
            if isinstance(num, int):
                res.append(num)
                continue
            stack.append(cur[i + 1:])
            stack.append(num)
            break
    return res

def flatten(arr):
	stack = []
	res = []
	n = len(arr)

	for i in range(n - 1, -1, -1):
		stack.append(arr[i])

	print (stack)

	while stack:
		cur = stack.pop(-1)
		# print stack
		if isinstance(cur, int):
			res.append(cur)
			continue
		m = len(cur)
		for i in range(m - 1, -1, -1):
			stack.append(cur[i])

	return res

if __name__ == '__main__':
    arr = [1, 2, [3, 4, [5], [], 6], [7, 8], 9]
    # print(flat_array(arr))
    # print(flat_array2(arr))
    print(flat_array3(arr))
    print(flat_array4(arr))