import java.util.Scanner;

/**
 * @Author Frederik Alexander Hounsvad: frhou18 - Oliver Lind Nordestgaard: olnor18
 */
public class Treesort {
    
    public static void main(String... args){
        DictBinTree dict = new DictBinTree();
        Scanner scanner = new Scanner(System.in);
        while(scanner.hasNextInt()){
            dict.insert(scanner.nextInt());
        }
        dict.orderedTraversal().forEach(i -> System.out.println(i));
        scanner.close();
    }
}