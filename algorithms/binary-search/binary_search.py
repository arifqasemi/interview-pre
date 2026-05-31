## | Hint                     | Meaning                 |
## | ------------------------ | ----------------------- |
## | sorted array             | biggest signal          |
## | find target              | common                  |
## | minimum/maximum possible | binary search on answer |
## | monotonic behavior       | very strong hint        |
## | search space             | strong hint             |
## | can eliminate half       | strongest clue          |
#. 
#. sorted array
#. sorted list
#. sorted numbers
#  search value
#. locate element

##. Binary Search Framework
##. 
##. When reading a problem:
##. 
##. Ask:
##. Is something sorted?
##. Can I eliminate half safely?
##. Is there a monotonic condition?
##. Am I searching for:
##. minimum?
##. maximum?
##. first occurrence?
##. last occurrence?
##. 
##. If yes, Binary Search becomes a strong candidate.


##  Interview Problems To Learn
##  
##  I would prioritize these:
##  
##  Binary Search
##  Search Insert Position
##  Find First and Last Position of Element
##  Search in Rotated Sorted Array
##  Koko Eating Bananas (Binary Search on Answer)
##  Capacity To Ship Packages Within D Days (Binary Search on Answer)

####### Binary Search on Answer #########
####. minimum possible
####. maximum possible
####. smallest value
####. largest value
####. least capacity
####. minimum speed
####. maximum distance
####  Peak element


###. Generic Template
###. 
###. Most Binary Search on Answer problems look like:
###. 
###. left = minimum_possible_answer
###. right = maximum_possible_answer
###. 
###. while left <= right:
###. 
###.     mid = (left + right) // 2
###. 
###.     if valid(mid):
###.         answer = mid
###.         right = mid - 1
###.     else:
###.         left = mid + 1
###. 
###. return answer
