import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class boj18430 {
    private static int[][] trees;
    private static boolean[][] visited;
    static int N; static int M;
    private static int answer=0;
    private static final int[] xChanges={+1,-1,+1,-1};
    private static final int[] yChanges={-1,-1,+1,+1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] argv =br.readLine().split(" ");
        N= Integer.parseInt(argv[0]);
        M= Integer.parseInt(argv[1]);
        if (N<=1||M<=1){
            System.out.println(0);
            return;
        }
        trees=new int[N][M];
        for(int i=0;i<N;i++){
            trees[i]= Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();
        }
        visited = new boolean[N][M];
        back(0,0,0);
        System.out.println(answer);
    }
    private static void back(int x, int y, int thisSum) {

        if (x == M) {  // 현재 열이 M에 도달하면 다음 행의 첫 열로 이동
            x = 0;
            y++;
        }

        if (y == N){
            answer = Math.max(answer, thisSum);
            return; // 모든 그리드를 검사한 경우
        }

        if (!visited[y][x]) {
            for (int k = 0; k < 4; k++) {
                int xChIdx = xChanges[k] + x;
                int yChIdx = yChanges[k] + y;

                if (xChIdx < 0 || xChIdx >= M || yChIdx < 0 || yChIdx >= N)
                    continue;

                if (!visited[yChIdx][x] && !visited[y][xChIdx]) {
                    visited[y][x] = true;
                    visited[yChIdx][x] = true;
                    visited[y][xChIdx] = true;
                    back(x + 1, y, thisSum + 2 * trees[y][x] + trees[yChIdx][x] + trees[y][xChIdx]);
                    visited[y][x] = false;
                    visited[yChIdx][x] = false;
                    visited[y][xChIdx] = false;
                }
            }
        }
        back(x + 1, y, thisSum);  // 현재 위치에서 부메랑을 선택하지 않은 경우
    }
}


/*
  나는 x,y를 모두 넘겼는데 하나의 index로 넘겨서 +1씩 시키고 들어가서 %N, %M으로 x,y를 계산하는 방법도 있음
    >> 이 경우에는 x, y 따로 계산할 필요 없이 x==M, y==N되면 return 가능
  현재 위치에서 부메랑을 선택하지 않은 경우도 모든 경우를 꼭 넣어줘야 함
  */