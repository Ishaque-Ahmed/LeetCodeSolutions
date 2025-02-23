var smallerNumbersThanCurrent = function (nums) {
    let sortedArray = [...nums].sort((a, b) => a - b);
    const storage = new Map();
    const retArr = [];
    
    for (const [index, element] of sortedArray.entries()) {
        if(!storage.has(element)) {
            storage[element] = index;
        }
        storage.set(element, index);
    }
    
    for(let num of nums){
        retArr.push(storage[num]);
    }

    return retArr;
};