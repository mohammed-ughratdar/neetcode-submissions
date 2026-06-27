class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        my_dict = {}
        final_list = []

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in my_dict:
                my_dict.get(sorted_word).append(word)
            else:
                my_dict[sorted_word] = [word]

        for k in my_dict:
            final_list.append(my_dict.get(k))

        return final_list
