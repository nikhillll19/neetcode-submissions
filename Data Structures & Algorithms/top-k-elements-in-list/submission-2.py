class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = {}

        for num in nums : 
            if num not in bucket:
                bucket[num] = 1
            else :
                bucket[num] += 1

        sorted_list = sorted(bucket, key=bucket.get)
        n = len(sorted_list)
        res = []

        for i in range(n-1,n-k-1,-1) :
            res.append(sorted_list[i])
        return res

