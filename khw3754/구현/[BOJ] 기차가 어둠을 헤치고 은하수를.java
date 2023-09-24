import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;
import java.util.stream.IntStream;
import java.util.stream.Stream;
import java.util.*;

public class Main{
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws Exception {
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        boolean[][] train = new boolean[N][20];

        for(int cc = 0; cc < M; cc++) {
            st = new StringTokenizer(br.readLine());
            int com = Integer.parseInt(st.nextToken());
            int t_num = Integer.parseInt(st.nextToken()) - 1;

            if(com == 1) {
                int seet = Integer.parseInt(st.nextToken()) - 1;
                train[t_num][seet] = true;
            }
            else if(com == 2) {
                int seet = Integer.parseInt(st.nextToken()) - 1;
                train[t_num][seet] = false;
            }
            else if(com == 3) {
                boolean[] new_train = new boolean[20];
                for(int i = 1; i < 20; i++) {
                    new_train[i] = train[t_num][i-1];
                }
                train[t_num] = new_train;
            }
            else if(com == 4) {
                boolean[] new_train = new boolean[20];
                for(int i = 0; i < 19; i++) {
                    new_train[i] = train[t_num][i+1];
                }
                train[t_num] = new_train;
            }
        }

        // 은하수를 건넘
        StringBuilder sb;
        String[] st_train = new String[N];
        for(int i = 0; i < N; i++) {
            sb = new StringBuilder();
            for(int seet = 0; seet < 20; seet++) {
                if(train[i][seet])
                    sb.append('1');
                else
                    sb.append('0');
            }
            st_train[i] = sb.toString();
        }

        int can_count = 0;
        String[] cross = new String[N];
        for(int i = 0; i < N; i++) {
            boolean can = true;
            for(int j = 0; j < can_count; j++) {
                if(cross[j].equals(st_train[i])) {
                    can = false;
                    break;
                }
            }
            if(can) {
                cross[can_count++] = st_train[i];
            }
        }

        System.out.println(can_count);
    }
}