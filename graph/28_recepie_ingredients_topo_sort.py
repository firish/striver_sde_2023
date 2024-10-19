# LC Medium
# URL: https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/submissions/

# My solutions
# Uses Topo sort (indegrees using Kahns algorithm)
from collections import deque, defaultdict
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        # build the adj list (graph)
        g = defaultdict(list)
        indegrees = defaultdict(int)
        for ind, ingredient_list in enumerate(ingredients):
            for ingredient in ingredient_list:
                g[ingredient].append(recipes[ind])
                indegrees[recipes[ind]] += 1
        # print(g, indegrees)
        
        # we have unlimited supply
        q = deque()
        seen = set()
        for ingredient in supplies:
            q.append(ingredient)
            seen.add(ingredient)
        
        # take elements out from supply one by one (avoid duplicates)
        while len(q) > 0:
            ingredient = q.pop()
            for recipe in g[ingredient]:
                indegrees[recipe] -= 1
                if indegrees[recipe] == 0 and recipe not in seen:
                    q.append(recipe)
                    seen.add(recipe)
        # print(indegrees)
        
        res = [recipe for recipe in recipes if indegrees[recipe] == 0]
        return res
                    
