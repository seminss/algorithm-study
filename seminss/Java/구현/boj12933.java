package 구현;

import java.io.*;

public class boj12933 {
    private static final char[] Q = {'q', 'u', 'a', 'c', 'k'};
    public static void main(String args[]) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char[] list=br.readLine().toCharArray();

        if (list.length%5!=0){
            System.out.println(-1);
            return;
        }

        int preSize=list.length;
        int cnt=0;
        while (preSize!=0){
            int duckIdx=0;
            int loopIdx=0;
            boolean made=false;
            int[] duck=new int[5];
            while(loopIdx<list.length){
                if (list[loopIdx]==Q[duckIdx]){
                    duck[duckIdx++]=loopIdx;
                    if(duckIdx==5){
                        made=true;
                        preSize-=5;
                        duckIdx=0;
                        for (int i=0;i<5;i++)
                            list[duck[i]]='\0'; //값이 없음을 나타냄
                    }
                }
                loopIdx++;
            }
            if (made) cnt++;
            else break;
        }
        System.out.println(preSize==0?cnt:-1);
    }
}