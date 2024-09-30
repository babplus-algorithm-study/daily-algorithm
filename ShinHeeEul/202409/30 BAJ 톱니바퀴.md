```java

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] ss = new String[5];

        for(int i = 1; i <= 4; i++) ss[i] = br.readLine();

        int K = Integer.parseInt(br.readLine());


        for(int i = 0; i < K; i++) {
            StringTokenizer st=  new StringTokenizer(br.readLine());
            int number = Integer.parseInt(st.nextToken());
            int direction = Integer.parseInt(st.nextToken());
            int startDirection = direction;
            String[] tmps = ss.clone();

            if(number == 1) {
                for(int j = 2; j <= 4; j++) {
                    if(ss[j-1].charAt(2) == ss[j].charAt(6)) {
                        break;
                    }
                    direction = -direction;
                    tmps[j] = turn(ss[j], direction);
                }
            } else if(number == 2) {
                if(ss[1].charAt(2) != ss[2].charAt(6)) {
                    tmps[1] = turn(ss[1], -direction);
                }
                for(int j = 3; j <= 4; j++) {
                    if(ss[j-1].charAt(2) == ss[j].charAt(6)) {
                        break;
                    }
                    direction = -direction;
                    tmps[j] = turn(ss[j], direction);
                }
            } else if(number == 3) {
                if(ss[3].charAt(2) != ss[4].charAt(6)) {
                    tmps[4] = turn(ss[4], -direction);
                }
                for(int j = 3; j > 1; j--) {
                    if(ss[j-1].charAt(2) == ss[j].charAt(6)) {
                        break;
                    }

                    direction = -direction;
                    tmps[j-1] = turn(ss[j-1], direction);
                }
            } else if(number == 4) {
                for(int j = 4; j > 1; j--) {
                    if(ss[j-1].charAt(2) == ss[j].charAt(6)) {
                        break;
                    }

                    direction = -direction;
                    tmps[j-1] = turn(ss[j-1], direction);
                }
            }

            tmps[number] = turn(ss[number], startDirection);
            ss = tmps.clone();
        }
        int count = 0;
        for(int i = 1; i <= 4; i++) {
            count += (int) (Integer.parseInt(ss[i].charAt(0) + "") * Math.pow(2, (i-1)));
        }

        System.out.println(count);
    }

    public static String turn(String s, int direction) {

        StringBuilder sb = new StringBuilder();

        if(direction == 1) {
            sb.append(s, 0, s.length() - 1);
            sb.insert(0, s.charAt(s.length() - 1));
        } else {
            sb.append(s.substring(1)).append(s.charAt(0));
        }

        return sb.toString();
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
