```java
package gold;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P17404 {
    static int N;
    static int[][] costs;
    static int[][] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());

        costs = new int[N][3];

        int ans = (int) 1e9;

        for(int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < 3; j++) {
                costs[i][j] = Integer.parseInt(st.nextToken());
            }
        }


        for(int i =0; i < 3; i++) {
            dp = new int[N][3];
            dp[0][0] = costs[0][i];
            dp[0][1] = costs[0][i];
            dp[0][2] = costs[0][i];
            //처음 스타트 포인트 고정
            int temp = costs[1][i];
            costs[1][i] = (int) 1e9 ;

            for(int j = 1; j < N; j++) {
                dp[j][0] = Math.min(dp[j - 1][1], dp[j - 1][2]) + costs[j][0];
                dp[j][1] = Math.min(dp[j - 1][0], dp[j - 1][2]) + costs[j][1];
                dp[j][2] = Math.min(dp[j - 1][0], dp[j - 1][1]) + costs[j][2];
            }

            for(int j = 0; j < 3; j++) {
                if(j == i) continue;
                ans = Math.min(ans, dp[N-1][j]);
            }
            costs[1][i] = temp;
        }

        System.out.println(ans);


    }
}

```