package SWEA;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

//9:39~10:01
public class problem1204 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());
        for (int test_case = 1; test_case <= T; test_case++) {
            int t = Integer.parseInt(br.readLine());
            sb.append("#").append(t).append(" ");
            int[] scores = new int[101];
            Arrays.fill(scores, 0);
            st = new StringTokenizer(br.readLine());
            while (st.hasMoreTokens()) {
                int score = Integer.parseInt(st.nextToken());
                scores[score]++;
            }
            int value = 0;
            int key = 1;
            for (int i = 1; i < 101; i++) {
                if (value > scores[i]) {
                    continue;
                }
                key = i;
                value = scores[i];
            }
            sb.append(key).append("\n");
        }
        System.out.println(sb);
    }
}
