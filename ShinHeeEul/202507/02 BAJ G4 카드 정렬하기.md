```java
import java.util.Arrays;
import java.util.PriorityQueue;

public class Main
{

    public static void main(String[] args) throws Exception {
        int N = read();
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for(int i = 0; i < N; i++) pq.add(read());

        if(N == 1) {
            System.out.println(0);
            return;
        }
        int sum = 0;
        while(pq.size() > 1) {
            int a = pq.poll();
            int b = pq.poll();
            sum += (a + b);
            pq.add(a + b);
        }
        System.out.println(sum);
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
