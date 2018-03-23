class Solution(object):
    def remove_duplicates(self, s):
        seen = set()
        s_wo_dup = ""
        for c in s:
            if c not in seen:
                s_wo_dup += c
                seen.add(c)
        return s_wo_dup
