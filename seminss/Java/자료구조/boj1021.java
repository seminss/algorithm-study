package 자료구조;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class boj1021 {
    private static int N ;
    private static int M;
    private static int count;
    private static int[] data;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        setInput(br, st);
        Deque<Integer> dq = new ArrayDeque<Integer>();
        for (int i =1; i<=N; i++)
            dq.add(i);
        for (int num : data) {
            if (findIndex(dq,num)<=dq.size()/2){
                while(true){
                    int popNum= dq.pollFirst();
                    if(popNum==num)
                        break;
                    count++;
                    dq.addLast(popNum);
                }
                continue;
            }
            while(true){
                int popNum= dq.pollLast();
                count++; //pop은 무조건 앞에서 빼는거라 뒤부터 빼는 식으로 회전시키면 최종적으로 연산 +1
                if(popNum==num)
                    break;
                dq.addFirst(popNum);
            }
        }
        System.out.println(count);
    }

    private static <T> int findIndex(Deque<T> dq, T value){
        int index = 0;
        for (T item: dq){
            if (item.equals(value))
                return index;
            index++;
        }
        return -1;
    }

    private static void setInput(BufferedReader br, StringTokenizer st) throws IOException {
        N =Integer.parseInt(st.nextToken()); //큐의 크기
        M = Integer.parseInt(st.nextToken()); //뽑아내려고 하는 수
        data = new int[M];
        st = new StringTokenizer(br.readLine());
        for (int j=0;j<M;j++)
            data[j]=Integer.parseInt(st.nextToken());
    }
}
