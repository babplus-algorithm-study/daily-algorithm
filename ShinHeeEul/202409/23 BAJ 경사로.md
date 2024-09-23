```java
public class Main {

    static int N;
    static int L;
    static int[][] map;
    public static void main(String[] args) throws Exception {
        N = read();
        L = read();

        map = new int[N + 2][N + 2];

        for(int i = 1 ; i <= N; i++) {
            for(int j = 1; j <= N; j++) {
                map[i][j] = read();
            }
        }

        int count = 0;
        for(int i = 1; i <= N; i++) {
            if(iCheck(i)) count++;
            if(jCheck(i)) count++;
        }

        System.out.println(count);

    }

    public static boolean iCheck(int i) {
        return mainCheck(map[i]);
    }


    public static boolean jCheck(int j) {
        int[] tmp = new int[N + 2];

        for(int i = 1; i <= N; i++) {
            tmp[i] = map[i][j];
        }
        return mainCheck(tmp);
    }

    public static boolean mainCheck(int[] map) {
        //이전값이자 시작값
        int before = map[1];
        boolean[] visited = new boolean[N + 2];
        for(int j = 2; j <= N; j++) {
            int node = map[j];

            //이전값이랑 동일한 경우? continue
            if(before == node) continue;

            // 만약 이전 값보다 2이상 차이나면 false
            if(Math.abs(node - before) >= 2) return false;

            // 만약 node가 before보다 크다면?
            if(node > before) {
                // l j-L-1부터 j-1까지
                int tmp = map[j-1];
                for(int k = j-1; k >= j-L; k--) {
                    int l = map[k];
                    // l이 tmp와 다르다면 false
                    if(l != tmp) return false;
                    // visited[k]이 true라면 false
                    if(visited[k]) return false;
                    // visited를 true로 만들어줌
                    visited[k] = true;
                }
            } else {
                // 만약 node가 before보다 작다면?
                // l j부터 j + L까지
                for(int k = j; k < j + L; k++) {
                    int l = map[k];
                    // l이 node와 다르다면 false
                    if(l != node) return false;
                    // visited[k]이 true라면 false
                    if(visited[k]) return false;
                    // visited를 true로 만들어줌
                    visited[k] = true;
                }
            }

            before = node;
        }
        return true;
    }




    private static int read() throws Exception {
        int d, o;
        boolean negative = false;
        d = System.in.read();
        if (d == '-') {
            negative = true;
            d = System.in.read();
        }

        o = d & 15;
        while ((d = System.in.read()) > 32)
            o = (o << 3) + (o << 1) + (d & 15);

        return negative? -o:o;
    }
}

```
