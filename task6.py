def solve(array):
    indexes = sorted(range(len(array)), key = lambda x:array[x])
    
    stack = []
    result = [-1] * len(array)

    for ind in indexes:
        while stack and ind < stack[-1]:
            stack.pop()
        if stack:
            result[ind] = array[stack[-1]]
        stack.append(ind)
    
    return result


if __name__ == "__main__":
    arr = [2, 3, 4, 5, 1]
    print(solve(arr))
