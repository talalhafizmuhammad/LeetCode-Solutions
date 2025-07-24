class Solution(object):
    def intersection(self, nums1, nums2):
        list1 = (set(nums1))
        list2 = (set(nums2))
        myList = list1.intersection(list2)
        return list(myList)

        
