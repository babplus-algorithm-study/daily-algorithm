```java
class Main {


    static boolean[][] map;
    static int count = 0;
    static int R;
    static int C;

    public static void main(String[] args) throws Exception {
        R = read();
        C = read();
        map = new boolean[R + 2][C + 2];

        for(int i = 1; i <= R; i++) {
            for(int j = 1; j <= C; j++) {
                char c = (char) System.in.read();
                if(c == '.') {
                    map[i][j] = true;
                } else if(c == 'x') {
                    map[i][j] = false;
                }
            }
            System.in.read();
        }

        for(int i = 1; i <= R; i++) {
            dfs(i, 1);
        }
        System.out.println(count);
    }

    private static boolean dfs(int i, int j) {
        if(j == C) {
            count++;
            return true;
        }

        for(int k = -1; k < 2; k++) {
            if(!map[i + k][j + 1]) continue;
            map[i + k][j + 1] = false;
            if(dfs(i + k, j + 1)) return true;
        }

        return false;
    }


    private static int read() throws Exception {
        int d, o;
        boolean negative = false;
        d = System.in.read();
        if (d == 45) {
            negative = true;
            d = System.in.read();
        }

        o = d & 15;
        while ((d = System.in.read()) > 32)
            o = (o << 3) + (o << 1) + (d & 15);

        return negative ? -o : o;
    }
}
```
