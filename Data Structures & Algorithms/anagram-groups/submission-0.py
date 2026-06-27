class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}

        for word in strs:
            sorted_key = tuple(sorted(word))
            if sorted_key in anagram_dict:
                anagram_dict.get(sorted_key).append(word)
            
            else:
                anagram_dict[sorted_key] = [word]

        final_list = []
        for v in anagram_dict.values():
            final_list.append(v)

        return final_list