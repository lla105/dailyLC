class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d = Counter(arr)
        print(d)
        stack = []
        for i,v in d.items():
            if v==1:
                stack.append(i)
        print(stack)

        if k-1>=len(stack):
            return ''
        else:
            return stack[k-1]