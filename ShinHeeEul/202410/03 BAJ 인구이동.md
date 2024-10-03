```java
import org.w3c.dom.Node;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

class Main {

    static int[][] maps;
    static int[] di = {-1, 1, 0, 0};
    static int[] dj = {0 ,0, -1 ,1};
    static int count;
    static int val;
    public static void main(String[] args) throws Exception {
        int N = read();
        int L = read();
        int R = read();
        maps = new int[N+2][N+2];

        Arrays.fill(maps[0], -1000);
        for(int i = 1; i < N+1; i++) {
            Arrays.fill(maps[i], -1000);
            for(int j = 1; j < N+1; j++) {
                maps[i][j] = read();
            }
        }
        Arrays.fill(maps[N+1], -1000);

        int date = -1;
        boolean check = true;
        while(check) {
            date++;
            check = false;
            boolean[][] allVisited = new boolean[N+2][N+2];

            for(int i = 1; i <= N; i++) {
                for(int j = 1; j <= N; j++) {
                    if(allVisited[i][j]) continue;
                    boolean[][] visited = new boolean[N + 2][N + 2];
                    int count = 0;
                    int val = 0;

                    Queue<Node> queue = new LinkedList<>();
                    Queue<Node> queue2 = new LinkedList<>();
                    queue.add(new Node(i, j, maps[i][j]));
                    queue2.add(new Node(i, j, maps[i][j]));
                    visited[i][j] = true;
                    while(!queue.isEmpty()) {
                        Node node = queue.poll();
                        int ni = node.i;
                        int nj = node.j;
                        count++;
                        val += node.val;
                        for(int k = 0; k < 4; k++) {
                            int ai = ni + di[k];
                            int aj = nj + dj[k];
                            int diff = Math.abs(node.val - maps[ai][aj]);

                            if(diff >= L && diff <= R) {
                                if(visited[ai][aj] || allVisited[ai][aj]) continue;
                                check = true;
                                visited[ai][aj] = true;
                                queue.add(new Node(ai, aj, maps[ai][aj]));
                                queue2.add(new Node(ai, aj, maps[ai][aj]));
                            }
                        }
                    }
                    if(count == 1) continue;
                    int people = val / count;
                    while(!queue2.isEmpty()) {
                        Node node = queue2.poll();
                        int k = node.i;
                        int m = node.j;
                        allVisited[k][m] = true;
                        maps[k][m] = people;
                    }
                }
            }

        }
        System.out.println(date);
    }

    private void dfs(int i, int j) {

    }

    private static class Node {
        int i;
        int j;
        int val;

        public Node(int i, int j, int val) {
            this.i = i;
            this.j = j;
            this.val = val;
        }
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
