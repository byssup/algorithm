class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        return [
            True
            if candi + extraCandies >= max(candies) else False for candi in candies 
        ]

