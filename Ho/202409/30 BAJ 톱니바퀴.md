```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P14891 {
    static int[][] wheels = new int[4][8];
    static int[][] infos = new int[4][2];

    static int N;
    static int[][] cmd;

    public static void main(String[] args) throws IOException {
        // 톱니바퀴 회전시키려면 회전 시킬 톱니 바퀴랑 방향 결정하기
        // 옆에있는 톱니바퀴를 회전 시킬 수도 있고 아닐 수도 있다.
        // A가 회전할 때 맞닿는 톱니의 극이 다르면 B는 A가 회전한 방향과 반대로 회전
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int i = 0; i < 4; i++) {
            String line = br.readLine();
            for (int j = 0; j < 8; j++) {
                wheels[i][j] = line.charAt(j) - '0';
            }
        }

        N = Integer.parseInt(br.readLine());
        cmd = new int[N][2];

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            cmd[i][0] = Integer.parseInt(st.nextToken()) -1;
            cmd[i][1] = Integer.parseInt(st.nextToken());
            if(cmd[i][1] == -1) cmd[i][1] = 0;
        }

        infos[0] = new int[]{2, 0};
        infos[1] = new int[]{2, 6};
        infos[2] = new int[]{2, 6};
        infos[3] = new int[]{0, 6};

        simulate();

        int answer = 0;
        answer = calcAnswer();
        System.out.println(answer);

    }
    public static int calcAnswer() {
        int sum = 0;
        for (int i = 0; i < 4; i++) {

            if (i == 3) {
                int idx = (infos[i][1] + 2) % 8;
                if (wheels[i][idx] == 1) {
                    sum += 8;
                    break;
                }
            }

            int idx = (infos[i][0] + 6) % 8;

            if (wheels[i][idx] == 1) {
                if (i == 0)
                    sum += 1;
                if (i == 1)
                    sum += 2;
                if (i == 2)
                    sum += 4;
            }
        }
        return sum;
    }

    public static void simulate() {
        for (int i = 0; i < N; i++) {
            int curDirection = cmd[i][1];
            int originDir = cmd[i][1];

            curDirection = (curDirection + 1) % 2;

            //1번 톱니가 회전하는 경우
            if(cmd[i][0] == 0) {
                if(wheels[1][infos[1][1]] != wheels[0][infos[0][0]]) {
                    if (wheels[2][infos[2][1]] != wheels[1][infos[1][0]]) {
                        if (wheels[3][infos[3][1]] != wheels[2][infos[2][0]]) {
                            move(curDirection, 3);
                        }
                        move(originDir, 2);
                    }
                    move(curDirection, 1);
                }
            }

            // 2번 톱니가 처음 회전하는 경우
            if(cmd[i][0] == 1) {
                if(wheels[1][infos[1][1]] != wheels[0][infos[0][0]]) {
                    move(curDirection, 0);
                }
                if(wheels[1][infos[1][0]] != wheels[2][infos[2][1]]) {
                    if (wheels[2][infos[2][0]] != wheels[3][infos[3][1]]) {
                        move(originDir, 3);
                    }
                    move(curDirection, 2);
                }
            }

            // 3번 톱니가 처음 회전하는 경우
            if(cmd[i][0] == 2) {
                if(wheels[2][infos[2][0]] != wheels[3][infos[3][1]]) {
                    move(curDirection, 3);
                }
                if(wheels[2][infos[2][1]] != wheels[1][infos[1][0]]) {
                    if(wheels[1][infos[1][1]] != wheels[0][infos[0][0]]) {
                        move(originDir, 0);
                    }
                    move(curDirection, 1);
                }
            }

            //4번 톱니
            if(cmd[i][0] == 3) {
                if(wheels[3][infos[3][1]] != wheels[2][infos[2][0]]) {
                    if(wheels[2][infos[2][1]] != wheels[1][infos[1][0]]){
                        if(wheels[1][infos[1][1]] != wheels[0][infos[0][0]]){
                            move(curDirection, 0);
                        }
                        move(originDir, 1);
                    }
                    move(curDirection, 2);
                }
            }

            if(originDir == 1) {
                rotate(cmd[i][0]);
            }
            else{
                reverseRotate(cmd[i][0]);
            }
        }
    }

    public static void move(int dir,int index) {
        if(dir == 0) {
            reverseRotate(index);
        }
        else {
            rotate(index);
        }
    }

    public static void rotate(int index) {
        int cur = infos[index][0];
        cur = (cur + 7) % 8;
        infos[index][0] = cur;


        cur = infos[index][1];
        cur = (cur + 7) % 8;
        infos[index][1] = cur;


    }

    public static void reverseRotate(int index) {
        int cur = infos[index][0];
        cur = (cur + 9) % 8;
        infos[index][0] = cur;


        cur = infos[index][1];
        cur = (cur + 9) % 8;
        infos[index][1] = cur;

    }
}

```