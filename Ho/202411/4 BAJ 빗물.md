```java
package gold;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P14719 {
    static int N,M;
    static int[] info;
    static int[][] grid;
    static int ans = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        info = new int[M];
        grid = new int[N][M];

        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < M; i++) {
            info[i] = Integer.parseInt(st.nextToken());
        }
        makeGrid();
        getRainAmount();
        System.out.println(ans);
    }

    public static void makeGrid() {

        for(int i = 0; i < M; i++) {
            for(int j = 1; j <= info[i]; j++) {
                grid[N-j][i] = 1;
            }
        }
    }

    public static void getRainAmount() {
        for(int r =N-1; r >= 0; r--) {
            int left = -1;
            for(int c = 0; c < M; c++) {
                //맨 왼쪽 오른쪽이 비어 있으면 모일 수 가 없다.
                if(left == -1 && grid[r][c] == 1) {
                    left = c;
                }
                else if(grid[r][c] == 1 && left != -1) {
                    if(c - (left+1) > 0) {
                        ans += c - (left+1);
                    }
                    left = c;
                }
            }
        }
    }
}

```