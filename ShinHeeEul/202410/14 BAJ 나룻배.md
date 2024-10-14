```java
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

class Main {

        static int M;
        static int t;
        static int N;
        // 0 : 좌측 , 1 우측
        static int LEFT = 0;
        static int RIGHT = 1;
        static PriorityQueue<Node>[] pq;
        static int status = LEFT;
        static int currentTime = 0;
        public static void main(String[] args) throws Exception {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            StringTokenizer st = new StringTokenizer(br.readLine());
            M = Integer.parseInt(st.nextToken());
            t = Integer.parseInt(st.nextToken());
            N = Integer.parseInt(st.nextToken());

            pq = new PriorityQueue[2];
            pq[LEFT] = new PriorityQueue<>();
            pq[LEFT].add(new Node(-1, Integer.MAX_VALUE));
            pq[RIGHT] = new PriorityQueue<>();
            pq[RIGHT].add(new Node(-1, Integer.MAX_VALUE));
            int[] arrivalTime = new int[N];
            Node[] ship = new Node[M];

            for(int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                int tt = Integer.parseInt(st.nextToken());
                String s = st.nextToken();

                if(s.equals("left")) {
                    pq[0].add(new Node(i, tt));
                } else {
                    pq[1].add(new Node(i, tt));
                }
            }

            while(pq[0].size() > 1 || pq[1].size() > 1) {
                // if 배가 대기 중
                // 아무도 없다?

                // 현재 시간 = 두 queue 중 최상단에의 작은 값 pop
                // if 반대? 현재 시간 + t
                int left = pq[0].peek().val;
                int right = pq[1].peek().val;
                if(left > currentTime && right > currentTime) {
                    currentTime = Math.min(left, right);
                    if(status == LEFT && right < left) {
                        status = RIGHT;
                        currentTime = right + t;
                    } else if(status == RIGHT && right > left) {
                        status = LEFT;
                        currentTime = left + t;
                    }
                }

                // 현재 위치의 현재 시간보다 작은 애들 다 pop
                int a = 0;
                for(; (currentTime >= pq[status].peek().val) && a < M; a++) {
                    ship[a] = pq[status].poll();
                }
                // t만큼 이동
                currentTime += t;
                status = status ^ 1;
                // 내려주면서 값 받기
                a--;
                for(; a >= 0 ; a--) {
                    arrivalTime[ship[a].index] = currentTime;
                }
            }

            StringBuilder sb = new StringBuilder();
            for(int i : arrivalTime) {
                sb.append(i).append("\n");
            }

            System.out.println(sb);

        }

        public static class Node implements Comparable<Node> {
            int index;
            int val;

            public Node(int index, int val) {
                this.index = index;
                this.val = val;
            }

            public int compareTo(Node o) {

                return this.val - o.val;
            }
        }
    }
```
