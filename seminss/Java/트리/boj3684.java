package 트리;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

//bottom up 방식 사용, swea/problem1248와 유사한데 그 문제도 이 방식으로 풀면 더 좋을듯
public class boj3684 {
    private static int N;
    private static int[] parents;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        int T = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= T; tc++) {
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken()); //정점 개수
            parents = new int[N + 1];

            for (int i = 1; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                int parent = Integer.parseInt(st.nextToken());
                int child = Integer.parseInt(st.nextToken());
                addNode(parent, child);
            }

            st = new StringTokenizer(br.readLine());
            int A = Integer.parseInt(st.nextToken()); //정점1
            int B = Integer.parseInt(st.nextToken()); //정점2
            int commonParent = findCommonParent(A, B);

            sb.append(commonParent).append("\n");
        }
        System.out.print(sb);
    }

    private static void addNode(int parent, int child) {
        parents[child] = parent;
    }

    private static int findCommonParent(int a, int b) {
        boolean[] visited = new boolean[N + 1];
        visited[a] = true;
        while (hasParent(a)) {
            a = parents[a];
            visited[a] = true; //a의 조상을 모두 표시해둠
        }
        while (!visited[b]) { //visited[b]가 true -> a의 조상인 것.
            b = parents[b]; //a의 조상과 b의 조상이 만날 때까지 위로 올라가기
        }
        return b;
    }

    private static boolean hasParent(int a) {
        return parents[a] != 0;
    }
}