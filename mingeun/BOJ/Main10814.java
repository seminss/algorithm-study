// 12.2 22:20~22:25

import java.io.*;
import java.util.*;

public class Main10814 {

    private static class Member {
        public int age;
        public String name;
        public int id;
        public Member(int age, String name, int id) {
            this.age = age;
            this.name = name;
            this.id = id;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String inputs[];
        List<Member> members = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            inputs = br.readLine().split(" ");
            members.add(new Member(Integer.parseInt(inputs[0]), inputs[1], i));
        }
        members.sort((m1, m2) -> {
            if (m1.age == m2.age) {
                return m1.id - m2.id;
            }
            return m1.age - m2.age;
        });
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            sb.append(members.get(i).age + " " + members.get(i).name + "\n");
        }
        System.out.println(sb.toString());
    }
}
