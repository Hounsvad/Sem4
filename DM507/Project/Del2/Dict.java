import java.util.ArrayList;

/**
 * @Author Frederik Alexander Hounsvad: frhou18 - Oliver Lind Nordestgaard: olnor18
 */
public interface Dict {
    public void insert(int k);
    public ArrayList<Integer> orderedTraversal();
    public boolean search(int k);
}