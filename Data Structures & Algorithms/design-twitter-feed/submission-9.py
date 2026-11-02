from collections import defaultdict
from typing import List

class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time,tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        maxheap = []
        users = self.following[userId]|{userId}

        for userid in users:
            if self.tweets[userid]:
                index = len(self.tweets[userid])-1
                time,tweetId = self.tweets[userid][index]

                heapq.heappush(maxheap, (-time,tweetId,userid,index))

        res = []
        while maxheap and len(res)<10:
            negtime, tweetID, userId, index = heapq.heappop(maxheap)

            res.append(tweetID)

            if index > 0:
                index -= 1
                time, pretweetid = self.tweets[userId][index]
                heapq.heappush (maxheap, (-time,pretweetid,userId,index))
            
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)