```java
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

public class Main {


    public static void main(String[] args) throws Exception {
        int T = read();

        StringBuilder sb = new StringBuilder();

        while(T --> 0) {
            int N = read();
            int E = read();
            boolean[] arr = new boolean[N + 1];
            boolean[] visited = new boolean[N + 1];

            ArrayList<Integer>[] graphs = new ArrayList[N + 1];
            for(int i = 1 ; i <= N; i++) {
                graphs[i] = new ArrayList<>();
            }

            while(E --> 0) {
                int a = read();
                int b = read();
                graphs[a].add(b);
                graphs[b].add(a);
            }

            boolean b = true;
            for(int i = 1; i <= N; i++) {
                if(visited[i]) continue;
                visited[i] = true;

                Queue<Integer> q = new LinkedList<>();
                q.add(i);
                
                while(!q.isEmpty()) {
                    int a = q.poll();
                    for(int v : graphs[a]) {
                        if(!visited[v]) {
                            visited[v] = true;
                            arr[v] = !arr[a];
                            q.add(v);
                        } else {
                            if(arr[a] == arr[v]) {
                                sb.append("NO").append("\n");
                                b = false;
                                break;
                            }
                        }
                    }
                    if(!b) break;
                }
                if(!b) break;
            }
            if(b) sb.append("YES").append("\n");
        }

        System.out.println(sb);
    }


    private static int read() throws Exception {
        int d, o;
        boolean negative = false;
        d = System.in.read();

        if (d == 45) {
            negative = true;
            d = System.in.read();
        }

        o = d & 15;
        while ((d = System.in.read()) > 32)
            o = (o << 3) + (o << 1) + (d & 15);

        return negative ? -o : o;
    }
}
```
