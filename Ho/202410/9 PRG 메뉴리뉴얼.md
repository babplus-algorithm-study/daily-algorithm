```java
import java.util.*;

class Solution {
    int[] alpaCnt = new int[26];
    HashMap<String, Integer> map = new HashMap<>();
    ArrayList<Character> list = new ArrayList<>();
    ArrayList<String> ans = new ArrayList<>();
    int size = 0;
    
    
    public String[] solution(String[] orders, int[] course) {
        String[] answer = {};
        
        
        for(int i = 0; i < course.length; i++) {
            size = course[i];
            map = new HashMap<>();
            int curMax = 2;
            ArrayList<String> temp = new ArrayList<>();
            //curlen짜리 단어 찾기
            for(int j = 0; j < orders.length; j++) {
                String curString = orders[j];
                char[] chars = curString.toCharArray();
                Arrays.sort(chars);
                curString = new String(chars);
                back(curString, 0, 0);   
                
            }
            
            //max만 넣기
            for(String key : map.keySet()) {
                if(map.get(key) > curMax) {
                    curMax = map.get(key);
                    temp = new ArrayList<>();
                    temp.add(key);
                }
                else if(curMax == map.get(key)) {
                    if(!list.contains(key)) {
                        temp.add(key);    
                    }
                }
            }
            
            for(String key : temp) {
                ans.add(key);
            }
        }
        Collections.sort(ans);
        answer = new String[ans.size()];
        
        int idx = 0;
        for(String w : ans) {
            answer[idx++] = w;
        }
        
        return answer;
    }
    
    public void back(String word,int idx,int depth) {
        if(depth == size) {
            String curWord = makeWord();
            int curCnt = map.getOrDefault(curWord,0);
            map.put(curWord, curCnt + 1);
            return;
        }
        
        for(int i = idx; i < word.length(); i++) {
            list.add(word.charAt(i));
            back(word,i+1,depth+1);
            list.remove(list.size()-1);
        }
    }
    
    public String makeWord() {
        StringBuilder sb = new StringBuilder();
        
        for(char c : list) {
            sb.append(c);
        }
        return sb.toString();
    }
}
```