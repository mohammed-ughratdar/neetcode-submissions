class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = [0] * 26
        s2_count = [0] * 26
        matches = 0
        l = r = 0

        if len(s1) > len(s2):
            return False
            
        while r <len(s1):
            idx_s2 = ord(s2[r]) - ord('a')
            idx_s1 = ord(s1[r]) - ord('a')
            s1_count[idx_s1] +=1
            s2_count[idx_s2] +=1
            r+=1

        for x in range(0, 26):
            if s1_count[x] == s2_count[x]:
                matches+=1

        if matches == 26:
            return True
        
        while r < len(s2):
            idx_remove = ord(s2[l]) - ord('a')
            idx_add = ord(s2[r]) - ord('a')
            is_to_remove_index_matched_before = s1_count[idx_remove] == s2_count[idx_remove]
            s2_count[idx_remove] -= 1
            is_to_remove_index_matched_after = s1_count[idx_remove] == s2_count[idx_remove]
            if is_to_remove_index_matched_before and not is_to_remove_index_matched_after:
                matches -=1
            if not is_to_remove_index_matched_before and is_to_remove_index_matched_after:
                matches +=1
                

            is_to_add_index_matched_before = s1_count[idx_add] == s2_count[idx_add]
            s2_count[idx_add] += 1
            is_to_add_index_matched_after = s1_count[idx_add] == s2_count[idx_add]
            if is_to_add_index_matched_before and not is_to_add_index_matched_after:
                matches -=1
            if not is_to_add_index_matched_before and is_to_add_index_matched_after:
                matches +=1

            
            if matches == 26:
                return True
            
            l+=1
            r+=1

        return False


