```java
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.PriorityQueue;

public class Main {


    public static void main(String[] args) throws Exception {
        int N = read();
        int[] cranes = new int[N];
        int max = 0;
        for(int i = 0; i < N; i++) {
            cranes[i] = read();
            max = Math.max(max, cranes[i]);
        }

        Arrays.sort(cranes);

        int M = read();
        ArrayList<Integer> boxes = new ArrayList<>();
        for(int i = 0; i < M; i++) {
            int box = read();
            boxes.add(box);
            if(box > max) {
                System.out.println(-1);
                return;
            }
        }
        boxes.sort(Collections.reverseOrder());

        int count = 0;

        while(!boxes.isEmpty()) {
            int boxIdx = 0, craneIdx = N-1;

            while(craneIdx >= 0) {
                if(boxIdx == boxes.size()) break;

                else if(boxes.get(boxIdx) <= cranes[craneIdx]) {
                    boxes.remove(boxIdx);
                    craneIdx--;
                } else boxIdx++;
            }
            count++;
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
