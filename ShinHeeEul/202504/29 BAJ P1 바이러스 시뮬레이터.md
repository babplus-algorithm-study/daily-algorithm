```java
import java.io.FileInputStream;

class Main {

        static int N;
        static int Q;
        static Node[] segments;
        static int size;
        static long MIN = Long.MIN_VALUE / 80_000L;
        static Node DEFAULT = new Node(MIN, MIN, MIN, 0, MIN, 50000000);

        public static void main(String[] args) throws Exception {
            System.setIn(new FileInputStream("54.in"));
            N = read();
            Q = read();
            size = 1;

            while(size < N) size <<= 1;

            segments = new Node[(size << 1) + 1];


            for(int i = size + 1; i < size + N + 1; i++) {
                int a = read();
                segments[i] = new Node(a, a, a, a, a, i - size);
            }

            for(int i = size + N + 1; i < segments.length; i++) segments[i] = DEFAULT;

            int segmentSize = segments.length - 1;

            while(segmentSize > 2) {
                segments[segmentSize >> 1] = combine(segments[segmentSize - 1], segments[segmentSize]);
                segmentSize -= 2;
            }

            StringBuilder sb = new StringBuilder();
            while(Q-->0) {
                int a = read();
                int b = read();
                int c = read();

    //            for(int i = 2; i < segments.length; i++) {
    //                System.out.print(segments[i].max + " ");
    //            }
    //            System.out.println();
                if(a == 1) {
                    update(b, -c);
                } else if(a == 2) {
                    update(b, c);
                } else {
                    long d = query(b, c, 2, 1, size).max;
                    sb.append(d < 0 ? 0 : d).append('\n');
                }
            }
            System.out.write(sb.toString().getBytes());

        }

        public static void update(int index, long val) {
            if(index > N) return;
            index += size;
            if(segments[index].largeIdx > 500000) return;
            long a = (segments[index].max < 0 ? 0 : segments[index].max) + val;

           if(a < 0) {
               segments[index] = new Node(MIN,MIN,MIN,MIN,MIN, index - size);
               int before = index;
               index = (index + 1) >> 1;
               while(index >= 2) {
                   segments[index] = combine(segments[(index << 1) - 1], segments[index << 1]);
                   index = (index + 1) >> 1;
               }
               update(queryLarge(before - size + 1, N, 2, 1,  size).largeIdx, a);
           } else {
               if(a == 0) a = MIN;
               segments[index] = new Node(a, a, a, a, a, index - size);
               index = (index + 1) >> 1;
               while(index >= 2) {
                   segments[index] = combine(segments[(index << 1) - 1], segments[index << 1]);
                   index = (index + 1) >> 1;
               }
           }
        }

        public static Node queryLarge(int left, int right, int node, int start, int end) {
            if(left > end || right < start) return DEFAULT;

            if(left <= start && end <= right) {
                return segments[node];
            }

            int mid = (start + end) >> 1;
            Node ln = queryLarge(left, right, (node << 1) - 1, start, mid);
            Node rn = queryLarge(left, right, node << 1, mid + 1, end);

            if(ln.large >= rn.large) {
                return ln;
            } else {
                return rn;
            }
        }

        public static Node query(int left, int right, int node, int start, int end) {
            if(left > end || right < start) return DEFAULT;

            if(left <= start && end <= right) {
                return segments[node];
            }

            int mid = (start + end) >> 1;
            return combine(query(left, right, (node << 1) - 1, start, mid), query(left, right, node << 1, mid + 1, end));
        }


        public static Node combine(Node ln, Node rn) {

            return new Node(
                    Math.max(ln.lmax, ln.sum + rn.lmax),
                    Math.max(rn.rmax, rn.sum + ln.rmax),
                    Math.max(ln.rmax + rn.lmax, Math.max(ln.max, rn.max)),
                    ln.sum + rn.sum,
                    Math.max(ln.large, rn.large),
                    ln.large >= rn.large ? ln.largeIdx : rn.largeIdx
            );
        }

        static class Node {
            long lmax;
            long rmax;
            long max;
            long sum;
            long large;
            int largeIdx;

            public Node(long lmax, long rmax, long max, long sum, long large, int largeIdx) {
                this.lmax = lmax;
                this.rmax = rmax;
                this.max = max;
                this.sum = sum;
                this.large = large;
                this.largeIdx = largeIdx;
            }
        }

        private static int read() throws Exception {
            int d, o;
            d = System.in.read();


            o = d & 15;
            while ((d = System.in.read()) > 32)
                o = (o << 3) + (o << 1) + (d & 15);

            return o;
        }

    }
```
