class Solution(object):
    def groupAnagrams(self, strs):
        d = {}
        for curstring in strs:
            sorted_string = ''.join(sorted(curstring))
            if sorted_string in d:
                d[sorted_string].append( curstring )
            else:
                d[sorted_string] = [curstring]
        output = []
        for i,v in d.items():
            output.append(v)
        return output
        