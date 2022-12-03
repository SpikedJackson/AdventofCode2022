import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class day2 {
    public static void main(String[] args) throws Exception {
        File myObj = new File("src/input2.txt");
        Scanner myReader = new Scanner(myObj);
        int total = 0;
        int total2 = 0;
        while (myReader.hasNextLine()) {
            String data = myReader.nextLine();
            int player = data.charAt(2)-23-64;
            int elf = data.charAt(0)-64;
            total+=player;
            if(elf==player){
                total+=3;
            } else if(player==elf+1 || player==elf-2){
                total+=6;
            }
            //part 2
            if(player==2){
                total2+=3;
                total2+=elf;
            } else if(player==3){
                total2+=6;
                if(elf!=3){
                    total2+=elf+1;
                } else {
                    total2+=elf-2;
                }
            } else {
                if(elf!=1){
                    total2+=elf-1;
                } else {
                    total2+=elf+2;
                }
            }
        }
        //part 1
        System.out.println(total);
        //part 2
        System.out.println(total2);
    }
}
