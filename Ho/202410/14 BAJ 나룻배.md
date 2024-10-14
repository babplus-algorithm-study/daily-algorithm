package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.StringTokenizer;

public class P2065 {
static int M, T, N;

    static Queue<Node> lQ = new LinkedList<>();
    static Queue<Node> rQ = new LinkedList<>();
    static PriorityQueue<Node> pq = new PriorityQueue<Node>((o1,o2) -> {
        return o1.time - o2.time;
    });
    static int[] exitArr;

    static int elaspedTime = 0;
    static ArrayList<Node> ships = new ArrayList<>();
    static int exitCount = 0;
    static char curSide = 'l';

    static class Node {
        int time;
        char side;
        int index;

        Node(int t, char s,int i) {
            time = t;
            side = s;
            index = i;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        M = Integer.parseInt(st.nextToken());
        T = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());

        // M명이 나룻배를 탈 수 있는 최대
        // T는 편도 시간
        // N이 사람 수

        // 없을 때만 기다린다.
        // 사람이 도착하면 대기 큐에 넣는다.

        for(int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());

            int time = Integer.parseInt(st.nextToken());
            char side = st.nextToken().charAt(0);
            pq.offer(new Node(time, side,i));
        }

        int arrTime = 0;
        boolean isWait = true;
        exitArr = new int[N];
        // 시간이 되면 대기열에 넣고 싶다.
        // 그리고 나룻배에 태울때 타는 시간을 적는다.
        while(exitCount < N) {
            // 사람이 도착하면 대기열에 넣기
            while(!pq.isEmpty() && pq.peek().time == elaspedTime) {
                if(pq.peek().side == 'l') {
                    lQ.add(pq.poll());
                }
                else{
                    rQ.add(pq.poll());
                }
            }

            // 정박장에 도착한 경우 정박장에 사람들 태우기
            // 반대편으로 도착하는 경우를 어떻게 관리할까?
            if(elaspedTime == arrTime || isWait) {
                //내려줄 사람이 있다면 내려준다.
                while(!ships.isEmpty()) {
                    exitArr[ships.get(ships.size()-1).index] = elaspedTime;
                    ships.remove(ships.size() - 1);
                    exitCount++;
                }

                //현재 태울 사람이 있으면 태운다.
                if(curSide == 'l') {
                    if(lQ.size() == 0) {
                        isWait = true;
                        // 태울 사람이 없는 경우 반대편을 본다.
                        if(rQ.size() > 0) {
                            //태울 사람 있으면 출발
                            isWait = false;
                            arrTime = elaspedTime + T;
                            curSide = 'r';
                        }
                    }
                    else{
                        // 태울 사람이 있는 경우
                        while(ships.size() < M && lQ.size() > 0) {
                            ships.add(lQ.poll());
                            arrTime = elaspedTime + T;
                            isWait = false;
                        }
                        curSide = 'r';
                    }


                }
                else {
                    if(rQ.size() == 0) {
                        isWait = true;

                        if(lQ.size() > 0) {
                            isWait = false;
                            arrTime = elaspedTime + T;
                            curSide = 'l';
                        }
                    }
                    else{
                        while(ships.size() < M && rQ.size() > 0) {
                            ships.add(rQ.poll());
                            arrTime = elaspedTime + T;
                            isWait = false;
                        }
                        curSide = 'l';
                    }
                }
            }
            elaspedTime++;
        }

        for(int i = 0; i < N; i++) {
            System.out.println(exitArr[i]);
        }
    }

}
