import java.util.*;


public class TestTaks1 {
    public static void main(String... args) {
        //********** test case 1 **********\\
        System.out.println("//********** test case 1 **********\\\\");
        System.out.println("Insert, OrderdTraversal, Search Tests");
        DictBinTree dict = new DictBinTree();
        List<Integer> randomInserts = new ArrayList<>();
        Random r = new Random();
        for (short i = 0; i < 20; i++) {
            randomInserts.add(r.nextInt(100));
        }
        randomInserts.add(100);
        randomInserts.add(100);
        for (Integer i : randomInserts) {
            dict.insert(i);
        }
        
        System.out.printf("%20s", "Unsorted tree: ");
        randomInserts.forEach(i -> System.out.printf(" %3d,", i));
        Collections.sort(randomInserts);
        System.out.println();
        System.out.printf("%20s", "Sorted random: ");
        randomInserts.forEach(i-> System.out.printf( " %3d,", i));
        System.out.println();
        System.out.printf("%20s", "dict sorted: ");
        dict.orderedTraversal().forEach(i-> System.out.printf(" %3d,", i));
        System.out.println();
        System.out.println("The list is sorted: "+randomInserts.equals(dict.orderedTraversal()));
        System.out.println("Search for present number: " + dict.search(100));
        System.out.println("Search for not present number: " + dict.search(101));
        

        //********** test case 2 **********\\
        System.out.println("//********** test case 2 **********\\\\");
        System.out.println("No input - Search and orderedTraversel");
        dict = new DictBinTree();
        System.out.println("Search for 1: " + dict.search(1));
        System.out.print("Traverse empty: ");
        dict.orderedTraversal().forEach(i -> System.out.print(i + ", "));
        System.out.println();
    }
}