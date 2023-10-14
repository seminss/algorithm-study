import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class boj16922 {
    private static final int[] roma= {1,5,10,50};
    private static final boolean[] check=new boolean[50*20+1];
    private static int total =0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N=Integer.parseInt(br.readLine());
        dfs(0,N,0);

        System.out.println(total);
    }
    private static void dfs(int romaSum, int N,int idx){ //사전 인덱스 사용 -> 중복 조합 탐색 x (시간 초과 방지)
        if(N==0){
            if( !check[romaSum]){
                check[romaSum]=true;
                total +=1;
            }
            return;
        }
        for(int i=idx;i<4;i++){
            dfs(romaSum+roma[i], N-1, i);
        }
    }
}
