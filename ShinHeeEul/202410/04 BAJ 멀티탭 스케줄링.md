```java
import java.util.Comparator;
import java.util.PriorityQueue;

class Main {

    public static void main(String[] args) throws Exception {
        int n = read();
        int k = read();
        int[] arr = new int[k];
        PriorityQueue<Integer>[] pq = new PriorityQueue[k + 1];
        for(int i = 1; i <= k; i++) {
            pq[i] = new PriorityQueue<>();
            pq[i].add(100_000);
        }

        for(int i = 0; i < k; i++) {
            int a = read();
            pq[a].add(i);
            arr[i] = a;
        }

        int[] ans = new int[n];

        int count = 0;
        for(int i = 0; i < k; i++) {
            int a = arr[i];

            int max = -1;
            int maxIndex = 0;

            boolean b = true;
            for(int j = 0; j < n; j++) {
                int ind = ans[j];
                if(ind == a || ind == 0) {
                    ans[j] = a;
                    b = false;
                    break;
                } else {
                    while(pq[ind].peek() < i) {
                        pq[ind].poll();
                    }

                    int peek = pq[ind].peek();
                    if(max <= peek) {
                        max = peek;
                        maxIndex = j;
                    }
                }
            }
            if(b) {
                ans[maxIndex] = a;
                count++;
            }

        }

        System.out.println(count);



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
    
