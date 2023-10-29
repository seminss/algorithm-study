// 2023-10-29 09:05 ~ 09:50

import java.util.*;
import java.io.*;

public class Main17276 {

    private static int T;
    private static int n;
    private static int d;
    private static int[][] matrix;
    private static int[] inputs;
    private static StringBuilder answer = new StringBuilder();
    private static BufferedReader br;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++) {
            inputs = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
            n = inputs[0];
            d = inputs[1];
            matrix = new int[n][n];
            readMatrix();
            rotateMatrix();
            appendMatrixToAnswer();
        }
        System.out.println("------------------------");
        System.out.println(answer.toString());
    }

    private static void readMatrix() throws IOException {
        for (int i = 0; i < n; i++) {
            inputs = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
            for (int j = 0; j < n; j++) {
                matrix[i][j] = inputs[j];
            }
        }
    }

    private static void rotateMatrix() {
        if (d == 0)
            return;
        int repetition = d / 45;
        int direction = repetition / Math.abs(repetition);
        repetition = Math.abs(repetition) % 8;
        if (direction < 0)
            repetition = 8 - repetition;
        for (int i = 0; i < repetition; i++) {
            rotate45degree();
        }
    }

    private static void rotate45degree() {
        int[][] tmp = new int[n][n];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                tmp[i][j] = matrix[i][j];
        int m = n / 2;
        // X의 주 대각선을 ((1,1), (2,2), …, (n, n)) 가운데 열 ((n+1)/2 번째 열)로 옮긴다.
        for (int i = 0; i < n; i++)
            tmp[i][m] = matrix[i][i];
        // X의 가운데 열을 X의 부 대각선으로 ((n, 1), (n-1, 2), …, (1, n)) 옮긴다. 
        for (int i = 0; i < n; i++)
            tmp[i][n - 1 - i] = matrix[i][m];
        // X의 부 대각선을 X의 가운데 행 ((n+1)/2번째 행)으로 옮긴다.
        for (int i = 0; i < n; i++)
            tmp[m][n - 1 - i] = matrix[i][n - 1 - i];
        // X의 가운데 행을 X의 주 대각선으로 옮긴다.
        for (int i = 0; i < n; i++)
            tmp[i][i] = matrix[m][i];
        matrix = tmp;
        tmp = null;
    }

    private static void appendMatrixToAnswer() {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                answer.append(matrix[i][j] + " ");
            }
            answer.append("\n");
        }
    }
}
