```java
import java.util.*;
import java.io.*;

class Main {


    static Node[] segments;
    static int N;
    static int size;
    static int MIN = Integer.MIN_VALUE >> 1;
    static Node DEFAULT = new Node(MIN,MIN,MIN,0);
    public static void main(String[] args) throws Exception {


        N = read();
        size = 1;

        while(size < N) {
            size <<= 1;

        }

        segments = new Node[(size << 1) + 1];

        for(int i = size + 1; i < size + N + 1; i++) {
            int a = read();
            segments[i] = new Node(a, a, a, a);
        }

        for(int i = size + N + 1; i < (size << 1) + 1; i++) segments[i] = DEFAULT;

        init();

        int M = read();
        StringBuilder sb = new StringBuilder();
        while(M-->0) {
            Node node = query(read(), read(), 2, 1, size);
            sb.append(node.max).append("\n");
        }
        System.out.println(sb);
    }

    public static Node query(int left, int right, int node, int start, int end) {
        if(end < left || right < start) return DEFAULT;

        if(left <= start && end <= right) {
            return segments[node];
        }

        int mid = (start + end) >> 1;
        Node leftNode = query(left,  right, (node << 1) - 1, start, mid);
        Node rightNode = query(left, right, node << 1, mid + 1, end);
        return new Node(Math.max(leftNode.lmax, leftNode.sum + rightNode.lmax),
                Math.max(rightNode.rmax, rightNode.sum + leftNode.rmax),
                Math.max(leftNode.max, Math.max(rightNode.max, leftNode.rmax + rightNode.lmax)),
                leftNode.sum + rightNode.sum);

    }

    public static void init() {

        int segmentSize = size << 1;

        while(segmentSize > 2) {
            Node leftNode = segments[segmentSize - 1];
            Node rightNode = segments[segmentSize];
            // 범위 내의 제일 좌측 노드를 포함하는 연속합은?
            // (왼쪽 자식의 leftMax), (왼쪽 자식의 sum) + (우측 자식 노드의 leftMax)

            // 범위 내의 제일 우측 노드를 포함하는 연속합은?
            // (우측 자식의 rightMax), (우측 자식의 sum) + (좌측 자식 노드의 rightMax)

            // 범위 내의 최대 합은?
            // (왼쪽 자식의 leftMax), (우측 자식의 rightMax), (왼쪽 자식의 rightMax + 우측 자식의 leftMax)

            segments[segmentSize >> 1] = new Node(
                    Math.max(leftNode.lmax, leftNode.sum + rightNode.lmax),
                    Math.max(rightNode.rmax, rightNode.sum + leftNode.rmax),
                    Math.max(leftNode.max, Math.max(rightNode.max, (leftNode.rmax + rightNode.lmax))),
                    leftNode.sum + rightNode.sum
            );
            segmentSize -= 2;
        }

    }

    static class Node {
        // 범위 내의 제일 좌측 노드를 포함하는 최대 연속합
        int lmax;
        // 범위 내의 제일 우측 노드를 포함하는 최대 연속합
        int rmax;
        // 범위 내의 최대  연속합
        int max;
        // 구간 합
        int sum;

        public Node(int leftMax, int rightMax, int max, int sum) {
            this.lmax = leftMax;
            this.rmax = rightMax;
            this.max = max;
            this.sum = sum;

        }
    }

    private static int read() throws Exception {
        int c;
        int n = 0;
        boolean negative = false;

        while ((c = System.in.read()) <= 32) {
            if (c == -1) return -1;
        }

        if (c == '-') {
            negative = true;
            c = System.in.read();
        }

        do {
            n = n * 10 + (c - '0');
            c = System.in.read();
        } while (c > 32);

        return negative ? -n : n;
    }

}
```
