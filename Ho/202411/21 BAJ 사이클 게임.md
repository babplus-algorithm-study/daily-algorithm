```java
package gold;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.stream.IntStream;

public class P20040 {
    static int N,M;
    static int[] uf;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        uf = IntStream.range(0, N).toArray();

        // 사이클이 존재하는지 효율적으로 판단하는법이 중요하다.
        // 단방향으로 이동해서 출발지로 돌아올 수 있는가?
        boolean isFinsh = false;

        for(int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());

            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());

            if(union(start, end)) {
                System.out.println(i + 1);
                isFinsh = true;
                break;
            }
        }

        if(!isFinsh) {
            System.out.println(0);
        }

    }

    public static int find(int x) {
        if(uf[x] == x) return x;
        return uf[x] = find(uf[x]);
    }

    public static boolean union(int a, int b) {
        int parent = find(a);
        int child = find(b);

        if(parent == child) return true;

        if(parent > child) {
            int temp = parent;
            parent = child;
            child = temp;
        }

        uf[child] = parent;

        return false;
    }
}

```