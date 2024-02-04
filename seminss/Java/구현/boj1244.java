package 구현;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj1244 {
    static int n;
    static int[] switches;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        n = Integer.parseInt(br.readLine());
        switches = new int[n + 1];
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i < n + 1; i++) {
            switches[i] = Integer.parseInt(st.nextToken());
        }
        int p = Integer.parseInt(br.readLine());
        for (int i = 0; i < p; i++) {
            st = new StringTokenizer(br.readLine());
            int gender = Integer.parseInt(st.nextToken());
            int core = Integer.parseInt(st.nextToken());
            switch (gender) {
                case (1):
                    male(core);
                    break;
                case (2):
                    female(core);
                    break;
            }
        }
        for (int i = 1; i < n + 1; i++) {
            sb.append(switches[i]).append(" ");
            if (i % 20 == 0) {
                sb.append("\n");
            }
        }
        System.out.println(sb);
    }

    private static void female(int core) {
        switches[core] = switches[core] == 0 ? 1 : 0;
        for (int k = 1; k < n / 2 + 1; k++) {
            if (core + k >= n + 1 || core - k < 1) {
                continue;
            }
            if (switches[core - k] == switches[core + k]) {
                switches[core - k] = switches[core - k] == 0 ? 1 : 0;
                switches[core + k] = switches[core - k];
                continue;
            }
            return;
        }
    }

    private static void male(int core) {
        for (int cnt = 1; cnt * core < n + 1; cnt++) {
            switches[core * cnt] = switches[core * cnt] == 0 ? 1 : 0;
        }
    }
}
