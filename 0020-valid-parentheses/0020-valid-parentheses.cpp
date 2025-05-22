class Solution {
public:
    bool isValid(string s) {
        int top=0;
        char stack[s.length()+1];
        stack[top]='#';
        for(int i=0; i<s.length(); i++){
            if(s[i]=='{' || s[i]=='[' || s[i]=='('){
                stack[++top]=s[i];
            }
            else{
                if(s[i]=='}'){
                    if(stack[top]=='{')
                        stack[top--];
                    else
                        stack[++top]=s[i];
                }
                else{ 
                    if(s[i]==']'){
                        if(stack[top]=='[')
                            stack[top--];
                        else
                            stack[++top]=s[i];
                    }
                    else{
                        if(stack[top]=='(')
                            stack[top--];
                        else
                            stack[++top]=s[i];
                    } 
                }              
            }    
        }
        if(stack[top]=='#')
            return true;
        else
            return false;
    }
};