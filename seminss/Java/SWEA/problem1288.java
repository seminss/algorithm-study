package SWEA.D2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;

//3:50~4:18
public class problem1288 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= T; tc++) {
            sb.append("#").append(tc).append(" ");
            Set<Integer> numbers = new HashSet<>();
            int n = Integer.parseInt(br.readLine());
            int cnt = 1;
            while (numbers.size() < 10) {
                int temp = n * cnt;
                while (temp != 0) {
                    numbers.add(temp % 10);
                    temp /= 10;
                }
                cnt++;
            }
            sb.append(n*(cnt-1)).append("\n");
        }
        System.out.println(sb);
    }
}