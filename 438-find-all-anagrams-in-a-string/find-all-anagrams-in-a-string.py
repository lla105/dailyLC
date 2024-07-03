class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count = defaultdict(int) 
        for c in p:
            p_count[c] += 1

        res = []
        m = len(p)
        missing = set(p)
        window = defaultdict(int)

        def update_missing(c):
            if c in missing and window[c] == p_count[c]:
                missing.remove(c)
            elif p_count[c] and window[c] != p_count[c]:
                missing.add(c)

        for i, c in enumerate(s):
            window[c] += 1
            update_missing(c)
            if i >= m - 1:
                out_idx = i - m + 1
                if not missing:
                    res.append(out_idx)
                window[s[out_idx]] -= 1
                update_missing(s[out_idx])

        return res