class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        s1 = set() #all cities
        s2 = set() #source cities
        for i in range(len(paths)):
            from_city = paths[i][0]
            to_city = paths[i][1]
            s1.add( from_city )
            s1.add( to_city )
            s2.add( from_city )
        for item in s1:
            # print('>> ', item)
            if item not in s2:
                return item
        return ""