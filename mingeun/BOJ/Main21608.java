// 23.10.14 19:50 ~ 21:40
import java.util.*;
import java.io.*;

public class Main21608 {
    private static int n;
    private static int[] input;
    private static int[][] data;
    private static int answer;
    private static int[][] sit;
    private static final int X = 0;
    private static final int Y = 1;
    private static int[] studentOrder;

    public static void main(String[] args) throws IOException {
        // input
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        data = new int[n * n][];
        studentOrder = new int[n * n];
        for (int i = 0; i < n * n; i++) {
            input = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
            data[input[0] - 1] = new int[4];
            studentOrder[i] = input[0] - 1;
            for (int j = 0; j < 4; j++)
                data[input[0] - 1][j] = input[j + 1] - 1;
        }
        // solution
        sit = new int[n][n];
        Arrays.stream(sit).forEach((arr) -> Arrays.fill(arr, -1));
        for (int i = 0; i < n * n; i++) {
            int[] pos = decidePositionOf(studentOrder[i]);
            sit[pos[X]][pos[Y]] = studentOrder[i];
        }
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                answer += satisfactionScoreFor(i, j);

        // print2DMatrix(sit);
        System.out.println(answer);
    }

    private static int[] decidePositionOf(int student) {
        int[][] direction = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
        int maxScore = -1;
        int tmpScore = 0;
        int posCount = 0;
        int[] position = new int[2];
        List<int[]> promisingPos = new ArrayList<>();
        // 1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (sit[i][j] != -1)
                    continue;
                // count: 좋아하는 학생이 있는 인접한 칸 개수
                for (int d = 0; d < 4; d++) {
                    int xn = i + direction[d][X];
                    int yn = j + direction[d][Y];
                    if (xn >= 0 && xn < n && yn >= 0 && yn < n) {
                        for (int k = 0; k < 4; k++) {
                            if (data[student][k] == sit[xn][yn])
                                tmpScore++;
                        }
                    }
                }
                if (tmpScore > maxScore) {
                    position[X] = i; position[Y] = j;
                    maxScore= tmpScore;
                    promisingPos.add(new int[] {i, j, tmpScore});
                } else if (tmpScore == maxScore) {
                    promisingPos.add(new int[] {i, j, tmpScore});
                }
                tmpScore = 0;
            }
        }
        // 2. 1을 만족하는 칸이 여러 개면, 인접한 칸 중 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
        // 3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로,
        // 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.
        int emptyCount = -1;
        for (int p = 0; p < promisingPos.size(); p++) {
            if (promisingPos.get(p)[2] < maxScore)
                continue;
            int i = promisingPos.get(p)[X];
            int j = promisingPos.get(p)[Y];
            if (sit[i][j] != -1)
                continue;
            // tmpScore: 인접한 칸 중 빈 칸 수
            for (int d = 0; d < 4; d++) {
                int xn = i + direction[d][X];
                int yn = j + direction[d][Y];
                if (xn >= 0 && xn < n && yn >= 0 && yn < n && sit[xn][yn] == -1) {
                    tmpScore++;
                }
            }
            if (tmpScore > emptyCount) {
                position[X] = i; position[Y] = j;
                emptyCount = tmpScore;
            }
            tmpScore = 0;
        }
        return position;
    }

    private static int satisfactionScoreFor(int i, int j) {
        int count = 0;
        int[][] direction = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
        for (int d = 0; d < 4; d++) {
            int xn = i + direction[d][X];
            int yn = j + direction[d][Y];
            if (xn >= 0 && xn < n && yn >= 0 && yn < n) {
                for (int k = 0; k < 4; k++) {
                    if (data[sit[i][j]][k] == sit[xn][yn])
                        count++;
                }
            }
        }
        int result = 0;
        switch (count) {
            case 0: result = 0; break;
            case 1: result = 1; break;
            case 2: result = 10; break;
            case 3: result = 100; break;
            case 4: result = 1000; break;
        }
        return result;
    }

    private static void print2DMatrix(int[][] matrix) {
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix.length; j++){
                System.out.print((matrix[i][j] + 1) + " ");
            }
            System.out.println();
        }
    }
}
