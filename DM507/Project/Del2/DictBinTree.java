import java.util.ArrayList;
import java.util.List;

/**
 * @Author Frederik Alexander Hounsvad: frhou18 - Oliver Lind Nordestgaard: olnor18
 */
public class DictBinTree implements Dict {

    public BinNode rootNode = null;

    DictBinTree() {

    }

    //Inserts a node with the key k into the tree by appending it as a child of an appropriate node
    public void insert(int k) {
        //Create a new node with the given key an null as both legs
        BinNode newNode = new BinNode(k, null, null);
        BinNode parentNode = null;
        BinNode currentNode = rootNode;
        while (currentNode != null) {
            //if the new node has a key smaller than the key of the current node then we set currentNode to be the left leg of currentNode else we set currentNode to be the rigth leg of currentNode
            //this loops until currentNode is null meaning we have reached the end of the tree
            parentNode = currentNode;
            currentNode = newNode.k < currentNode.k ? currentNode.leftLeg : currentNode.rightLeg; 
        }
        if (parentNode == null) {
            // if parentNode has not been set in the loop above, then currentNode == null meaning rootnode is null, therefore the new node is the root
            rootNode = newNode;
        } else if (newNode.k < parentNode.k) {
            // if the key of the new node is smaller than the key of parentNode then the left leg of parentNode is the new node
            parentNode.leftLeg = newNode;
        } else {
            // if the key of the new node is larger or equal to the key of parentNode then the right leg of parentNode is the new node
            parentNode.rightLeg = newNode;
        }

    }

    public ArrayList<Integer> orderedTraversal() {
        //Creates a list to hold the return values and recursively orders the new list starting from the root, then returns it
        ArrayList<Integer> returnList = new ArrayList<>();
        orderedTraversalRecursive(returnList, rootNode);
        return returnList;
    }
    private void orderedTraversalRecursive(List<Integer> returnList, BinNode x) {
        //if the input node is null then it doens't do anything, else it calls the sort of the left leg, as those as smaller than itself, so they should be added first
        //Then is adds itself
        //Then it calls the sort of the rigth leg as those should be added after itself
        if(x != null){
            orderedTraversalRecursive(returnList, x.leftLeg);
            returnList.add(x.k);
            orderedTraversalRecursive(returnList, x.rightLeg);
        }
    }

    public boolean search(int k) {
        return searchRecursive(k, rootNode);
    }

    private boolean searchRecursive(int k, BinNode x) {
        //If the current node is null then return false as the end has been reached without finding the key
        //If the searchKey is equal to the key of the current node then we have found it and should return true
        //If the seachKey is smaller than the current node's key then search down the left leg of the current node
        //Else search down the right leg of the current node
        if (x == null)
            return false;
        if (x.k == k)
            return true;
        if (k < x.k)
            return searchRecursive(k, x.leftLeg);
        else
            return searchRecursive(k, x.rightLeg);
    }

}
