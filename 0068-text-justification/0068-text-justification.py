class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result=[]
        curr=[]
        for word in words:
            if len(' '.join(curr+[word]))<=maxWidth:
                curr.append(word)
            elif len(' '.join(curr))<=maxWidth:
                sp=maxWidth-len(' '.join(curr))
                n=len(curr)
                s=n-1
                if s!=0:
                    q=sp//s
                    r=sp%s
                    for i in range(r):
                        curr[i]=curr[i]+' '
                    result.append((' '*(q+1)).join(curr))
                else:
                    result.append(' '.join(curr)+' '*sp)
                curr=[word]
        s=maxWidth-len(' '.join(curr))
        result.append(' '.join(curr)+' '*s)
        return result