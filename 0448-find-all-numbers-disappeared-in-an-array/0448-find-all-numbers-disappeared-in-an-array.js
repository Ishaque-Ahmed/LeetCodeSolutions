var findDisappearedNumbers = function (nums) {
    const uniqueNums = new Set();
    const missingNums = [];
    for (let num of nums) {
        uniqueNums.add(num);
    }
    
    for (let i = 1; i <= nums.length; i++) {
        if (!uniqueNums.has(i)) {
            missingNums.push(i);
        }
    }
    return missingNums;
};