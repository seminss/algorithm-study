package 자료구조;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class boj18115 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());

        int[] skills = new int[n];
        st =new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            skills[i] = Integer.parseInt(st.nextToken()); //1:젤 위, 2:두번째, 3:젤밑
        }

        Deque<Integer> dq = new ArrayDeque<>();
        int idx = n - 1; //skill에 접근하는 순서
        for (int num = 1; num <= n; num++) {
            if (dq.isEmpty()) {
                dq.add(num);
                idx--;
                continue;
            }
            switch(skills[idx]){
                case 1:
                    dq.addFirst(num);
                    break;
                case 2:
                    int temp = dq.pollFirst();
                    dq.addFirst(num);
                    dq.addFirst(temp);
                    break;
                case 3:
                    dq.addLast(num);
                    break;
            }
            idx--;
        }
        for(int num:dq){
            sb.append(num).append(" ");
        }
        System.out.println(sb);
    }
}
