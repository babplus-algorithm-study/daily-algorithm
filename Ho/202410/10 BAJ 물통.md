```java
package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.SortedSet;
import java.util.StringTokenizer;
import java.util.TreeSet;

public class P2251 {
    static int[] bottles;
    static boolean[][][] visited;
    static SortedSet<Integer> set = new TreeSet<Integer>();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        // A 물통에 n 있을 때 C에서 가져 감을 판단하고 싶음
        visited = new boolean[201][201][6];
        bottles = new int[3];
        for(int i = 0; i < 3; i++) {
            bottles[i] = Integer.parseInt(st.nextToken());
        }


        dfs(0, 0, bottles[2]);


        for (Integer i : set) {
            System.out.print(i + " ");
        }
    }

    public static void dfs(int a, int b, int c) {
        // 3 -> 2
        if(!visited[c][b][0] && b != bottles[1]) {
            visited[c][b][0] = true;

            // b에 넣을 수 있는 양
            int bAmount = bottles[1] - b;

            bAmount = Math.min(c, bottles[1] - b);
            addAnswer(a,c - bAmount);
            dfs(a, b + bAmount, c - bAmount);
        }
        // 3 -> 1
        if(!visited[c][a][1] && a != bottles[0]) {
            visited[c][a][1] = true;

            int aAmount = bottles[0] - a;

            aAmount = Math.min(c, bottles[0] - a);
            addAnswer(a + aAmount,c - aAmount);
            dfs(a + aAmount, b, c - aAmount);
        }
        // 2 -> 1
        if(!visited[b][a][2] && a != bottles[0]) {
            visited[b][a][2] = true;

            int aAmount = bottles[0] - a;

            aAmount = Math.min(b, bottles[0] - a);
            addAnswer(a + aAmount,c);
            dfs(a + aAmount, b - aAmount, c);
        }
        // 2- > 3
        if(!visited[b][c][3] && c != bottles[2]) {
            visited[b][c][3] = true;

            int cAmount = bottles[2] - c;
            cAmount = Math.min(b, bottles[2] - c);
            addAnswer(a,c + cAmount);
            dfs(a, b - cAmount, c + cAmount);
        }
        // 1 -> 3
        if(!visited[a][c][4] && c != bottles[2]) {
            visited[a][c][4] = true;
            int cAmount = bottles[2] - c;

            cAmount = Math.min(a, bottles[2] - c);
            addAnswer(a - cAmount,c + cAmount);
            dfs(a - cAmount, b, c + cAmount);
        }
        // 1 -> 2
        if(!visited[a][b][5] && b != bottles[1]) {
            visited[a][b][5] = true;
            int bAmount = bottles[1] - b;

            bAmount = Math.min(a, bottles[1] - b);
            addAnswer(a - bAmount,c);
            dfs(a - bAmount, b + bAmount, c);
        }
    }

    static public void addAnswer(int a, int c) {
        if(a == 0) {
            set.add(c);
        }
    }

}

```