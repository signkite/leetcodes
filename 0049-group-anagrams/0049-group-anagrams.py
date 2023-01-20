class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sort_dict = {}
        for s in strs:
            s_sorted = ''.join(sorted(s))
            if s_sorted in sort_dict.keys():
                sort_dict[s_sorted].append(s)
            else:
                sort_dict[s_sorted] = [s]
        
        return list(sort_dict.values())
            