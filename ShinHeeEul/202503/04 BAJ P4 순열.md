```java
import java.util.*;
import java.io.*;

public class Main {
	
	static int[] segments;
	static int size;
	static int N;
	public static void main(String[] args) throws Exception {
		N = read();
		
		size = 1;
		
		while(size < N) {
			size <<= 1;
		}
		
		segments = new int[(size << 1) + 1];
		
		
		// 빈공간들의 합을 올리고
		
		int segmentSize = size << 1;
		while(segmentSize > 1) {
			if(segmentSize > size) {
				segments[segmentSize >> 1] = 2;
				segmentSize-=2;
			}
			else {
				segments[(segmentSize >> 1)] = segments[segmentSize] + segments[segmentSize - 1];
				segmentSize -= 2;
			}
		}

		for(int i = 1;  i <= N; i++) {
			int A = read();
			update(A, i);
		}
		
		StringBuilder sb = new StringBuilder();
		
		for(int i = size + 1; i < size + N + 1; i++) {
			sb.append(segments[i]).append("\n");
		}
		
		System.out.println(sb);
		
		
	}
	
	public static void update(int A, int idx) {
		
		// 2에서부터 내려가면서
		int index = 2;
		
		while(true) {

			// 거치는 애들 -1
			segments[index]--;
			int doubleIndex = index << 1;
			int doubleIndexMinusOne = doubleIndex - 1;
			// size보다 커지면? 해당 위치에 idx를 넣고 종료
			if(index > (size >> 1)) {
				if(A == 1) {
					segments[doubleIndex] = idx;
				} else {
					if(segments[doubleIndexMinusOne] != 0) {
						segments[doubleIndex] = idx;
					} else {
					segments[doubleIndexMinusOne] = idx;
					}
				}
				return;
			}
			
			// 좌측보다 크거나 같다?
			int left = segments[doubleIndexMinusOne];
			
			if(A >= left) {
				// 좌측만큼 빼주고 
				A -= left;
				// 우측으로 이동
				index = doubleIndex;
			}

			// 나머지 경우?
				// 좌측으로 이동
			else {
				index = doubleIndexMinusOne;
			}
		}
	}
	
    private static int read() throws Exception {
        int d, o;
        d = System.in.read();

        o = d & 15;

        while ((d = System.in.read()) > 32)
            o = (o << 3) + (o << 1) + (d & 15);

        return o;
    }
	
}
```
