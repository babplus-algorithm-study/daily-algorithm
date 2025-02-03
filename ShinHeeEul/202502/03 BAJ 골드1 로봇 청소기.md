```java
    import java.io.*;
    import java.util.*;

    class Solution {
        static char[][] map;
        static int[][] dustDis;
        static Node[] dusts;
        static Map<Integer, Integer> dustIndex;
        static int N = 1;
        static int M = 1;
        static boolean[][] visited;
        static int count;
        static BufferedReader br;
        static StringTokenizer st;

        public static void main(String args[]) throws Exception {
            br = new BufferedReader(new InputStreamReader(System.in));
            StringBuilder sb = new StringBuilder();

            while (true) {
                M = read();
                N = read();
                if (M == 0 && N == 0) break;

                dusts = new Node[11];
                count = 1;
                dustIndex = new HashMap<>();
                map = new char[N][M];

                for (int i = 0; i < N; i++) {
                    for (int j = 0; j < M; j++) {
                        map[i][j] = (char) System.in.read();
                        if (map[i][j] == '*') {
                            dustIndex.put(i * 20 + j, count);
                            dusts[count] = new Node(i, j);
                            count++;
                        }
                        if (map[i][j] == 'o') {
                            dusts[0] = new Node(i, j);
                        }
                    }
                    System.in.read();
                }

                dustDis = new int[count + 1][count + 1];
                for (int i = 0; i < count; i++) {
                    bfs(dusts[i].i, dusts[i].j, i);
                }

                int ans = bitMasking();
                sb.append(ans == 0 || ans == (Integer.MAX_VALUE >> 1) ? -1 : ans).append("\n");
            }

            System.out.print(sb);
        }

        public static int bitMasking() {
            count--;
            int[][] dustDP = new int[1 << count][count + 1];
            for (int i = 0; i < (1 << count); i++)
                Arrays.fill(dustDP[i], Integer.MAX_VALUE >> 1);

            for (int i = 0; i < count; i++) dustDP[1 << i][i + 1] = dustDis[0][i + 1];

            for (int i = 0; i < (1 << count); i++) {
                for (int k = 1; k <= count; k++) {
                    for (int j = 0; j < count; j++) {
                        int a = 1 << j;
                        int ba = a | i;
                        if (ba == i || ba >= dustDP.length || dustDis[k][j + 1] == 0) continue;
                        dustDP[ba][j + 1] = Math.min(dustDP[ba][j + 1], dustDP[i][k] + dustDis[k][j + 1]);
                    }
                }
            }

            int min = Integer.MAX_VALUE;
            for (int i = 0; i <= count; i++) {
                min = Math.min(dustDP[(1 << count) - 1][i], min);
            }
            return min;
        }

        public static void bfs(int si, int sj, int index) {
            visited = new boolean[N][M];
            int[] di = {1, -1, 0, 0};
            int[] dj = {0, 0, 1, -1};

            Queue<Dust> queue = new LinkedList<>();
            queue.add(new Dust(si, sj, 0));
            visited[si][sj] = true;

            while (!queue.isEmpty()) {
                Dust dust = queue.poll();
                int i = dust.i;
                int j = dust.j;
                int count = dust.count;

                int d = dustIndex.getOrDefault(i * 20 + j, -1);
                if (d != -1) {
                    dustDis[index][d] = count;
                }

                for (int k = 0; k < 4; k++) {
                    int ii = i + di[k];
                    int jj = j + dj[k];

                    if (!check(ii, jj)) continue;
                    visited[ii][jj] = true;
                    queue.add(new Dust(ii, jj, count + 1));
                }
            }
        }

        public static boolean check(int i, int j) {
            if (i < 0 || i >= N || j < 0 || j >= M) return false;
            if (map[i][j] == 'x') return false;
            return !visited[i][j];
        }

        public static class Node {
            int i, j;
            public Node(int i, int j) {
                this.i = i;
                this.j = j;
            }
        }

        public static class Dust {
            int i, j, count;
            public Dust(int i, int j, int count) {
                this.i = i;
                this.j = j;
                this.count = count;
            }
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
