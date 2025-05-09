class Solution:
    @staticmethod
    def union_arr(arr1, arr2):
        seen = set()
        result = []
        for num in arr1 + arr2:
            if num not in seen:
                seen.add(num)
                result.append(num)
        return result

    @staticmethod
    def intersection_arr(arr1, arr2):
        set2 = set(arr2)
        return [num for num in arr1 if num in set2]

# Test
arr1 = [1, 2, 5, 6]
arr2 = [1, 2, 3, 4]

print("Union:", Solution.union_arr(arr1, arr2))
print("Intersection:", Solution.intersection_arr(arr1, arr2))
