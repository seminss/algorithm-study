package 구현;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class boj21608 {

    private static int[][] maps;
    private static int N;
    private static int[] dx={1,-1,0,0};
    private static int[] dy={0,0,1,-1};

    /**
     * maps을 돌면서 빈 좌석인지 확인,
     * 빈 좌석이면 상하좌우 확인해서 좋아하는 학생이 몇명인지 확인
     * 만약 좋아하는 학생(최대 좋아하는 학생 수를 변수 m)이 더 많다면 i, j, m 갱신
     * 같다면 해당 좌석의 상하좌우를 탐색해서 빈 좌석이 많은지 확인 -> 더 많은 쪽으로 i,j,m 갱신
     * 같다면 행 번호 우선 -> 행 번호가 작은 칸으로 i,j,m 갱신
     * 같다면 열 우선 -> 열 번호가 작은 칸으로 i,j,m 갱신
     * */

    private static void setMaps(int stuNum, List<Integer> stuLikes){
        int preM = -1;
        int preI = 0;
        int preJ = 0;
        for(int i=0;i<N;i++){
            for(int j=0;j<N;j++){
                if(maps[i][j]==0){
                    int m=0;
                    m = numOfLikableStudent(j, i, stuLikes, maps, m);
                    if(m>preM){
                        preI = i; preJ = j; preM = m;
                    } else if (m==preM){
                        int zero=0; int preZero=-1;
                        for(int w=0;w<4;w++){
                            int nx=j+dx[w]; int ny=i+dy[w];
                            int preNx=dx[w]+preJ; int preNy=dy[w]+preI;
                            if (!(nx<0 || nx>=N ||ny<0|| ny>=N))
                                if(maps[ny][nx]==0)
                                    zero++;
                            if (!(preNx<0 || preNx>=N ||preNy<0|| preNy>=N))
                                if(maps[preNy][preNx]==0)
                                    preZero++;
                        }
                        if(zero>preZero){
                            preI = i; preJ = j; preM = m;
                        } else if (zero==preZero) {
                            if(i<preI){
                                preI = i; preJ = j; preM = m;
                            }else if(i==preI){
                                if(j<preJ){
                                    preI = i; preJ = j; preM = m;
                                }
                            }
                        }
                    }
                }
            }
        }
        maps[preI][preJ]=stuNum;
    }

    private static int numOfLikableStudent(int j, int i, List<Integer> stuLikes, int[][] maps, int m) {
        for (int w = 0; w < 4; w++) {
            int nx = j + dx[w];
            int ny = i + dy[w];
            if (nx < 0 || nx >= N || ny < 0 || ny >= N)
                continue;
            if (stuLikes.contains(maps[ny][nx]))
                m++;
        }
        return m;
    }

    private static int getTotalLikability(int[][] maps, List<Integer>[] likes) {
        int totalLikeability=0;

        for (int i=0;i<N;i++) {
            for (int j = 0; j < N; j++) {
                int stuNum = maps[i][j];
                int thisLikeability=0;
                thisLikeability = numOfLikableStudent(j, i, likes[stuNum], maps, thisLikeability);
                if(thisLikeability==1)
                    totalLikeability+=1;
                else if(thisLikeability==2)
                    totalLikeability+=10;
                else if(thisLikeability==3)
                    totalLikeability+=100;
                else if(thisLikeability==4)
                    totalLikeability+=1000;
            }
        }
        return totalLikeability;
    }

    private static void setInputs(BufferedReader br, int[] orders, List<Integer>[] likes) throws IOException {
        StringTokenizer st;
        for(int i=1;i<=N*N;i++){
            st=new StringTokenizer(br.readLine());
            int stuNum=Integer.parseInt(st.nextToken());
            orders[i-1]=stuNum;
            for(int j=0;j<4;j++){
                likes[stuNum].add(Integer.parseInt(st.nextToken()));
            }
        }
    }

    private static void printMaps() {
        for(int r=0;r<N;r++){
            for(int c=0;c<N;c++){
                System.out.print(maps[r][c]);
            }
            System.out.println();
        }
        System.out.println("-------------");
    }

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        maps = new int[N][N];
        int[] orders=new int[N*N];
        List<Integer>[] likes = new ArrayList[N*N+1];

        for(int i=0;i<=N*N;i++) {
            likes[i] = new ArrayList<>();
        }
        for(int i=0;i<N;i++){
            for(int j=0;j<N;j++){
                maps[i][j]=0;
            }
        }
        setInputs(br, orders, likes);
        for(int o : orders){
            setMaps(o,likes[o]);
            //printMaps();
        }

        int answer=getTotalLikability(maps,likes);
        System.out.print(answer);
    }
}
