class Solution(object):
    def findRestaurant(self, list1, list2):
        index_map = {word: i for i, word in enumerate(list1)}
        min_sum = float('inf')
        result = []

        for j, word in enumerate(list2):
            if word in index_map:
                i = index_map[word]
                total = i + j
                if total < min_sum:
                    result = [word]
                    min_sum = total
                elif total == min_sum:
                    result.append(word)

        return result
