```java
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws Exception {
        int N = read();
        int K = read();
        int[][] dp = new int[N + 1][K + 1];
        Arrays.fill(dp[0], 1);
        dp[0][0] = 0;
        for(int i = 0; i <= N ; i++) dp[i][1] = 1;

        for(int i = 1; i <= N; i++) {
            for(int j = 1; j <= K; j++) {
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % (1_000_000_000);
            }
        }

        System.out.println(dp[N][K]);
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
