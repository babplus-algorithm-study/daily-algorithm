```java
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

class Main {


    static int N;
    static int size;
    static Node[] segments;
    static Point[] arr;
    static long D_MIN = Long.MIN_VALUE >> 1;
    static Node DEFAULT = new Node(D_MIN, D_MIN, D_MIN, 0);

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        ArrayList<Point> list = new ArrayList<>();

        for(int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            list.add(new Point (Integer.parseInt(st.nextToken()),Integer.parseInt(st.nextToken()), 1));
        }

        int M = Integer.parseInt(br.readLine());

        for(int i = 0; i < M; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            list.add(new Point (Integer.parseInt(st.nextToken()),Integer.parseInt(st.nextToken()), -1));
        }


        StringTokenizer st = new StringTokenizer(br.readLine());
        int S = Integer.parseInt(st.nextToken());
        int E = Integer.parseInt(st.nextToken());


        arr = list.toArray(new Point[0]);

        for(int i = 0; i < N; i++) arr[i].val *= S;
        for(int i = N; i < N + M; i++) arr[i].val *= E;

        N += M;

        // x좌표가 작은 순으로 정렬
        Arrays.sort(arr, (o1, o2) -> {
            if(o1.x == o2.x) return o1.y - o2.y;
            return o1.x - o2.x;
        });


        int cnt = 1;
        for(int i = 0; i < N; i++) {
            arr[i].index = cnt;
            while(i != N - 1 && arr[i].x == arr[i + 1].x) {
                arr[i + 1].index = cnt;
                i++;
            }
            cnt++;
        }

        size = 1;

        while(size < cnt) size <<= 1;

        Arrays.sort(arr, Comparator.comparingInt(o -> o.y));


        long max = 0;
        for(int i = 0; i < N; i++) {

            // y가 같으면 보지 않아야 됨
            int start = i;
            while(i != N-1 && arr[i].y == arr[i + 1].y) {
                i++;
            }

            segments = new Node[(size << 1) + 1];
            Arrays.fill(segments,DEFAULT);

            for(int j = start; j < N; j++) {
                update(arr[j].index, arr[j].val);
                while(j != N - 1 && arr[j].y == arr[j + 1].y) {
                    update(arr[j + 1].index, arr[j + 1].val);
                    j++;
                }
                // 업데이트 치고 max 찾고
                max = Math.max(max, segments[2].max);
            }

        }

        System.out.println(max);
    }

    static void update(int index, long val) {
        index += size;

        if(segments[index] == DEFAULT) {
            segments[index] = new Node(val, val, val, val);
        } else {
            segments[index].rmax += val;
            segments[index].lmax += val;
            segments[index].max += val;
            segments[index].sum += val;
        }

        index = (index + 1) >> 1;
        while(index >= 2) {
            segments[index] = combine(segments[(index << 1) - 1], segments[index << 1]);
            index = (index + 1) >> 1;
        }
    }

    static Node combine(Node lNode, Node rNode) {
        return new Node(
                Math.max(lNode.lmax, lNode.sum + rNode.lmax),
                Math.max(rNode.rmax, rNode.sum + lNode.rmax),
                Math.max(lNode.rmax + rNode.lmax, Math.max(lNode.max, rNode.max)),
                rNode.sum + lNode.sum
        );
    }

    static class Node {
        long rmax;
        long lmax;
        long max;
        long sum;

        public Node(long lmax, long rmax,long max, long sum) {
            this.rmax = rmax;
            this.lmax = lmax;
            this.max = max;
            this.sum = sum;
        }
    }

    static class Point {
        int x;
        int y;
        int val;
        int index;

        public Point(int x, int y, int val) {
            this.x = x;
            this.y = y;
            this.val = val;
        }
    }

}
```
