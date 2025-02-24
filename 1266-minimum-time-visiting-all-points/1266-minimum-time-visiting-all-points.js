var minTimeToVisitAllPoints = function(points) {
    let result = 0;
    let [x1, y1] = points.shift();
    while (points.length>0) {
        let [x2, y2] = points.shift();
        result += Math.max(Math.abs(x2-x1), Math.abs(y2-y1));
        [x1, y1] = [x2, y2];
    }
    return result;
};