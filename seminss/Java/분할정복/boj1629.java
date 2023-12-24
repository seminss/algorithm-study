package 분할정복;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
//분할 정복 사용, 모듈러 합동 공식 알아야 함.
public class boj1629 {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer st;
    private static int A, B, C;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        A = Integer.parseInt(st.nextToken());
        B = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        System.out.println(power(A, B));
    }

    private static long power(long number, long index) {
        if (index == 1) {
            return number % C;
        }
        long x = power(number, index / 2);
        if (index % 2 == 0) { //지수가 짝수
            return (x * x) % C;
        }
        return (x * x % C) * number % C;
    }
}
