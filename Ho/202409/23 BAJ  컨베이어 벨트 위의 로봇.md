```
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.StringTokenizer;

public class Main {

    static int N;
    static int K;
    static int[] conveyerBelt;
    static boolean[] isRobot;

    static int upIndex;
    static int downIndex;
    static int answer = 0;
    static HashSet<Integer> brokenRobotPos = new HashSet<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        upIndex = 0;
        downIndex = N-1;
        conveyerBelt = new int[2 * N];
        isRobot = new boolean[2 * N];

        st = new StringTokenizer(br.readLine());

        for(int i = 0; i < N * 2; i++) {
            conveyerBelt[i] = Integer.parseInt(st.nextToken());
        }

        simulate();
    }

    public static void simulate() {
        while(true) {
            if(isFinish()) {
                System.out.println(answer);
                return;
            }
            rotate();
            move();
            upRobot();

            answer++;
        }
    }

    // 1.회전
    public static void rotate() {
        //로봇과 함께 벨트를 움직인다.
        upIndex = (upIndex + (2*N)-1)  % (2*N);
        downIndex = (downIndex + (2*N)-1) % (2*N);
    }
    // 2. 이동가능한 경우 로봇 이동하기
    public static void move() {
        //가장 먼저 올라간 로봇이라면 downIndex와 가까움
        if(isRobot[downIndex]) {
            isRobot[downIndex] = false;
        }

        for(int i = 0; i < N; i++) {
            int curIndex = (downIndex + (2*N) - i) % (2*N);
            int preIndex = (downIndex + (2*N) - i - 1) % (2*N);

            if(canMove(curIndex, preIndex)) {
                //로봇을 옮길 수 있는 경우
                conveyerBelt[curIndex]--;
                isRobot[curIndex] = true;
                isRobot[preIndex] = false;
            }

            if(curIndex == downIndex) {
                isRobot[curIndex] = false;
            }
        }
    }

    public static boolean canMove(int moveIndex, int curIndex) {
        if(isRobot[curIndex]) {
            return !isRobot[moveIndex] && conveyerBelt[moveIndex] > 0;
        }
        return false;
    }

    public static void upRobot() {
        if(conveyerBelt[upIndex] > 0 ) {
            isRobot[upIndex] = true;
            conveyerBelt[upIndex]--;
        }
    }

    public static boolean isFinish() {
        for(int i =0; i < 2 *N; i++) {
            if(conveyerBelt[i] == 0) {
                brokenRobotPos.add(i);
            }
        }
        return brokenRobotPos.size() >= K;
    }
}

```