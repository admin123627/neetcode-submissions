class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_list = []
        anagrams_map = {}  #The key is a map and the value is list
        for i in strs:
            string_map = {}  #The key is a letter and the value is number of tiems letter occurs in string
            for j in range(len(i)):
                if i[j] not in string_map:
                    string_map[i[j]] = 1
                else:
                    string_map[i[j]] += 1
            strings_tuple = tuple(sorted(string_map.items()))
            if strings_tuple in anagrams_map:
                anagrams_map[strings_tuple].append(i)
            else:
                anagrams_map[strings_tuple] = [i]
                anagrams_list.append(anagrams_map[strings_tuple])
        return anagrams_list      