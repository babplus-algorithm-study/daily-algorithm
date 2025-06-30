```java
import java.util.Arrays;

public class Main {

    // 거리, 나무가 몇 개인지
    static Node DEFAULT = new Node(0, 0);
    static Node[] segments;
    static int MOD = 1_000_000_007;
    static long answer = 1L;
    static int N;
    static int size;
    public static void main(String[] args) throws Exception {
        N = read();
        size = 1;

        while(size < 200_000) size <<= 1;
        segments = new Node[(size << 1) + 1];
        // 0부터 20만까지두고, 0~현재수의 합, 현재수~20만
        Arrays.fill(segments, DEFAULT);

        int start = read();
        update(start);

        for(int i = 1; i < N; i++) {
            int a = read();

            Node left = query(1, a + 1, 2, 1, size);
            Node right = query(a + 1, size, 2, 1, size);

            long val = (long) a * left.count - left.distance + right.distance - (long) a * right.count;
            val %= MOD;
            answer = (answer * val) % MOD;

            update(a);
        }

        System.out.println(answer);
    }

    static void update(int a) {

        int index = a + 1 + size;

        while(index >= 2) {
            segments[index] = new Node(segments[index].distance + a, segments[index].count + 1);
            index = (index + 1) >> 1;
        }
    }

    static Node query(int left, int right, int node, int start, int end) {
        if(end < left || right < start) return DEFAULT;

        if(left <= start && end <= right) {
            return segments[node];
        }

        int mid = (start + end) >> 1;
        Node leftNode = query(left, right, (node << 1) - 1, start, mid);
        Node rightNode = query(left, right, node << 1, mid + 1, end);

        return new Node(leftNode.distance + rightNode.distance, leftNode.count + rightNode.count);
    }

    static class Node {
        long distance;
        int count;

        public Node(long distance, int count) {
            this.distance = distance;
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
