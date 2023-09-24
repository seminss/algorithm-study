package 구현;

import java.io.*;

public class boj1913 {
    public static int[][] makeSnail(int N){
        int[][] snail = new int[N][N];
        int num=N*N;

        for (int i=0;i<N/2;i++){ // 0 1 2 3
            for (int j=i;j<N-i-1;j++){
                snail[j][i]=num;
                num-=1;
            }
            for (int j=i;j<N-i-1;j++){
                snail[N-i-1][j]=num;
                num-=1;
            }
            for (int j=N-1-i;j>i;j--){
                snail[j][N-i-1]=num;
                num-=1;
            }
            for (int j=N-1-i;j>i;j--){
                snail[i][j]=num;
                num-=1;
            }
        }

        snail[N/2][N/2]=1;

        return snail;
    }
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N= Integer.parseInt(br.readLine());
        int target= Integer.parseInt(br.readLine());
        int[][] snail = makeSnail(N);

        int x=0;
        int y=0;

        StringBuilder sb = new StringBuilder();
        for (int i=0;i<N;i++){
            for (int j=0;j<N;j++){
                sb.append(snail[i][j] + " ");
                if (snail[i][j]==target){
                    y=i+1; x=j+1;
                }
            }
            sb.append("\n");
        }
        sb.append(y+" "+x);
        System.out.print(sb.toString());
    }
}
