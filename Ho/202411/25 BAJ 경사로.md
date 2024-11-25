```java
package gold;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P14890 {
    static int N,L;
    static int[][] grid;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        L = Integer.parseInt(st.nextToken());

        grid = new int[N][N];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                grid[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int ans = 0;
        for (int i = 0; i < N; i++) {
            //한번은 행을 확인 한번은 열을 확인
            if (isPath(i, 0,0)) {
                ans++;
            }
            if(isPath(0,i,1)) {
                ans++;
            }
        }
        System.out.println(ans);
    }

    public static boolean isPath(int row, int col, int dir) {
        boolean[] isUsed = new boolean[N];

        if(dir == 0) {
            //행 고정
            for (int i = 0; i < N - 1; i++) {
                if(grid[row][i] == grid[row][i + 1]) {
                    //높이가 같은 경우
                    continue;
                }
                else{
                    //높이가 다른 경우
                    if(Math.abs(grid[row][i] - grid[row][i + 1]) > 1) {
                        // 1보다 큰 경우는 불가능
                        return false;
                    }
                    else{
                        // gap이 1인 경우 경사로를 만들어서 처리 가능한지 확인
                        if(grid[row][i] < grid[row][i + 1]) {

                            for (int j = 0; j < L; j++) {
                                if(!inRange(i-j)) {
                                    return false;
                                }
                                if(isUsed[i-j] || grid[row][i-j] != grid[row][i]) return false;
                                isUsed[i-j] = true;
                            }
                        }
                        else{
                            // 왼쪽이 더 높은 경우
                            for (int j = 1; j <= L; j++) {
                                if(!inRange(i + j)) return false;
                                if(isUsed[i+j] || grid[row][i+j] != grid[row][i + 1]) return false;
                                isUsed[i+j] = true;
                            }
                        }
                    }
                }
            }

        }
        else{
            //열 고정
            for (int i = 0; i < N - 1; i++) {


                if(grid[i][col] == grid[i+1][col]) {
                    //높이가 같은 경우
                    continue;
                }
                else{
                    //높이가 다른 경우
                    if (Math.abs(grid[i][col] - grid[i + 1][col]) > 1) {
                        // 1보다 큰 경우는 불가능
                        return false;
                    } else {
                        // gap이 1인 경우 경사로를 만들어서 처리 가능한지 확인
                        if (grid[i][col] < grid[i + 1][col]) {
                            // 이런 경우에는 외쪽으로  확인해야함
                            for (int j = 0; j < L; j++) {
                                if (!inRange(i - j)) {
                                    return false;
                                }
                                if (isUsed[i - j] || grid[i-j][col] != grid[i][col]) {
                                    return false;
                                }
                                isUsed[i - j] = true;
                            }
                        } else {
                            // 왼쪽이 더 높은 경우
                            for (int j = 1; j <= L; j++) {
                                if (!inRange(i + j)) {
                                    return false;
                                }
                                if (isUsed[i + j] || grid[i+j][col] != grid[i + 1][col]) {
                                    return false;
                                }
                                isUsed[i + j] = true;
                            }
                        }
                    }
                }
            }
        }
        return true;
    }

    public static boolean inRange(int idx) {
        return idx >= 0 && idx < N;
    }
}

```