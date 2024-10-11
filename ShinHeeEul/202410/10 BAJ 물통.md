```java
import java.util.*;

class Main {

    static SortedSet<Integer> set = new TreeSet<>();
    static HashMap<Node, Boolean> map = new HashMap<>();
    static Queue<Node> queue = new LinkedList<>();

    public static void main(String[] args) throws Exception {
        int A = read();
        int B = read();
        int C = read();

        queue.add(new Node(0,0, C));
        map.put(queue.peek(), true);

        while(!queue.isEmpty()) {
            Node node = queue.poll();
            int a = node.a;
            int b = node.b;
            int c = node.c;

            if(a == 0) set.add(c);

            // a to b
            int min = Math.min(a, B - b);
            Node tmp = new Node(a - min, b + min,c);
            valid(tmp);

            // a to c
            min = Math.min(a, C - c);
            tmp = new Node(a - min, b, c + min);
            valid(tmp);

            // b to a
            min = Math.min(b, A - a);
            tmp = new Node(a + min, b - min, c);
            valid(tmp);

            // b to c
            min = Math.min(b, C - c);
            tmp = new Node(a, b - min, c + min);
            valid(tmp);

            // c to a
            min = Math.min(c, A - a);
            tmp = new Node(a + min, b, c - min);
            valid(tmp);

            // c to b
            min = Math.min(c, B - b);
            tmp = new Node(a, b + min, c - min);
            valid(tmp);


        }


        StringBuilder sb = new StringBuilder();

        for(int a: set) sb.append(a).append(" ");
        System.out.println(sb);
    }

    public static void valid(Node node) {

        if(!map.getOrDefault(node, false)) {
            map.put(node, true);
            queue.add(node);
        }

    }


    public static class Node {
        int a;
        int b;
        int c;

        public Node(int a, int b, int c) {
            this.a = a;
            this.b = b;
            this.c = c;
        }

        @Override
        public int hashCode() {
            return a * 90_000 + b * 300 + c;
        }

        @Override
        public boolean equals(Object obj) {
            Node node = (Node) obj;
            if(this.a == node.a && this.b == node.b && this.c == node.c) return true;
            return false;
        }
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
