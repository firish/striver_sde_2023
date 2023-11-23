# Link: https://leetcode.com/problems/design-twitter/submissions/
# LC Medium


import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        # connections will act as a unidirected follower graph
        # use a defaultdict of sets
        # this gives O(1) lookup, and
        # O(1) addition and popping
        self.connections = defaultdict(set)
        
        # user_tweets will hold all tweets by a user_id
        # use a defaultdict of lists, 
        # this allows O(1) lookup
        self.user_tweets = defaultdict(list)
        
        # time will keep track of the relative time of posts
        # the time can be used as a key in sorting, or heapifying
        # the time is negative, as python has only min_heap
        # and negation lets us convert it to a max_heap
        self.time = -1

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweets[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        network = [userId] 
        network += [user_id for user_id in self.connections[userId]]
        feed = []
        for followed_user in network:
            feed += self.user_tweets[followed_user]
        k = min(10, len(feed))
        heapq.heapify(feed)
        news_feed = []
        for _ in range(k):
            time, tweet_id = heapq.heappop(feed)
            news_feed.append(tweet_id)
        return news_feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.connections[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.connections[followerId]:
            self.connections[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
