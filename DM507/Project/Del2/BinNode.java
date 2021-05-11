/**
 * @Author Frederik Alexander Hounsvad: frhou18 - Oliver Lind Nordestgaard: olnor18
 */
public class BinNode{
    public BinNode leftLeg = null;
    public BinNode rightLeg = null;
    public int k;

    BinNode(int k, BinNode leftLeg, BinNode rightLeg){
        this.k = k;
        this.leftLeg = leftLeg;
        this.rightLeg = rightLeg;
    }
}