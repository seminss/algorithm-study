// 23.10.15 15:52 ~ 18:37

import java.util.*;
import java.io.*;

public class Main20164 {

    private static final int MAX = 0;
    private static final int MIN = 1;
    private static int[] answer;
    private static String N;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = br.readLine();
        
        answer = new int[2];
        answer[MIN] = 999999999;
        splitTo3Numbers(N, countOdds(N));
        System.out.println(answer[MIN] + " " + answer[MAX]);
    }

    private static void splitTo3Numbers(String number, int oddCount) {
        int l = number.length();
        if (l == 1) {
            answer[MAX] = Math.max(answer[MAX], oddCount);
            answer[MIN] = Math.min(answer[MIN], oddCount);
        } else if (l == 2) {
            String newNumber = stringFormOfsum(number.substring(0, 1), number.substring(1, 2));
            splitTo3Numbers(newNumber, oddCount + countOdds(newNumber));
        } else {
            List<String[]> result = new ArrayList<>();
            for (int i = 1; i < l - 1; i++) {
                String n1 = number.substring(0, i);
                for (int j = i + 1; j < l; j++) {
                    String n2 = number.substring(i, j);
                    String n3 = number.substring(j, l);
                    // DFS
                    String newNumber = stringFormOfsum(n1, n2, n3);
                    splitTo3Numbers(newNumber, oddCount + countOdds(newNumber));
                }
            }
        }
    }

    private static String stringFormOfsum(String... numbers) {
        int sum = 0;
        for (String n: numbers)
            sum += Integer.parseInt(n);
        return String.valueOf(sum);
    }

    private static int countOdds(String number) {
        int result = 0;
        for (int i = 0; i < number.length(); i++) {
            if (number.charAt(i) % 2 == 1)
                result++;
        }
        return result;
    }
}
