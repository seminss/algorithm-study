package 구현;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class boj1212 {
    public static String toBin(String octStr){
        StringBuilder answer= new StringBuilder();
        for(char ch: octStr.toCharArray()){
            int octPart=ch-'0'; //ASCII 를 이용한 [문자 -> 정수] 트릭
            StringBuilder binPart=new StringBuilder();
            for (int i=0;i<3;i++){
                binPart.insert(0,octPart%2); //StringBuilder 의 insert 는 정수도 인자로 받음
                octPart/=2;
            }
            answer.append(binPart);
        }
        return answer.toString().replaceFirst("^0+", ""); //뒤집었을 때 0이 앞에 있는 경우, 0 제거
    }
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String oct= br.readLine();
        if (oct.equals("0")){ //0인 경우는 빈스트링을 출력해서 예외처리 필요
            System.out.println(oct);
            return;
        }
        System.out.println(toBin(oct));
    }
    //입력과 반환 모두 문자열로 처리해야 한다. 문제에서 테스트로 사용하는 값이 int, long 범위를 한참 넘음
}
