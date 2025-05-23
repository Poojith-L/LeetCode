int removeDuplicates(int* nums, int numsSize) {
    int i,j=0;
    for(i=0; i<numsSize-1; i++){
        if(nums[i]!=nums[i+1]){
            nums[j]=nums[i];
            j++;
        }
    }
    nums[j]=nums[i];
    numsSize=j+1;
    return numsSize;
}