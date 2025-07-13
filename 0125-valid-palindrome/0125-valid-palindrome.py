class Solution:
    def isPalindrome(self, s: str) -> bool:
        st=''.join(ch for ch in s if ch.isalnum())
        st=st.lower()
        i=0
        j=len(st)-1
        while i<j:
            if st[i]==st[j]:
                i+=1
                j-=1
            else:
                return False
        return True