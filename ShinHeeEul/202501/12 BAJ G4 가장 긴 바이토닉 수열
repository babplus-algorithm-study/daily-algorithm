```java
import java.io.*;

class Solution
{

    public static void main(String[] args) throws Exception
    {
        int N = read();
        int[] arr = new int[N];
        int[] dp = new int[N];
        int[] adp = new int[N];
        int[] rdp = new int[N];
        int index = 0;
        for(int i = 0; i < N; i++) arr[i] = read();

        dp[0] = arr[0];
        adp[0] = 1;
        for(int i = 1; i < N; i++) {
            index = getIndex(arr, dp, index, adp, i);
        }

        int reIndex = 0;
        int[] bdp = new int[N];
        rdp[0] = arr[N-1];
        bdp[N-1] = 1;
        for(int i = N-2; i >= 0; i--) {
            reIndex = getIndex(arr, rdp, reIndex, bdp, i);
        }

        int max = 0;
        for(int i = 0; i < N; i++) {
            max = Math.max(max, adp[i] + bdp[i]);
        }

        System.out.println(max - 1);

    }

    private static int getIndex(int[] arr, int[] rdp, int reIndex, int[] bdp, int i) {
        if(rdp[reIndex] < arr[i]) {
            rdp[++reIndex] = arr[i];
            bdp[i] = reIndex + 1;
            return reIndex;
        }
        int a =binary(reIndex, arr[i], rdp);
        bdp[i] = a + 1;
        rdp[a] = arr[i];
        return reIndex;
    }

    private static int binary(int index, int a, int[] dp) {
        int start = 0;
        int end = index;
        while(start < end) {
            int mid = (start + end) / 2;
            if(dp[mid] < a) {
                start = mid + 1;
            } else {
                end = mid;
            }
        }
        return end;
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
