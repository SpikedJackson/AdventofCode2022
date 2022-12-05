import java.util.Scanner;
import java.io.FileNotFoundException;
import java.io.File;
import java.util.ArrayList;

public class day4 {
    public static void main(String[] args) throws FileNotFoundException {
        File file = new File("src/input4.txt");
        Scanner scanner = new Scanner(file);
        int total = 0;
        int total2 = 0;
        while (scanner.hasNextLine()) {
            String data = scanner.nextLine();
            int step = 0;
            ArrayList<Integer> list = new ArrayList<Integer>();
            for (int i = 0; i <= data.length(); i++) {
                if (i == data.length()) {
                    list.add(Integer.parseInt(data.substring(step, i)));
                    break;
                }
                if (data.charAt(i) == '-') {
                    list.add(Integer.parseInt(data.substring(step, i)));
                    step = i + 1;
                }
                if (data.charAt(i) == ',') {
                    list.add(Integer.parseInt(data.substring(step, i)));
                    step = i + 1;
                }
            }
            // part 1
            if ((list.get(0) >= list.get(2) && list.get(1) <= list.get(3))
                    || (list.get(0) <= list.get(2) && list.get(1) >= list.get(3))) {
                total++;
            }
            // part 2
            if ((list.get(0) > list.get(2) && list.get(1) > list.get(2) && list.get(0) > list.get(3)
                    && list.get(1) > list.get(3))
                    || (list.get(0) < list.get(2) && list.get(1) < list.get(2) && list.get(0) < list.get(3)
                            && list.get(1) < list.get(3))) {
            } else {
                total2++;
                System.out.println(list);
                System.out.println(total2);
            }
        }
        // System.out.println(total);
        System.out.println(total2);
    }
}
