# Link: https://leetcode.com/problems/design-a-food-rating-system/


# Solution -> 
from sortedcontainers import SortedList

# SortedList maintains all its elements in sorted order.
# It's useful when you need a list that remains sorted after each insertion or deletion

# How is it different from a Heap/Priority queue?
# Heap gives the smallest/largest element of a collection, but all elements are not sorted
# hence 5th element of a heap is not always the 5th largest or 5th smallest element of the collection
# While SortedList[5] will always give the 5th smallest element

# Why don't we always use a SortedList
# Heap is extremely effective in updates
# insertion/deletion typically take O(logN) in a heap
# insertion/deletion typically take O(N) + O(logN) in a SortedList

# The choice between the two is dependent on how many elements of the collection
# need to be accessible at any given moment. 


class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        # Constructor Initializations
        self.n = len(foods)
        self.dict = defaultdict(SortedList)
        self.food = {}
        
        for i in range(self.n):
            self.dict[cuisines[i]].add((-ratings[i], foods[i]))
            self.food[foods[i]] = [cuisines[i], -ratings[i]]

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.food[food][0]
        
        # remove the previous rating
        self.dict[cuisine].remove((self.food[food][1], food))
        
        # update the rating
        self.food[food][1] = -newRating
        self.dict[cuisine].add((-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        return self.dict[cuisine][0][1]
    
# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
