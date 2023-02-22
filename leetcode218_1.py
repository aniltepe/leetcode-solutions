def getSkyline(buildings):
    keypoints = []
    minseg = min([b[0] for b in buildings])
    maxseg = max([b[1] for b in buildings])
    for i in range(len(buildings)):
        for j in range(len(buildings)):
            if i == j:
                continue
            if buildings[i][0] <= buildings[j][0]:
                
    keypoints.append([maxseg, 0])



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