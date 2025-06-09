## Example 1:
## 
## Input: ratings = [1,0,2]
## Output: 5
## Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
## Example 2:
## 
## Input: ratings = [1,2,2]
## Output: 4
## Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
## The third child gets 1 candy because it satisfies the above two conditions.


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n

        # Left to right
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        # print(candies)

        # Right to left
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        print(candies)

        return sum(candies)
        