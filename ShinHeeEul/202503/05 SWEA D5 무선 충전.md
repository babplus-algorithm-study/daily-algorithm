```java
import java.io.*;
import java.util.*;

public class Solution {

	static int H;
	static int W;
	
	// 얼음 상 우 하 좌 : 0 1 2 3 4
	static int[] di = {0, -1, 0, 1, 0};
	static int[] dj = {0, 0, 1, 0, -1};
	static BC[] bcs;
	static int[] p1;
	static int[] p2;
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(br.readLine());
		StringBuilder sb = new StringBuilder();
		for(int t = 1; t <= T; t++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			sb.append("#").append(t).append(" ");
			
			int M = Integer.parseInt(st.nextToken());
			int A = Integer.parseInt(st.nextToken());
			p1 = new int[] {1, 1};
			p2 = new int[] {10, 10};
			StringTokenizer p1Route = new StringTokenizer(br.readLine());
			StringTokenizer p2Route = new StringTokenizer(br.readLine());
			bcs = new BC[A];
			
			for(int i = 0; i < A; i++) {
				st = new StringTokenizer(br.readLine());
				bcs[i] = new BC(Integer.parseInt(st.nextToken()),
						Integer.parseInt(st.nextToken()),
						Integer.parseInt(st.nextToken()),
						Integer.parseInt(st.nextToken()));
			}
			
			Arrays.sort(bcs);
			
			int sum = 0;
			
			for(int i = 0; i <= M; i++) {
				int b1 = 0;
				int b2 = 0;
				int b3 = 0;
				for(int j = 0; j < A; j++) {
					
					if(b1 + b2 + b3 == 2) break;
					BC bc = bcs[j];
					boolean p1In = bc.isIn(p1[0], p1[1]);
					boolean p2In = bc.isIn(p2[0], p2[1]);
					if(p1In && p2In) {
						b3++;
						sum += bcs[j].p;
						continue;
					}
					
					if(b1 == 0 && p1In) {
						b1 = 1;
						sum += bcs[j].p;
					}
					
					if(b2 == 0 && p2In) {
						b2 = 1;
						sum += bcs[j].p;
					}
					
				}

				if(i == M) break;
				
				int p1Dir = Integer.parseInt(p1Route.nextToken());
				int p2Dir = Integer.parseInt(p2Route.nextToken());
				p1[0] += di[p1Dir];
				p1[1] += dj[p1Dir];
				p2[0] += di[p2Dir];
				p2[1] += dj[p2Dir];
			}
			
			sb.append(sum).append("\n");
			
		}
		System.out.println(sb);
	}
	
	static class BC implements Comparable<BC> {
		int i;
		int j;
		int c;
		int p;
	
		public BC(int j, int i, int c, int p) {
			this.i = i;
			this.j = j;
			this.c = c;
			this.p = p;
		}
		
		public int compareTo(BC b) {
			return b.p - this.p;
		}
		
		public boolean isIn(int i, int j) {
			return Math.abs(this.i - i) + Math.abs(this.j - j) <= c;
		}
	}
	
}

```
