# Note obtained knowledges
# Looping using a set is much faster than a normal array
# n+length is better than create an increment variable
# For bruteforce O(nlogn) approach, just ignore duplicate completely (do it normally)
# Searching or checking sth is in a collection, always use a set

class Solution:
    def longestConsecutive_bruteforcev2(self, nums) -> int:
        if not nums:
            return 0
        sorted_nums = sorted(list(set(nums))) # Remove duplicates then sort them
        longest = 0
        length = 1
        curr = sorted_nums[0]
        for i in range(1, len(sorted_nums)): 
            if sorted_nums[i] != (curr+length):
                longest = max(length, longest)
                curr = sorted_nums[i]
                length = 1
            else:
                length += 1
        longest = max(length, longest)
        return longest

    def longestConsecutive_bruteforce(self, nums) -> int:
        if not nums:
            return 0
        sorted_nums = sorted(nums)
        longest = 0
        length = 1
        curr = sorted_nums[0]
        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] == curr:
                continue
            if sorted_nums[i] != curr+1:
                longest = max(length, longest)
                curr = sorted_nums[i]
                length = 1
            else:
                curr += 1
                length += 1
        longest = max(length, longest)
        return longest

    def longestConsecutive(self, nums) -> int:
        setnums = set(nums)
        longest = 0
        for n in setnums:
            if n-1 not in setnums:
                length = 1
                while (n+length) in setnums:
                    length += 1
                if length > longest:
                    longest = length
        return longest
    
    def longestConsecutive_builtin(self, nums) -> int:
        setnums = set(nums)
        longest = 0
        for n in setnums:
            if n-1 not in setnums:
                length = 1
                while (n+length) in setnums:
                    length += 1
                longest = max(length, longest)
        return longest

# Testing
#nums = [100,4,200,1,3,2]

#nums = [100,14,200,11,13,12]

#nums = [0,3,7,2,5,8,4,6,0,1,1]

nums = [9,1,4,7,3,-1,0,5,8,-1,6]

print(Solution().longestConsecutive(nums))

print(Solution().longestConsecutive_bruteforce(nums))
    
