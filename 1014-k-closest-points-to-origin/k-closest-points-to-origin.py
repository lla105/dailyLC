class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    
        def getdistance(corrdinate):
            x = corrdinate[0]
            y = corrdinate[1]
            x = x*x
            y = y*y
            temp = x+y
            return sqrt(temp)
        d = {} #format: { distance: corrdinates}
        # d2 = {} # format: { distance: corrdinates}
        keystack = []
        for i in range(len(points)):
            # print('-->', points[i])
            # print(' = ', getdistance(points[i]))
            temp = getdistance(points[i])
            if temp in d:
                d[temp].append(points[i])
            else:
                d[temp] = [points[i]]
            # d2[temp] = points[i]

            keystack.append(temp)

        print(d)
        print()
        keystack = sorted(keystack)
        print(keystack)
        result = []
        j=0 #index for keystack
        while k>0:
            key = keystack[j]
            # print(">>", key, " - ", d[key])
            # print("<<", len(d[key]))
            keylength = 0
            while len(d[key])>keylength:
                # print("appending : ", d[key][keylength])
                result.append(d[key][keylength])
                # print(" result : ", result)
                j+=1
                k-=1
                keylength += 1
        print(" result : ", result)
        
        return result