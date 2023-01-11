var intersection = function(nums1, nums2) {
    let list1 = new Set(nums1)
    let list2 = new Set(nums2)
    let list3 = []
    for (let n of list1){
        if (list2.has(n)){
            list3.push(n)
        }
    }
    return list3
};
let nums1 = [1,2,3,3]
let nums2 = [2,3,4]
console.log(intersection(nums1, nums2))