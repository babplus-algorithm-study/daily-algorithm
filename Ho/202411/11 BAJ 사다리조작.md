```java
package gold;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class P15684 {
    static int N,M,H;
    static char[][] board;
    static boolean isEnd = false;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        H = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        board = new char[M][N];

        for (int i = 0; i < H; i++) {
            st = new StringTokenizer(br.readLine());
            int r = Integer.parseInt(st.nextToken()) - 1;
            int c = Integer.parseInt(st.nextToken()) - 1;

            board[r][c] = true;
        }

        // 내려보고 불가능하면 하나 설치하기
        if (down()) {
            isEnd = true;
            System.out.println("0");
        }
        else{
            //설치하고 down을 반복
            for(int i = 3; i < 4; i++) {
                back(0,0,0,i);
            }
        }
    }

    public static void back(int r, int c, int level, int max) {
        if(isEnd) return;
        if(level == max )  {
            if(down()) {
                // 내려가면 끝냄
                isEnd = true;
                System.out.println(max);
            }
            return;
        }

        for(int i = r; i < M; i++) {
            if(i > r) c = 0;
            for(int j = c; j <  N - 1; j++) {
                if(canLet(i,j)) {
                    board[i][j] = true;
                    back(i, j, level + 1, max);
                    board[i][j] = false;
                }
            }
        }
    }

    public static boolean canLet(int r, int c) {
            if(board[r][c]) {return false;}
            if(c == 0) {
                if(board[r][c + 1]) return false;
            }

            else if(c == N - 1) {
                if(board[r][c-2]) return false;
            }
            else{
                if(board[r][c-1]) return false;
                if(board[r][c]) return false;
            }
        //자기랑 동일한 열은 오른쪽으로   // 작은거는 왼쪽으로
        return true;
    }

    public static boolean down() {
        for(int i = 0; i < N; i++) {
            // 0번 레일부터 내려가기
            int curH = 0;
            int curC = i;

            while(curH < M) {
                if(curC == 0) {
                    // 왼쪽은 볼 필요 없음
                    if(board[curH][curC]) curC++;
                }

                else if(curC == N - 1) {
                    //오른쪽은 볼 필요 없음
                    if(board[curH][curC - 1]) curC--;
                }

                else {
                    if(board[curH][curC]) {
                        curC++;
                        continue;
                    }
                    if(board[curH][curC - 1]) curC--;
                }
                curH++;
            }
            if(curC != i) return false;
        }
        return true;
    }
}

```
미완성...틀림