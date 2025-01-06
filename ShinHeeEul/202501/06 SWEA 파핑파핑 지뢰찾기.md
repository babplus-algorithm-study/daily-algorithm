```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Solution {

    static int[][] arr;
    static boolean[][] visited;
    static int N;
    static int[] dj = {0,1,1,1,0,-1,-1,-1};
    static int[] di = {-1,-1,0,1,1,1,0,-1};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();

        for(int t = 1; t <= T; t++) {

            N = Integer.parseInt(br.readLine());
            arr = new int[N][N];
            visited = new boolean[N][N];

            for(int i = 0; i < N; i++) {
                String s = br.readLine();
                for(int j = 0; j < N; j++) {
                    char c = s.charAt(j);
                    if(c == '*') {
                        arr[i][j] = -10;
                        for(int k = 0; k < 8; k++) {
                            if(check(i + di[k], j + dj[k])) arr[i + di[k]][j + dj[k]]++;
                        }
                    }
                }
            }

            int count = 0;
            for(int i = 0; i < N; i++) {
                for(int j = 0; j < N; j++) {
                    if(!visited[i][j] && arr[i][j] == 0) {
                        count++;
                        visited[i][j] = true;
                        bfs(i,j);
                    }
                }
            }

            for(int i = 0; i < N; i++) {
                for(int j = 0; j < N; j++) {
                    if(!visited[i][j] && arr[i][j] > 0) count++;
                }
            }

            sb.append("#").append(t).append(" ").append(count).append("\n");
        }
        System.out.println(sb);
    }

    private static boolean check(int i, int j) {
        return i >=0 && j >=0 && i < N && j < N;
    }

    private static void bfs(int i, int j) {
        Queue<Node> queue = new LinkedList<>();

        queue.add(new Node(i, j));

        while(!queue.isEmpty()) {
            Node n = queue.poll();
            int ni = n.i;
            int nj = n.j;

            for(int k = 0; k < 8; k++) {
                int nii = ni + di[k];
                int njj = nj + dj[k];

                if(!check(nii, njj)) continue;
                if(visited[nii][njj]) continue;

                visited[nii][njj] = true;

                if(arr[nii][njj] == 0) queue.add(new Node(nii,njj));
            }
        }
    }

    private static class Node {
        int i;
        int j;
        Node(int i, int j) {
            this.i = i;
            this.j = j;
        }
    }

}

```
