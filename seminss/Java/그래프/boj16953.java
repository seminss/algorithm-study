package 그래프.dfs;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
//1:35~2:03
//1억이 들어 왔을 때 1을 더하는 연산을 하면 11억 -> int 범위 벗어남 -> long으로 관리해야 함
public class boj16953 {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer st;
    private static long A, B;
    private static int MAX_NUM = 100_000_000;
    private static long result = MAX_NUM;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        A = Long.parseLong(st.nextToken());
        B = Long.parseLong(st.nextToken());
        dfs(A, 0);
        System.out.println(result == MAX_NUM ? -1 : result + 1);
    }

    private static void dfs(long start, long cnt) {
        if (start == B) {
            result = Math.min(result, cnt);
        }
        if (start > B) {
            return;
        }
        dfs(multipleTwo(start), cnt + 1);
        dfs(addOneForLastDigit(start), cnt + 1);
    }

    private static long multipleTwo(long before) {
        return before * 2;
    }

    private static long addOneForLastDigit(long before) {
        return before * 10 + 1;
    }
}
