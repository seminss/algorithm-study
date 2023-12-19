package 브루트포스;

//1:05 ~ 1:37 풀이 참고 ㅜㅜ

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj6064 {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(br.readLine());
        for (int t = 0; t < T; t++) {
            st = new StringTokenizer(br.readLine());
            int M = Integer.parseInt(st.nextToken());
            int N = Integer.parseInt(st.nextToken());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            solution(M, N, x - 1, y - 1);
        }
    }

    private static void solution(int M, int N, int X, int Y) {
        for (int cnt = X; cnt < M * N; cnt += M) {
            if (cnt % N == Y) {
                System.out.println(cnt + 1);
                return;
            }
        }
        System.out.println(-1);
    }
}
