class Solution:
    def partition(self, s: str) -> List[List[str]]:
        output = [] 
        def isP( word ) :
            i = 0
            j = len(word) - 1
            while i<j:
                if word[i]!=word[j]:
                    return False
                i+=1
                j-=1
            return True
        def trav( cur_string, cur_list, idx ) :
            if idx == len(s):
                # if cur_string :
                #     output.append( cur_list + [cur_string] )
                if not cur_string:
                    output.append( cur_list)
                return
            # left
            cur_word = cur_string + s[idx]
            if isP(cur_word):
                print(f'{cur_word} is palin.')
                trav( "", cur_list+[cur_word] , idx+1)
            else:
                print(f'{cur_word} is not palin.')
            # right
            trav( cur_word , cur_list , idx+1)
        trav( "", [] , 0)
        return output