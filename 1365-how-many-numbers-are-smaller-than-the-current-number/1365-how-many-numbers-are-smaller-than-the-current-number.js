var smallerNumbersThanCurrent = function (nums) {
    let sortedArray = [...nums].sort((a, b) => a - b);
    const storage = new Map();
    
    for (const [index, element] of sortedArray.entries()) {
        if(!storage.has(element)) {
            storage[element] = index;
        }
        storage.set(element, index);
    }
    
    for (const [index, element] of nums.entries()) {
        nums[index] = storage[element];
    }

    return nums;
};