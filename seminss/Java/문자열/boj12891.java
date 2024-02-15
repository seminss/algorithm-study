package 문자열;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj12891 {
    static int[] validCnt = new int[4];
    static int[] curCnt = new int[4];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int res=0;
        int s = Integer.parseInt(st.nextToken()); //문자열 길이
        int p = Integer.parseInt(st.nextToken()); //부분 문자열 길이
        char[] dna = br.readLine().toCharArray();
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < 4; i++) {
            validCnt[i] = Integer.parseInt(st.nextToken());
        }
        int cnt = 0;
        L:
        for (int i = 0; i < s; i++) {
            if (cnt >= p) {

                switch (dna[i - cnt]) {
                    case ('A'):
                        curCnt[0] -= 1;
                        cnt--;
                        break;
                    case ('C'):
                        curCnt[1] -= 1;
                        cnt--;
                        break;
                    case ('G'):
                        curCnt[2] -= 1;
                        cnt--;
                        break;
                    case ('T'):
                        curCnt[3] -= 1;
                        cnt--;
                        break;
                    default:
                        curCnt = new int[4];
                        cnt=0;
                }
            }

            switch (dna[i]) {
                case ('A'):
                    curCnt[0] += 1;
                    cnt++;
                    break;
                case ('C'):
                    curCnt[1] += 1;
                    cnt++;
                    break;
                case ('G'):
                    curCnt[2] += 1;
                    cnt++;
                    break;
                case ('T'):
                    curCnt[3] += 1;
                    cnt++;
                    break;
                default:
                    curCnt = new int[4];
                    cnt = 0;
            }
            for (int j = 0; j < 4; j++) {
                if (curCnt[j] < validCnt[j]) {
                    continue L;
                }
            }
//            System.out.println(cnt+" "+Arrays.toString(curCnt));
            if(cnt==p){
                res++;
            }
        }
        System.out.println(res);
    }
}
