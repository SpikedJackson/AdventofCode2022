import java.util.Scanner;
import java.io.FileNotFoundException;
import java.io.File;

public class day1 {
    public static void main(String[] args) throws FileNotFoundException {
        File file = new File("src/input1.txt");
        Scanner scanner = new Scanner(file);
        int max1 = 0, max2 = 0, max3 = 0;
        int temp = 0;
        int current = 0;
        while (scanner.hasNextLine()) {
            String string = scanner.nextLine();
            try {
                current = Integer.parseInt(string);
                temp += current;
            } catch (NumberFormatException ex) {
                if (temp > max1) {
                    if (temp > max2) {
                        if (temp > max3) {
                            max1 = max2;
                            max2 = max3;
                            max3 = temp;
                        } else {
                            max1 = max2;
                            max2 = temp;
                        }
                    } else {
                        max1 = temp;
                    }
                }
                temp = 0;
            }
        }
        // part1
        System.out.println(max3);
        // part2
        System.out.println(max1 + max2 + max3);
    }
}
