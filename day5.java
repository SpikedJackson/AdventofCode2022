import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.*;

public class day5 {
    public static void main(String[] args) throws FileNotFoundException {

        // access file
        File file = new File("src/input5.txt");
        Scanner scanner = new Scanner(file);

        // create list for each part of input
        ArrayList<String> list = new ArrayList<String>();
        ArrayList<String> list2 = new ArrayList<String>();
        Boolean check = false;
        while (scanner.hasNextLine()) {
            String next = scanner.nextLine();
            if (next.isEmpty()) {
                check = true;
            } else if (check) {
                list2.add(next);
            } else {
                list.add(next);
            }
        }
        scanner.close();

        // create dictionary to store stacks
        Hashtable<Character, Stack<String>> hash = new Hashtable<Character, Stack<String>>();
        for (int i = 0; i < list.get(list.size() - 1).length(); i++) {
            Character k = list.get(list.size() - 1).charAt(i);
            if (k != ' ') {
                hash.put(k, new Stack<String>());
            }
        }
        list.remove(list.size() - 1);
        for (int i = list.size() - 1; i >= 0; i--) {
            for (int j = 0; j < hash.size(); j++) {
                String k = list.get(i).substring(3 * j + j, 3 * j + j + 3);
                if (k.trim().length() > 0) {
                    hash.get(Integer.toString(j + 1).charAt(0)).push(k);
                }
            }
        }

        // run instructions
        for (int j = 0; j < list2.size(); j++) {

            // create list of instructions
            String[] arrofStr = list2.get(j).split(" ", 6);

            // for part 2
            ArrayList<String> part2 = new ArrayList<String>();

            for (int i = 0; i < Integer.parseInt(arrofStr[1]); i++) {
                // for part 1
                // String y = hash.get(arrofStr[3].charAt(0)).pop();
                // hash.get(arrofStr[5].charAt(0)).push(y);

                // for part 2
                part2.add(hash.get(arrofStr[3].charAt(0)).pop());
            }

            // for part 2
            Collections.reverse(part2);
            for (int i = 0; i < part2.size(); i++) {
                hash.get(arrofStr[5].charAt(0)).push(part2.get(i));
            }

        }

        // figure out last item of each stack
        ArrayList<String> finalanswer = new ArrayList<String>();
        for (int i = 1; i <= hash.size(); i++) {
            finalanswer.add(hash.get(Integer.toString(i).charAt(0)).pop());
        }
        System.out.println(finalanswer);
    }
}
