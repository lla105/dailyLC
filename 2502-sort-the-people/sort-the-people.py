class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d = defaultdict(list)
        maxheight = max(heights)
        for i in range(len(names)):
            if heights[i] in d:
                d[heights[i]].append(names[i])
            else:
                d[heights[i]] = [names[i]]
        print(d)
        result = []
        for h in range(maxheight, -1 ,-1):
            for person in d[h]:
                result.append(person)

        return result