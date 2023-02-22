def getSkyline(buildings):
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


buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
getSkyline(buildings)