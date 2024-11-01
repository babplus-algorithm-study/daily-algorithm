```java
import java.util.*;

class Solution {
    public String solution(String number, int k) {
        String answer = "";
        Stack<Character> stack = new Stack<>();
        stack.push('9');
        stack.push(number.charAt(0));
        
        for(int i = 1; i < number.length() ;i++) {
            char c = number.charAt(i);
            
            while((stack.peek() < c) && (k != 0)) {
                stack.pop();
                k--;
            }
            stack.push(c);
        }
        
        while(stack.size() != 1) {
            answer = stack.pop() + answer;
        }
        
        answer = answer.substring(0, answer.length() - k);
        
        return answer;
    }
    
}
```
