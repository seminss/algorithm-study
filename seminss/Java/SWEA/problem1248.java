package SWEA;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class problem1248 {
    private static int V, E, A, B, commonParent, subSize;
    private static ArrayList<Integer>[] graph;
    private static int[] dp;
    private static List<Integer> ACourse, BCourse;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        int T = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= T; tc++) {
            sb.append("#").append(tc).append(" ");
            st = new StringTokenizer(br.readLine());
            V = Integer.parseInt(st.nextToken()); //정점 개수
            E = Integer.parseInt(st.nextToken()); //간선 개수
            A = Integer.parseInt(st.nextToken()); //정점1
            B = Integer.parseInt(st.nextToken()); //정점2

            dp = new int[V + 1];
            graph = new ArrayList[V + 1];
            for (int i = 1; i <= V; i++) {
                graph[i] = new ArrayList<>();
            }

            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < E; i++) {
                int parents = Integer.parseInt(st.nextToken());
                int child = Integer.parseInt(st.nextToken());
                graph[parents].add(child);
            }
            dfsForCommonParent(1, new ArrayList<>(Arrays.asList(1)));
            for (int i = 0; i < Math.min(ACourse.size(), BCourse.size()); i++) {
                if (!ACourse.get(i).equals(BCourse.get(i))) {
                    commonParent = ACourse.get(i - 1); //공통 조상
                    break;
                }
            }

            subSize = 1;
            dfsForSubSize(commonParent);
            sb.append(commonParent).append(" ").append(subSize).append("\n");
        }
        System.out.println(sb);
    }

    private static void dfsForSubSize(int node) {
        for (int e : graph[node]) {
            dfsForSubSize(e);
            subSize++;
        }
    }

    private static void dfsForCommonParent(int node, List<Integer> course) {
        if (node == A) {
            ACourse = course;
            return;
        }
        if (node == B) {
            BCourse = course;
            return;
        }
        for (int e : graph[node]) {
            course.add(e);
            dfsForCommonParent(e, new ArrayList<>(course));
            course.remove(course.size() - 1);
        }
    }
}