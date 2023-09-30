package 구현;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;
import java.util.stream.IntStream;

public class boj2578 {
    public static void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        /**빙고판 만들기*/
        int[][]bingo = new int[5][5];
        for (int i=0;i<5;i++){
            st = new StringTokenizer(br.readLine());
            for (int j=0;j<5;j++){
                bingo[i][j]= Integer.parseInt(st.nextToken());
            }
        }
        /**사회자 부르는 수*/
        List<Integer> moderator=new ArrayList<>();
        for (int i=0;i<5;i++){
            st=new StringTokenizer(br.readLine());
            while(st.hasMoreTokens())
                moderator.add(Integer.valueOf(st.nextToken()));
        }

        int total=0;
        while (total<=24){
            int thisNum=moderator.get(total);

            fillBingo(bingo, thisNum);
            int bingoCount = getBingoCount(bingo);

            if(bingoCount>=3){
                System.out.println(total+1);
                return;
            }

            total++;
        }
    }

    /**빙고 갯수 세기*/
    private static int getBingoCount(int[][] bingo) {
        int bingoCount = 0;

        // 가로 줄 검사
        for (int i = 0; i < 5; i++) {
            int finalI=i;
            if (IntStream.range(0, 5).allMatch(j -> bingo[finalI][j] == 0)) {
                bingoCount++;
            }
        }

        // 세로 줄 검사
        for (int j = 0; j < 5; j++) {
            int finalJ=j;
            if (IntStream.range(0, 5).allMatch(i -> bingo[i][finalJ] == 0)) {
                bingoCount++;
            }
        }

        // 대각선 검사 (좌상 -> 우하)
        if (IntStream.range(0, 5).allMatch(i -> bingo[i][i] == 0)) {
            bingoCount++;
        }

        // 대각선 검사 (우상 -> 좌하)
        if (IntStream.range(0, 5).allMatch(i -> bingo[i][4 - i] == 0)) {
            bingoCount++;
        }

        return bingoCount;
    }


    private static void fillBingo(int[][] bingo, int thisNum) {
        for (int i=0;i<5;i++){
            for (int j=0;j<5;j++){
                if(bingo[i][j]== thisNum){
                    bingo[i][j]=0;
                    break;
                }
            }
        }
    }
}
