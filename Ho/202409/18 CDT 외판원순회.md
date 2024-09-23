```
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static int N;
    public static int[][] grid;
    public static boolean[] visited;
    public static int minCost = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        grid = new int[N][N];

        visited = new boolean[N];

        for(int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int j = 0; j < N; j++) {
                grid[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        simulate();
    }

    //모든 경우의 수 순회하기
    public static void simulate() {
        for (int i = 1; i < N; i++) {
            int currentCost = 0;
            if(canGo(0,i)) {
                visited[i] = true;
                currentCost += grid[0][i];
                dfs(i, currentCost, 1);
                visited[i] = false;
            }
        }
        
        System.out.println(minCost);
    }

    public static void dfs(int row, int currentCost, int depth) {

        if (depth == N - 1) {
            currentCost += grid[row][0];
            minCost = Math.min(currentCost, minCost);
            return;
        }

        for(int i = 1; i < N; i++) {
            if(canGo(row,i)) {
                visited[i] = true;
                currentCost += grid[row][i];
                dfs(i, currentCost, depth+1);
                currentCost -= grid[row][i];
                visited[i] = false;
            }
        }
    }

    public static boolean canGo(int row, int col) {
        if(row == col) return false;
        if(grid[row][col] == 0) return false;
        if(visited[col]) return false;
        return true;
    }
}

```