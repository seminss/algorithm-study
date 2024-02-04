package 자료구조;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class boj2493 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int N = Integer.parseInt(br.readLine());
        Stack<Info> tops = new Stack<>();

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 1; i < N + 1; i++) {
            int h = Integer.parseInt(st.nextToken());
            while (!tops.isEmpty()) {
                if (tops.peek().height > h) {
                    sb.append(tops.peek().idx).append(" ");
                    break;
                }
                tops.pop(); //어짜피 현재 h가 뒤에 오는 신호를 먼저 낚아챌거니까, 앞에 있던 탑들은 필요 x
            }
            if (tops.isEmpty()) {
                sb.append("0 "); //현재 h를 수신할 수 있는 탑 x
            }
            tops.push(new Info(h, i));
        }

        System.out.println(sb);
    }

    static class Info {
        int height;
        int idx;

        Info(int height, int idx) {
            this.height = height;
            this.idx = idx;
        }
    }
}
