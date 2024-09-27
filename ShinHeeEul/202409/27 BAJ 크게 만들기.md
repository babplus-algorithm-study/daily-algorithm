```java
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {


    public static void main(String[] args) throws Exception {
        int N = read();
        int K = read();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        Stack<Character> stack = new Stack<>();
        StringBuilder ans = new StringBuilder();
        for(int i = 0; i < N; i++) {
            char current = s.charAt(i);
            stack.add(current);
            if(i == N-1) break;
            char next = s.charAt(i+1);
            if(K == 0) continue;
            while(stack.peek() < next) {
                stack.pop();
                K--;
                if(stack.isEmpty() || K == 0) break;
            }
        }
        while(K > 0) {
            stack.pop();
            K--;
        }
        while(!stack.isEmpty())
            ans.insert(0, stack.pop());
        System.out.println(ans);
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
