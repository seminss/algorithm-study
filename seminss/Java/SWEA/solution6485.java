package SWEA.D3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

import static java.lang.Integer.parseInt;

public class solution6485 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        int T = parseInt(br.readLine());
        for (int tc = 1; tc <= T; tc++) {
            sb.append("#").append(tc).append(" ");
            int N = parseInt(br.readLine());
            Pair[] pairs = new Pair[N];
            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                pairs[i] = new Pair(parseInt(st.nextToken()), parseInt(st.nextToken()));
            }
            int P = parseInt(br.readLine());
            for (int i = 1; i <= P; i++) {
                int busNum = parseInt(br.readLine());
                int cnt=0;
                for (Pair p : pairs) {
                    if (busNum >= p.a && busNum <= p.b) {
                        cnt += 1;
                    }
                }
                sb.append(cnt).append(" ");
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }
}

class Pair {
    int a, b;

    public Pair(int a, int b) {
        this.a = a;
        this.b = b;
    }
}
