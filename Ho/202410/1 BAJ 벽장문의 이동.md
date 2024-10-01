```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P2666 {
    static int N;
    static int K;
    static int[] cmd;
    static int[][][] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());

        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());

        K = Integer.parseInt(br.readLine().trim());

        cmd = new int[K];
        dp = new int[K][N + 1][N + 1];

        for (int i = 0; i < K; i++) {
            for (int j = 0; j < N; j++) {
                for (int k = 0; k < N; k++) {
                    dp[i][j][k] = -1;
                }
            }
        }

        for (int i = 0; i < K; i++) {
            cmd[i] = Integer.parseInt(br.readLine().trim());
        }

        System.out.println(calcMinCost(0, a, b));
    }

    public static int calcMinCost(int depth, int doorA, int doorB) {
        if(depth == K) {
            return 0;
        }
        int destination = cmd[depth];

        if (dp[depth][doorA][doorB] != -1) {
            return dp[depth][doorA][doorB];
        }

        int doorACost = Math.abs(destination - doorA) + calcMinCost(depth + 1, destination, doorB);
        int doorBCost = Math.abs(destination - doorB) + calcMinCost(depth + 1, doorA, destination);

        dp[depth][doorA][doorB] = Math.min(doorACost, doorBCost);

        return dp[depth][doorA][doorB];
    }
}

```