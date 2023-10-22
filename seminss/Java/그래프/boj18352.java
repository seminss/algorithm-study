package 그래프;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class boj18352 {
    static int N;     static int M;
    static int K;     static int X;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N=Integer.parseInt(st.nextToken()); //도시의 개수
        M=Integer.parseInt(st.nextToken()); //도로의 개수
        K=Integer.parseInt(st.nextToken()); //거리 정보
        X=Integer.parseInt(st.nextToken()); //출발 도시 번호

        List<Integer>[] graph = new List[N+1];
        for (int i=0;i<graph.length;i++)
            graph[i]=new ArrayList<>();

        for(int i=0;i<M;i++){
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int goal = Integer.parseInt(st.nextToken());
            graph[start].add(goal);
        }

        int[] depth = new int[N+1];
        Arrays.fill(depth,-1);

        System.out.print(bfs(X,graph,depth));
    }

    static String bfs(int start, List<Integer>[] graph, int[] depth){
        Queue<Integer> dq = new ArrayDeque<>();
        List<Integer> answer= new ArrayList<>();
        dq.add(start);
        depth[start]=0;

        while(!dq.isEmpty()){
            int cur = dq.poll();
            if(depth[cur]>K)
                break;
            if(depth[cur]==K)
                answer.add(cur);
            for (int next : graph[cur]) {
                if(depth[next]!=-1)
                    continue;
                depth[next]=depth[cur]+1;
                dq.add(next);
            }
        }
        Collections.sort(answer);
        StringBuilder sb = new StringBuilder();
        for(int cur : answer){
            sb.append(cur).append("\n");
        }
        return sb.length()==0 ? "-1" : sb.toString(); //java11에서는 sb의 isEmpty 제공 x
    }
}
