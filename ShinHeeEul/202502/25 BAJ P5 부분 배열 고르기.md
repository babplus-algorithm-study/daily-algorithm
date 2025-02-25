```java
import java.util.Arrays;

public class Main {

    static long[] sums;
    static Node[] segments;
    static int size;
    static int N;
    static long max;

    static Node MAX_NODE = new Node(-1, Integer.MAX_VALUE);

    public static void main(String[] args) throws Exception {

        N = read();
        size = 1;
        sums = new long[N + 1];

        while(size < N) {
            size <<= 1;
        }

        segments = new Node[(size << 1) + 1];
        Arrays.fill(segments, MAX_NODE);
        for(int i = size + 1; i < size + N + 1; i++) {
            int a = read();
            int b = i - size;
            sums[b] = a + sums[b - 1];
            segments[i] = new Node(b, a);
        }

        int segmentSize = (size << 1);

        while(segmentSize > 1) {
            Node a = segments[segmentSize - 1];
            Node b = segments[segmentSize];
            int c = segmentSize >> 1;
            if(a.min < b.min) {
                segments[c] = a;
            } else {
                segments[c] = b;
            }
            segmentSize -= 2;
        }

        backTracking(1, N);
        System.out.println(max);
    }

    public static void backTracking(int start, int end) {
        if(start > end || start <= 0 || start > N || end > N) return;
        Node node = query(start, end, 2, 1, size);

        max = Math.max(max, node.min * (sums[end] - sums[start - 1]));

        if(end == start) return;
        int index = node.index;
        backTracking(start, index - 1);
        backTracking(index + 1, end);
    }

    public static Node query(int left, int right, int node, int start, int end) {
        if(end < left || right < start) return MAX_NODE;

        if(left <= start && end <= right) {
            return segments[node];
        }

        int mid = (start + end) >> 1;
        int halfNode = (node << 1);
        Node a = query(left, right, halfNode - 1, start, mid);
        Node b = query(left, right, halfNode, mid + 1, end);

        if(a.min < b.min) {
            return a;
        }
        return b;
    }

    public static class Node {
        int index;
        int min;

        Node(int index, int min) {
            this.index = index;
            this.min = min;
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
