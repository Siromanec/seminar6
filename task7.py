import timeit
from math import sqrt
class Solution():

    def solve(self, points: list):
        res = 0
        for p in points:
            cmap = {} #hash map
            for q in points:
                f = p[0]-q[0] # x1 - x2
                s = p[1]-q[1] # x1 - x2
                cmap[f*f + s*s] = 1 + cmap.get(f*f + s*s, 0) # compare distance squared
            for k in cmap:
                res += cmap[k] * (cmap[k] -1) # ways to shuffle
        return res
def solution_time(lst):
    SETUP_CODE = f'''
from __main__ import Solution, huge_list1, x'''
 
    TEST_CODE = '''


x.solve(huge_list1)

'''
     
    # timeit.repeat statement
    times = timeit.repeat(setup = SETUP_CODE,
                          stmt = TEST_CODE,
                          repeat = 3,
                          number = 10)
 
    # printing minimum exec. time
    return(min(times))

huge_list1 = []
x = Solution()
def test():
    


    for i in range (25):
        for j in range(10):
            a = [i, j]
            b = [-i, j]
            c = [i, -j]
            d = [-i, -j]
            huge_list1.append(a)
            huge_list1.append(b)
            huge_list1.append(c)
            huge_list1.append(d)
        print(len(huge_list1))
        sol_time = solution_time(huge_list1)
        print("time:",sol_time)
        print("increase:", sqrt(sol_time)/(2*len(huge_list1))) #if time is n**2 this number must remain somewhat constant


    print(x.solve(huge_list1))
    print(x.solve([[100,0],[0,0],[13,0]]))
    print(x.solve([[100,0],[50,0],[0,0]]))
    print(x.solve([[0,0],[1,0],[2,0]]))
    print(x.solve([[0,0],[1,1],[2,2]]))
if __name__ == "__main__":
    test()