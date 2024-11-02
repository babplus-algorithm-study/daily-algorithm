``` java
import java.util.*;

class Solution {
    
    ArrayList<String> lists = new ArrayList<>();
    String[][] tickets;
    boolean[] visited;
    
    public String[] solution(String[][] ticketss) {
        String[] answer;
        tickets = new String[ticketss.length][ticketss[0].length];
        visited = new boolean[tickets.length];
        
        for(int i = 0; i < ticketss.length; i++) {
            tickets[i] = ticketss[i].clone();
        }
        
        dfs(0, "ICN", "ICN");
        Collections.sort(lists);
        answer = lists.get(0).split(" ");
        
        return answer;
    }
    
    public boolean dfs(int count, String current, String all) {
        if(count == tickets.length) {
            lists.add(all);
            return true;
        }
        
        for(int i = 0; i < tickets.length; i++) {
            if(visited[i]) continue;
            
            if(current.equals(tickets[i][0])) {
                visited[i] = true;
                dfs(count+1, tickets[i][1], all + " " + tickets[i][1]);
                visited[i] = false;
        }
        }
        
        return false;
    }
}
```
