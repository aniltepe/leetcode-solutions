class Solution(object):
    def getSkyline(self, buildings):
        keypoints = []
        minline = min([b[0] for b in buildings])
        maxline = max([b[1] for b in buildings])
        prevheight = 0
        i = minline
        while i < maxline:
            j = i + 1
            maxheight = 0
            segmentheights = [b[2] for b in buildings if i >= b[0] and j <= b[1]]
            if len(segmentheights) > 0:
                maxheight = max(segmentheights)
            if maxheight != prevheight:
                keypoints.append([i, maxheight])
            prevheight = maxheight
            i = i + 1
        keypoints.append([maxline, 0])
        return keypoints
                    
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        