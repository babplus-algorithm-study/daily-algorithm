import java.io.*;
import java.util.*;

public class Main {
    static class Node {
        Node[] child = new Node[2];
        long  color = -1;
        int   time  = 0;
    }

    static Node root = new Node();
    static int curTime = 1;
    static long C;

    static Node getChild(Node p, int dir) {
        if (p.child[dir] == null) p.child[dir] = new Node();
        return p.child[dir];
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int q = Integer.parseInt(st.nextToken());
        C     = Long.parseLong(st.nextToken());
        StringBuilder out = new StringBuilder();

        for (int i = 0; i < q; i++) {
            st = new StringTokenizer(br.readLine());
            int t = Integer.parseInt(st.nextToken());

            if (t == 1) {                       // 색칠
                long x = Long.parseLong(st.nextToken());
                String s = br.readLine();
                Node cur = root;
                for (char ch : s.toCharArray())
                    cur = getChild(cur, ch == 'L' ? 0 : 1);
                cur.color = x;
                cur.time  = curTime++;
            } else {                            // 조회
                String s = br.readLine();
                Node cur = root;
                long diff = 0;
                long bestColor = root.color;
                long bestDiff  = 0;
                int  bestTime  = root.time;

                for (char ch : s.toCharArray()) {
                    int dir = ch == 'L' ? 0 : 1;
                    diff += dir == 0 ? 1 : -1;
                    cur = getChild(cur, dir);
                    if (cur.time > bestTime) {
                        bestTime  = cur.time;
                        bestColor = cur.color;
                        bestDiff  = diff;
                    }
                }

                if (bestTime == 0) out.append(-1).append('\n');
                else {
                    long ans = (bestColor + (diff - bestDiff)) % C;
                    if (ans < 0) ans += C;
                    out.append(ans).append('\n');
                }
            }
        }
        System.out.print(out);
    }
}
