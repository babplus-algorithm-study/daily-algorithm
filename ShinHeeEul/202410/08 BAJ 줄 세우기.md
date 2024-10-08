```java
class Main {


    static int[] dp;
    public static void main(String[] args) throws Exception {

        int n = read();
        dp = new int[n];

        int count = 0;
        int ans = 0;
        for(int i = 0; i < n; i++) {
            int a = read();

            if(a > dp[count]) {
                dp[++count] = a;
            } else {
                int start = 0;
                int end = count;

                while(start < end) {
                    int mid = (start + end) >> 1;

                    if(dp[mid] < a) {
                        start = mid + 1;
                    } else {
                        end = mid;
                    }
                }
                ans++;
                dp[start] = a;
            }
        }
        System.out.println(ans);
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
