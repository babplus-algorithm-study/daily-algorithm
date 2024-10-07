```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static int M;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());

        ArrayList<Integer> cmd = new ArrayList<>();
        Queue<Integer> q = new LinkedList<>();

        for(int i = 0; i < M; i++) {
            cmd.add(Integer.parseInt(st.nextToken()));
        }

        Set<Integer> set = new HashSet<>();

        int cnt = 0;

        for(int i = 0; i < M; i++) {
            int num = cmd.get(i);

            if(set.contains(num)) continue;
            if(set.size() < N && set.add(num)) continue;

            else{
                int max = -1, idx= -1;
                for(int s : set) {
                    int temp = 0;
                    List<Integer> sub = cmd.subList(i + 1, M);
                    if(sub.contains(s)) {
                        temp = sub.indexOf(s) + 1;
                    }
                    else{
                        temp = 200;
                    }
                    if(temp > max) {
                        max = temp;
                        idx = s;
                    }
                }
                set.remove(idx);
                set.add(num);
                cnt++;
                }
            }
        System.out.println(cnt);
        }

    }


```