package 수학;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class boj2270 {
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        sb.append((long) Math.pow(2, n) - 1).append("\n");
        hanoi(n, 1, 2, 3);
        System.out.println(sb);
    }

    public static void hanoi(int cnt, int from, int empty, int to) {
        if (cnt == 0) {
            return;
        }
        hanoi(cnt - 1, from, to, empty); //n-1사이즈 탑 -> 임시 위치에 넣어두기
        sb.append(from).append(" ").append(to).append("\n"); //맨 아래에 깔린 n 값 3번 위치에 넣기
        hanoi(cnt - 1, empty, from, to); //임시 위치에 있는 n-1 탑 -> 제대로 3번으로 보내주기
    }
}
