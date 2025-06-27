```java
public class Main {

    static int[] segments;
    static int size = 1 << 16;
    static long answer = 0;
    static int[] arr;
    public static void main(String[] args) throws Exception {

        int N = read();
        int K = read();
        segments = new int[(size << 1) + 1];
        arr = new int[N];

        for(int i = 0; i < N; i++) arr[i] = read();

        // segments[1]에는 합이 저장되어 있다.
        // 절반을 찾아야 한다.
        // 8
        // 6 2

        for(int i = 0; i < K; i++) update(arr[i], 1);
        find(1, (segments[1] + 1) / 2);
        for(int i = K; i < N; i++) {
            update(arr[i - K], -1);
            update(arr[i], 1);
            find(1, (segments[1] + 1) / 2);
        }

        System.out.println(answer);
    }

    public static void update(int a, int val) {
        a += size;

        while(a > 0) {
            segments[a]+=val;
            a /= 2;
        }
    }

    public static void find(int node, int a) {

        if(node >= size) {
            answer += (node - size);
            return;
        }
        if(a == 0 && segments[node * 2] == 0) find(node * 2 + 1, 0);
        // 왼쪽 노드 (* 2)가 a보다 크거나 같다?
            // 왼쪽 노드로 내려가기
        else if(segments[node * 2] >= a) find(node * 2, a);
        // 왼쪽 노드 (*2)가 a보다 작다?
            // 오른쪽 노드로 내려가기
        else find(node * 2 + 1, a - segments[node * 2]);
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
