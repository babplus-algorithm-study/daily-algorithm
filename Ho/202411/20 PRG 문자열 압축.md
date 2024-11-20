```java
class Solution {
    public int solution(String s) {
        int answer = 1000;
    
        StringBuilder sb = new StringBuilder();
        boolean[] visited = new boolean[s.length()];
        
        
        for(int i = 1; i <= s.length()/2; i++) {
            //무조건 앞에서부터 1개단위로 짤라야함.
            String curWord = s.substring(0,i);
            int cnt = 1;
            
            for(int j = i; j < s.length(); j+=i) {
                if(canCompress(curWord, j, s)) {
                    //압축 가능한 경우                
                    cnt++;
                }
                else{
                    if(cnt != 1) {
                        sb.append(cnt);
                    }
                    //cnt만큼 압축
                    sb.append(curWord);
                    if(j+i < s.length()) {
                        curWord = s.substring(j,j+i);    
                    }
                    else{
                        curWord = s.substring(j,s.length());
                    }
                    
                    cnt = 1;
                }
            }
            if(cnt != 1) {
                sb.append(cnt);
            }
            //cnt만큼 압축
            sb.append(curWord);
            answer = Math.min(answer, sb.length());
            
            sb = new StringBuilder();
            
        }    
        if(s.length() == 1) {
            answer = 1;
        }
        return answer;
    }
    
    public boolean canCompress(String word, int startIdx , String originalWord) {
        // 해당 단어의 끝지점부터 word 개수만큼 체크
        for(int i = 0; i < word.length(); i++) {
            if(i + startIdx >= originalWord.length()) return false;
            if(word.charAt(i) != originalWord.charAt(i + startIdx)) return false;
        }
        return true;
    }
}
```