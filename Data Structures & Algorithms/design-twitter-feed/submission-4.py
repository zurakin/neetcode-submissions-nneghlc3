class Twitter:

    def __init__(self):
        self.feeds = {}
        self.follows = {}
        self.posts = {}
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        post = (self.time, tweetId)
        if userId in self.posts:
            self.posts[userId].append(post)
        else: 
            self.posts[userId] = [post]
        if len(self.posts[userId]) > 10:
            self.posts[userId].pop(0)

    def getNewsFeed(self, userId: int) -> List[int]:
        followees = set()
        if userId in self.follows:
            followees = set(self.follows[userId])
        followees.add(userId)
        feed = []
        for followee in followees:
            if followee not in self.posts:
                continue
            for post in self.posts[followee]:
                heapq.heappush(feed, post)
                if len(feed) > 10:
                    heapq.heappop(feed)
        return [post[1] for post in sorted(feed, reverse=True)]


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows:
            self.follows[followerId].add(followeeId)
        else:
            self.follows[followerId] = set()
            self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)

        
