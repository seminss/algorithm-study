package 브루트포스;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

//10:30~11:00
public class boj20529 {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(br.readLine());
        for (int testCase = 0; testCase < T; testCase++) {
            solution();
        }
    }

    private static void solution() throws IOException {
        StringTokenizer st;
        int N = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        if (N > 32) {
            System.out.println(0);
            return;
        }
        List<String> list = new ArrayList<>();
        while (st.hasMoreTokens()) {
            list.add(st.nextToken());
        }
        int result = 12;
        for (int i = 0; i < N; i++) {
            for (int j = i + 1; j < N; j++) {
                for (int k = j + 1; k < N; k++) {
                    result = Math.min(
                            result, calculateDistance(list.get(i), list.get(j), list.get(k))
                    );
                }
            }
        }
        System.out.println(result);
    }

    private static int calculateDistance(String a, String b, String c) {
        int cnt = 0;
        for (int i = 0; i < 4; i++) {
            if (a.charAt(i) != b.charAt(i)) {
                cnt++;
            }
            if (b.charAt(i) != c.charAt(i)) {
                cnt++;
            }
            if (a.charAt(i) != c.charAt(i)) {
                cnt++;
            }
        }
        return cnt;
    }

}
