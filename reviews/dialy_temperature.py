
###Example 1:

###########Input: temperatures = [73,74,75,71,69,72,76,73]
###########Output: [1,1,4,2,1,1,0,0]
###########Example 2:
###########
###########Input: temperatures = [30,40,50,60]
###########Output: [1,1,1,0]
###########Example 3:
###########
###########Input: temperatures = [30,60,90]
###########Output: [1,1,0]


class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        answer = [0] * n
        stack = []  # stores indices

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev_index = stack.pop()
                answer[prev_index] = i - prev_index
            stack.append(i)

        return answer