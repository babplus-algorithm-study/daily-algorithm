```java
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

    static int[][] dp;
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();

        // 나 포함x 나 포함
        dp = new int[s.length() + 1][2];

        if(s.charAt(0) == '0') {
            System.out.println(0);
            return;
        }
        else dp[1][0] = 1;


        for(int i = 1; i < s.length(); i++) {
            int cur = Integer.parseInt(s.charAt(i) + "");
            int before = Integer.parseInt("" + s.charAt(i - 1) + s.charAt(i));
            if(cur != 0) {
                dp[i + 1][0] += dp[i][0];
            }
            if(before == 0) {
                System.out.println(0);
                return;
            }
            if(before >= 10 && before < 27) {
                dp[i + 1][0] += Math.max(dp[i][1], 1);
            }
            dp[i + 1][1] = dp[i][0];

            dp[i + 1][0] %= 1000000;
            dp[i + 1][1] %= 1000000;
        }

        System.out.println(dp[s.length()][0]);
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
