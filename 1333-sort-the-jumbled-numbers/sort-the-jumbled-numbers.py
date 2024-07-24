class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        converted = set()
        d = defaultdict(list)
        for i in range(len(nums)):
            curnum = []
            stringnum = str(nums[i])
            # print(curnum, ' --- ', stringnum[0])
            for j in range(len(stringnum)) :
                curnum.append( str(mapping[ int(stringnum[j]) ] ))
                # curnum.append(mapping[int(stringnum)[j]])
                # print(stringnum[j] , mapping[ int(stringnum[j]) ] 
            temp = int(''.join(curnum))
            converted.add(temp)
            # d[temp] = int(stringnum)
            d[temp].append( int(stringnum) )
            # print(stringnum, temp)
            # arr.append( int(''.join(curnum)))
        # print(converted)
        # print(d)
        converted = sorted(converted)
        result = []
        for key in converted:
            # print('key : ', key)
            for index in range(len(d[key])):
                # print(' >> ', d[key][index])
                result.append( d[key][index] )
        return result