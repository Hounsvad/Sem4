/**
 * @Author Frederik Alexander Hounsvad: frhou18 - Oliver Lind Nordestgaard: olnor18
 */
public class HoffmanTree {

    public BinNode rootNode = null;
    public HoffmanTree(BinNode k){
        this.rootNode = k;
    }

    public static HoffmanTree HoffmanTreeFactory(int[] characterFrequency){
        PQHeap Q = new PQHeap();

        /*
         * The PQHeap contains elements with frequency as their key and trees as data
         * Nodes in a tree without legs are leafs, and their keys are the int value for the char
         * Nodes with legs have a key of the combined frequency of the connected leafs.
         */
        for (int i = 0; i < characterFrequency.length; i++){
            HoffmanTree tree = new HoffmanTree(new BinNode(i, null, null));
            Q.insert(new Element(characterFrequency[i], tree));
        }

        /*
         * x and y are the two smallest elements of the PQ. Their frequency is combined as the key for the new element z.
         * The data of z is a new tree in which a new node is created as the root, which has the frequency as it's key.
         * The legs of the new root node is the roots of the trees contained in the data of x and y.
         */
        for (int i = 0; i<Encode.n-1; i++){
            Element x = Q.extractMin();
            Element y = Q.extractMin();
            int frequencyForZ = x.getKey() + y.getKey();
            HoffmanTree tree = new HoffmanTree(new BinNode(frequencyForZ, ((HoffmanTree) x.getData()).rootNode, ((HoffmanTree) y.getData()).rootNode));
            Element z = new Element(frequencyForZ, tree);
            Q.insert(z);
        }

        return ((HoffmanTree) Q.extractMin().getData());
    }

    public String[] getHoffmanKeywords() {
        //Creates a list to hold the return values and recursively orders the new list starting from the root, then returns it
        String[] returnList = new String[Encode.n];
        hoffmanKeywordTraversalRecursive(returnList, rootNode, "");
        return returnList;
    }
    private void hoffmanKeywordTraversalRecursive(String[] returnList, BinNode x, String bytecode) {
        //if the input node is null then it doens't do anything, else it calls the sort of the left leg, as those as smaller than itself, so they should be added first
        //Then is adds itself
        //Then it calls the sort of the rigth leg as those should be added after itself
        if(x != null){
            hoffmanKeywordTraversalRecursive(returnList, x.leftLeg, bytecode+"0");
            if (x.leftLeg == null) {
                returnList[x.k] = bytecode;//Byte.decode(bytecode).intValue();
            }
            hoffmanKeywordTraversalRecursive(returnList, x.rightLeg, bytecode+"1");
        }
    }
}
