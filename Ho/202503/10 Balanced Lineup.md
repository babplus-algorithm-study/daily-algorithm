```java
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Test {
    static int N, M, H;
    static Node[] segTree;

    public static void main(String[] args) throws Exception {
        BufferedReader br  = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        int h  = (int) Math.ceil(Math.log(N)/Math.log(2));
        int startIdx = (int) Math.pow(2, h);
        H = startIdx;

        segTree = new Node[(int) Math.pow(2, h + 1)];

        for(int i = 0; i < (int) Math.pow(2, h + 1) - startIdx; i++) {



            if(N <= i) {
                segTree[startIdx + i] = new Node(-1,Integer.MAX_VALUE);
                continue;
            }
            int num = Integer.parseInt(br.readLine());
            segTree[startIdx + i] = new Node(num, num);
        }

        // 쿼리 입력받고 해결하기
        StringBuilder sb = new StringBuilder();

        init(1);

        for(int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());

            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            Node t = query(1, 1, startIdx, a, b);

            sb.append(t.max - t.min ).append("\n");
        }

        System.out.println(sb);

    }

    // 가장 큰소랑 가장 작은 소 키 차이 구하기
    public static void init(int idx) {
        if(idx >= H) {
            return;
        }

        init(idx * 2);
        init(idx * 2 + 1);

        int max = Math.max(segTree[idx * 2].max, segTree[idx * 2 + 1].max);
        int min = Math.min(segTree[idx * 2].min, segTree[idx * 2 + 1].min);

        segTree[idx] = new Node(max, min);
    }

    // 가장 큰 소랑 가장 작은 소 키 차이 구하기
    public static Node query(int idx, int s,  int e, int left, int right) {

        //범위 밖인 경우
        if(left > e || right < s) {
            return new Node(Integer.MIN_VALUE, Integer.MAX_VALUE);
        }

        // 선택가능한 경우
        if(left <= s &&  e <= right) {
            return segTree[idx];
        }

        int mid = (s + e) / 2;

        Node n1 = query(idx * 2, s, mid, left, right);
        Node n2 = query(idx * 2 + 1, mid + 1, e, left, right);

        int max = Math.max(n1.max, n2.max);
        int min = Math.min(n1.min, n2.min);

        return new Node(max, min);
    }

    static class Node {
        int max;
        int min;

        Node(int max, int min) {
            this.max = max;
            this.min = min;
        }
    }

}
```