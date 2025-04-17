```java
import java.util.*;
import java.io.*;

class Main {
	
	static int MOD = 1_000_000_007;
	
	static StringBuilder sb = new StringBuilder();
	static String s;
	static long[] arr;
	static long[] max;
	static long[] min;
	static long ans = 0;
	static int N;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		N = read();
		
		// 슬라이딩 윈도우 처럼
		arr = new long[N];
		
		for(int i = 0; i < N; i++) {
			arr[i] = read();
		}
		
		// 정렬 하고?
		Arrays.sort(arr);
		
        long[] pow2 = new long[N];
        pow2[0] = 1;
        for (int i = 1; i < N; i++) {
            pow2[i] = (pow2[i-1] * 2) % MOD;
        }
        
        
		
		for(int i = arr.length - 1; i >= 0; i--) {
			ans = (ans + arr[i] * ((pow(2, i) - pow(2, N - i - 1) + MOD) % MOD) % MOD) % MOD;
		}
		
		
		System.out.println(ans);
	}
	
	
	public static long pow(long n, long r) {
		
		n %= MOD;
		long result = 1L;
		while(r > 0) {
			if((r & 1) == 1) {
				result = (result * n) % MOD;
			}
			n = (n * n) % MOD;
			r >>= 1;
		}
		
		return result % MOD;
	}

	private static int read() throws Exception {
	    int c;
	    int n = 0;
	    boolean negative = false;

	    while ((c = System.in.read()) <= 32) {
	        if (c == -1) return -1;
	    }

	    if (c == '-') {
	        negative = true;
	        c = System.in.read();
	    }

	    do {
	        n = n * 10 + (c - '0');
	        c = System.in.read();
	    } while (c > 32);

	    return negative ? -n : n;
	}


}
```
