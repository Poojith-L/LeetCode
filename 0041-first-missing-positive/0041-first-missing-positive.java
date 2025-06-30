class Solution {
    public int firstMissingPositive(int[] nums) {
        int i=1;
        Arrays.sort(nums);
        for(int n:nums)
        {
            if(n>0)
            {
                if(n==i)
                    i++;
                else if(n>i)
                    break;
            }
        }
        return i;
    }
}