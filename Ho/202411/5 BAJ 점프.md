```java
package gold;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;
import java.util.StringTokenizer;

public class P2253 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        HashSet<Integer> brokenStone = new HashSet<>();
        int[][] dp = new int[N + 1][(int)Math.sqrt(2*N) + 2];

        for(int i = 0; i <= N;i++) {
            Arrays.fill(dp[i], (int)1e9);
        }

        for(int i = 0; i < M; i++) {
            brokenStone.add(Integer.parseInt(br.readLine()));
        }

        dp[1][0] = 0;

        for(int i =2; i <= N; i++) {
            if(brokenStone.contains(i)) continue;

            for(int j = 1; j < (int)Math.sqrt(2*i) + 1; j++) {
                dp[i][j] = Math.min((Math.min(dp[i-j][j+1],dp[i-j][j])),dp[i-j][j-1]) + 1;
            }
        }
```