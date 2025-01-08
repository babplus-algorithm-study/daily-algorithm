```java
package swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class P7206 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());

        int[] dp = new int[100_000];

        for(int i = 10; i < 100_000; i++) {
            back(i, i, 1, dp);
        }
        StringBuilder sb = new StringBuilder();
        for(int t = 1; t <= T; t++) {

            int number = Integer.parseInt(br.readLine());

            sb.append("#" + t +" " + dp[number]).append("\n");
            }

        System.out.println(sb.toString());
        }


    public static void back(int current,int val, int mul, int[] dp) {
        int radix = 10;

        dp[current] = Math.max(dp[val*mul] + 1, dp[current]);

        if(val < 10) return;

        while(val >= radix) {
            back(current,val / radix, mul * (val % radix),dp);
            radix *= 10;
            }
        }
    }


```