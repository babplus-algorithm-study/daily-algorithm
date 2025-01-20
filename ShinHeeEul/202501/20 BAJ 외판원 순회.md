```java
import java.util.*;
import java.io.*;

class Main {

	public static void main(String args[]) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());

		int[][] arr = new int[N][N];

		for (int i = 0; i < N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++)
				arr[i][j] = Integer.parseInt(st.nextToken());
		}

		int size = (1 << N);

		// dp[i][j]면 dp[i]번째에 j를 거쳐서 온 것.
		// 내가 이미 방문을 한 거면 방문하지 않기.
		// n은 시작 위치
		int[][][] dp = new int[size][N][N];
		
		for(int i = 0; i < size; i++) {
			for(int j = 0; j < N; j++) {
				Arrays.fill(dp[i][j], Integer.MAX_VALUE >> 1);
			}
		}
		
		for(int i = 0; i < N; i++) {
				dp[1 << i][i][i] = 0;
		}
		
		// 출발 index
		int max = Integer.MAX_VALUE;
			for (int i = 1; i < size; i++) {
				for(int j = 0; j < N; j++) {
					// i를 방문하고 온 j의 위치
					// 1인데 1이면? 말이 안되잖아.
					// 10이면 1010 근데 3면? 업뎃쳐야지 다음으로 갈 거
					// 근데 1000 인데 3이면?말이 안되잖아 방문 안된거니까
					// 그니까 1 << j랑 i랑 같다면? continue;인거네
					// 만약 i에 j가 이미 방문되어 있다면? (1 << j | i) == i라면?
						// continue;
					// dp[i][j] = Math.min(dp[i][j], );
					for (int k = 0; k < N; k++) {
						int kk = 1 << k;
						if (((i | kk) == i))
							continue;
						int tmp = kk ^ i;
						if (tmp >= size)
							continue;
						if(arr[j][k] == 0) continue;
						
						if(tmp == size - 1) {
							// 원래대로 돌아가는 걸.. 어떻게 하냐..
							for(int l = 0; l < N; l++) {
								if(arr[k][l] == 0) continue;
								dp[tmp][k][l] = Math.min(dp[tmp][k][l], dp[i][j][l] + arr[j][k] + arr[k][l]);
							}
						} else {
							for(int l = 0; l < N; l++)
							dp[tmp][k][l] = Math.min(dp[tmp][k][l], dp[i][j][l] + arr[j][k]);
						}
					}
				}
				
			}

		
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < N; j++)
				max = Math.min(max, dp[size - 1][i][j]);
		}
		System.out.println(max);

	}

	private static int read() throws Exception {
		int d, o;
		boolean negative = false;
		d = System.in.read();
		if (d == '-') {
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
