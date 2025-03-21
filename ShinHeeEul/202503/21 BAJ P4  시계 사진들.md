```java
import java.io.*;
import java.util.Arrays;
import java.util.HashMap;


public class Main {


    static HashMap<Integer, Integer> map1 = new HashMap<>();
    static HashMap<Integer, Integer> map2 = new HashMap<>();
    static int[] s1;
    static int[] s2;

    static int[] failure;
    static int N;

    static final int MAX = 360_000;

    public static void main(String[] args) throws Exception {
        N = read();

        int[] arr1 = new int[N];
        int[] arr2 = new int[N];

        for(int i = 0; i < N; i++) {
            arr1[i] = read();
        }

        for(int i = 0; i < N; i++) {
            arr2[i] = read();
        }

        Arrays.sort(arr1);
        Arrays.sort(arr2);

        failure = new int[N];

        s1 = new int[N];
        s2 = new int[N << 1];

        int sum = 0;
        for(int i = 0; i < N-1; i++) {
            s1[i] = arr1[i + 1] - arr1[i];
            s2[i] = arr2[i + 1] - arr2[i];
            s2[N + i] = s2[i];
            sum ^= s1[i];
            sum ^= s2[i];
        }

        s1[N-1] = MAX + arr1[0] - arr1[N-1];
        s2[N-1] = MAX + arr2[0] - arr2[N-1];

        sum ^= s1[N-1];
        sum ^= s2[N-1];

        if(sum != 0) {
            System.out.println("impossible");
            return;
        }
        failureFunction();
        System.out.println(kmp() ? "possible" : "impossible");
    }

    private static void failureFunction() {
        int p = 0;

        for(int idx = 1; idx < N; idx++) {
            while(p != 0 && s1[idx] != s1[p]) p = failure[p - 1];

            if(s1[idx] == s1[p]) {
                p++;
                failure[idx] = p;
            }
        }

    }

    private static boolean kmp() {
        int p = 0;

        for(int idx = 0; idx < (N << 1); idx++) {
            while(p != 0 && s2[idx] != s1[p]) p = failure[p - 1];

            if(s2[idx] == s1[p]) {
                if(p == N - 1) {
                    return true;
                }
                p++;
            }
        }
        return false;
    }

    private static int read() throws IOException {
        int d, o = 0;
        boolean negative = false;

        while ((d = System.in.read()) <= 32);

        if (d == '-') {
            negative = true;
            d = System.in.read();
        }

        do {
            o = (o << 3) + (o << 1) + (d & 15); // o = o * 10 + (d - '0')
        } while ((d = System.in.read()) >= '0' && d <= '9');

        return negative ? -o : o;
    }
}
```
