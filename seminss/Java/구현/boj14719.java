package 구현;
//11:45~12:20
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj14719 {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer wh = new StringTokenizer(br.readLine());
        int[][] word = new int[Integer.parseInt(wh.nextToken())][Integer.parseInt(wh.nextToken())];
        StringTokenizer wall = new StringTokenizer(br.readLine());
        for (int i = 0; i < word[0].length; i++) {
            int height = Integer.parseInt(wall.nextToken());
            for (int j = word.length - 1; j >= word.length - height; j--) {
                word[j][i] = 1;
            }
        }

        System.out.print(measureRain(word));
    }

    private static int measureRain(int[][] word) {
        int answer = 0;
        for (int[] w : word) {
            int oneLineCnt = 0;
            boolean meat = false;
            for (int p : w) {
                if (!meat && p == 1) {
                    meat = true;
                } else if (meat && p == 0) {
                    oneLineCnt++;
                } else if (meat && p == 1 && oneLineCnt > 0) {
                    answer += oneLineCnt;
                    oneLineCnt = 0;
                }
            }
        }
        return answer;
    }
}
