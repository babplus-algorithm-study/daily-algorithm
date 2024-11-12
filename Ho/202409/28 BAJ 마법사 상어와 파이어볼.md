```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class P20056 {
    static int N;
    static int M;
    static int K;

    static int[][] grid;

    static ArrayList<Fireball> fireballs = new ArrayList<>();

    static ArrayList<Fireball>[][] map;



    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        grid = new int[N][N];
        map = new ArrayList[N][N];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++)
                map[i][j] = new ArrayList<>();
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());

            int r = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            int s = Integer.parseInt(st.nextToken());
            int d = Integer.parseInt(st.nextToken());

            fireballs.add(new Fireball(r-1,c-1,m,s,d));
        }
        simulate();

    }

    public static void simulate() {
        for (int p = 0; p < K; p++) {
            for (int i = fireballs.size() - 1; i >= 0 ; i--) {
                move(fireballs.get(i), i);
            }

            merge();

        }
        int answer = 0;

        for (Fireball fireball : fireballs) {
            answer += fireball.mass;
        }

        System.out.println(answer);
    }

    public static void merge() {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if(map[i][j].size() < 2) {
                    map[i][j].clear();
                    continue;
                }

                int mSum = 0, sSum = 0, oddCount = 0;
                int size = map[i][j].size();

                for (Fireball curFireball : map[i][j]) {
                    mSum += curFireball.mass;
                    sSum += curFireball.speed;

                    if(curFireball.direction % 2 != 0) {
                        oddCount++;
                    }
                    fireballs.remove(curFireball);
                }

                map[i][j].clear();

                mSum /= 5;
                sSum /= size;

                if(mSum == 0) {
                    continue;
                }

                if(oddCount == 0 || oddCount == size) {
                    int[] evenDir = {0, 2, 4, 6};
                    for (int dir : evenDir) {
                        fireballs.add(new Fireball(i, j, mSum, sSum, dir));
                    }
                }
                else{
                    int[] oddDir = {1, 3, 5, 7};
                    for (int dir : oddDir) {
                        fireballs.add(new Fireball(i, j, mSum, sSum, dir));
                    }
                }
            }
        }

    }

    public static void move(Fireball fireball,int idx) {
        int[] drs = {-1, -1, 0, 1, 1, 1, 0, -1};
        int[] dcs = {0, 1, 1, 1, 0, -1, -1, -1};

        int nextRow = fireball.row + (drs[fireball.direction] * fireball.speed);
        int nextCol = fireball.col + (dcs[fireball.direction] * fireball.speed);

        if(nextRow >= N) {
            nextRow %= N;
        }

        if(nextCol >= N) {
            nextCol %= N;
        }

        while(nextRow < 0) {
            nextRow += N;
        }

        while(nextCol < 0) {
            nextCol += N;
        }

        fireball.row = nextRow;
        fireball.col = nextCol;

        map[nextRow][nextCol].add(fireball);
    }

    public static boolean inRange(int r, int c) {
        return 0 <= r && r < N && 0 <= c && c < N;
    }

    static class Fireball {
        int row;
        int col;
        int mass;
        int speed;
        int direction;
        int index = 2501;
        boolean onlyEven = true;

        public Fireball(int row, int col, int mass, int speed, int direction) {
            this.row = row;
            this.col = col;
            this.mass = mass;
            this.speed = speed;
            this.direction = direction;
        }

    }
}

```