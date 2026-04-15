from collections import deque

class Twitter:

    def __init__(self):
        self.tweets = []
        self.follows = {}
        self.userId = None

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        for tUserId, tweetId in reversed(self.tweets):
            if userId == tUserId or tUserId in self.follows.get(userId, []):
                feed.append(tweetId)
            if len(feed) == 10:
                break
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = {followeeId}
        else:
            self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        try:
            self.follows[followerId].remove(followeeId)
        except KeyError as e:
            pass
        
