// 11.3 15:55 ~ 16:30

import java.util.*;
import java.io.*;

public class Main20207 {

    private static BufferedReader br;
    private static int n;
    private static final int S = 0;
    private static final int E = 1;
    private static int[] input;
    private static int[] calender = new int[366];
    private static int answer;

    public static void main(String[] args) throws IOException{
        readInput();
        calculateCoatingArea();
        System.out.println(answer);
    }

    private static void readInput() throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            input = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
            for (int j = input[S]; j <= input[E]; j++) {
                calender[j] += 1;
            }
        }
        br.close();
    }

    private static void calculateCoatingArea() {
        int date = 1;
        while (date <= 365) {
            int width = 0;
            int height = 0;
            while (date <= 365 && calender[date] > 0) {
                width++;
                height = Math.max(height, calender[date]);
                date++;
            }
            answer += width * height;
            date++;
        }
    }
}
