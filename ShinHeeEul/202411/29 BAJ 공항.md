```java
public class Main {


    static int[] segments;
    static int size;

    public static void main(String[] args) throws Exception {
        int G = read();
        int P = read();
        size = 1;

        while(size < G) {
            size <<= 1;
        }
        segments = new int[(size << 1) + 1];

        for(int i = size + G + 1; i < segments.length; i++) {
            segments[i] = 1;
        }

        int segmentSize = segments.length - 1;

        while(segmentSize > 1) {
            segments[segmentSize >> 1] = segments[segmentSize] + segments[segmentSize - 1];
            segmentSize -= 2;
        }


        int count = 0;
        for( ; count < P; count++) {
            int val = read();

            int index = query(1, val, 2, 1, size);
            if(index <= 0) break;
            update(index);
        }
        System.out.println( Math.min(count, G));

    }

    public static void update(int val) {
        while(val > 1) {
            segments[val]++;
            val = (val + 1) >> 1;
        }
    }
    public static int query(int left, int right, int node, int start ,int end) {

        if(left > end || right < start) return -1;

        if(node > size) {
            return node;
        }

        int mid = (end + start) >> 1;
        int next = node << 1;
        int a = -1;
        
        if(right > mid && segments[next] < (end - mid + 1)) {
            a = query(left, right, next, mid + 1, end);
        }

        if(a == -1 && segments[next - 1] < (mid - start + 1)) {
            a = query(left, right, next - 1, start, mid);
        }

        return a;
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
