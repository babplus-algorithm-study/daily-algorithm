```java

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class P2631 {

    static int N;
    static int ans = 0;
    static int[] arr;
    static int[] dp;
    static int max;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        arr = new int[N];
        dp = new int[N];
        

        for(int i = 0; i < N; i++) {
            int num = Integer.parseInt(br.readLine());
            arr[i] = num;
        }

        max = 0;
        Arrays.fill(dp, 1);

        for(int i = N-2; i >= 0; i--) {
            int curNum = arr[i];
            int tempMax = 1;

            for(int j = i+1; j < N; j++) {
                if(curNum < arr[j]) {
                    tempMax = Math.max(tempMax, dp[i] + dp[j]);
                }
            }
            dp[i] = tempMax;

            max = Math.max(max, dp[i]);
        }

        System.out.print(N - max);

    }
}

```