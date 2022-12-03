import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class day3 {
    public static void main(String[] args) throws FileNotFoundException {
        // part1
        File myObj = new File("src/input3.txt");
        Scanner myReader = new Scanner(myObj);
        int total = 0;
        while (myReader.hasNextLine()) {
            String data = myReader.nextLine();
            String list1 = data.substring(0, data.length() / 2);
            String list2 = data.substring((data.length() / 2), data.length());
            for (int i = 0; i < list1.length(); i++) {
                if (list2.contains(list1.substring(i, i + 1))) {
                    if (Character.isUpperCase(list1.charAt(i))) {
                        total += data.charAt(i) - 38;
                    } else {
                        total += data.charAt(i) - 96;
                    }
                    break;
                }
            }
        }
        System.out.println(total);
        // part2
        File myObj2 = new File("src/input3.txt");
        Scanner myReader2 = new Scanner(myObj2);
        total = 0;
        while (myReader2.hasNextLine()) {
            String data1 = myReader2.nextLine();
            String data2 = myReader2.nextLine();
            String data3 = myReader2.nextLine();
            for (int i = 0; i < data1.length(); i++) {
                if (data2.contains(data1.substring(i, i + 1)) && data3.contains(data1.substring(i, i + 1))) {
                    if (Character.isUpperCase(data1.charAt(i))) {
                        total += data1.charAt(i) - 38;
                    } else {
                        total += data1.charAt(i) - 96;
                    }
                    break;
                }
            }
        }
        System.out.println(total);
    }
}
