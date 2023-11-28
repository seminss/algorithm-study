// 11.29 00:24~00:34
import java.util.*;
import java.io.*;
public class Main2563 {
    private static final int X = 0;
    private static final int Y = 1;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[][] paper = new int[100][100];
        for (int k = 0; k < n; k++) {
            int[] input = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
            for (int i = 0; i < 10; i++) {
                for (int j = 0; j < 10; j++) {
                    paper[i + input[X]][j + input[Y]]++;
                }
            }
        }
        int answer = 0;
        for (int i = 0; i < 100; i++) {
            for (int j = 0; j < 100; j++) {
                if (paper[i][j] > 0)
                    answer++;
            }
        }
        System.out.println(answer);
    }

}
