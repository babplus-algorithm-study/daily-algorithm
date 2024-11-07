```java
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Queue;

public class Main {

    public static void main(String[] args) throws Exception {

        long L = read();
        int N = (int) read();
        int K = (int) read();

        Queue<Node> queue = new LinkedList<>();
        HashMap<Long, Boolean> map = new HashMap<>();


        for(int i = 0; i < N; i++) {
            long l = read();
            queue.add(new Node(l, 0));
            map.put(l, true);
        }

        StringBuilder sb = new StringBuilder();

        while(!queue.isEmpty()) {
            Node node = queue.poll();
            int value = node.value;
            sb.append(value).append("\n");
            K--;
            if(K == 0) break;

            long a = node.index - 1;
            long b = node.index + 1;
            if(!map.getOrDefault(a, false) && a >= 0) {
                map.put(a, true);
                queue.add(new Node(a, value + 1));
            }
            if(!map.getOrDefault(b, false) && b <= L) {
                map.put(b, true);
                queue.add(new Node(b, value + 1));
            }
        }

        System.out.println(sb);
    }

    public static class Node {
        long index;
        int value;

        public Node(long index, int value) {
            this.index = index;
            this.value = value;
        }
    }


    private static long read() throws Exception {
        long d, o;
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
