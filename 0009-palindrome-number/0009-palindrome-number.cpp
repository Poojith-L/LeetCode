class Solution {
public:
    bool isPalindrome(int x) {
        int ori,rem;
        long rev=0;
        if(x<0)
            return false;
        ori=x;
        while(x!=0){
            rem=x%10;
            rev=rev*10+rem;
            x=x/10;
        }
        if(ori==rev)
            return true;
        else
            return false;
    }
};