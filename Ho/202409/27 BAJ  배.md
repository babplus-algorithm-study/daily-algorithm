```java
package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class P1092 {
    static int N;
    static int[] crains;
    static int M;
    static int[] boxes;
    static ArrayList<Integer> ramainBoxes = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        crains = new int[N];

        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < N; i++) {
            crains[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());
        boxes = new int[M];

        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < M; i++) {
            boxes[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(crains);
        Arrays.sort(boxes);

        for(int j = M -1; j >= 0; j--) {
            ramainBoxes.add(boxes[j]);
        }
        int answer = 0;

        if(crains[N-1] < boxes[M-1]) {
            System.out.println(-1);
            System.exit(0);
        }

        while(ramainBoxes.size() > 0) {
            int boxIndex = 0;
            int crainIndex = N-1;
            while(crainIndex > -1) {
                if(boxIndex == ramainBoxes.size()) {
                    break;
                }
                if(canMove(crainIndex, boxIndex)) {
                    ramainBoxes.remove(boxIndex);
                    crainIndex--;
                }
                else{
                    boxIndex++;
                }
            }
            answer++;
        }

        System.out.println(answer);
    }

    public static boolean canMove(int crainIndex, int boxIndex) {
        return crains[crainIndex] >= ramainBoxes.get(boxIndex);
    }
}

```