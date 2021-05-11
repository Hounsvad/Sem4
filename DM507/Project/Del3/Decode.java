/**
 * @Author Frederik Alexander Hounsvad: frhou18 - Oliver Lind Nordestgaard: olnor18
 */

import java.io.*;
import java.util.Arrays;

public class Decode {
    public static final int n = 256;

    /**
     * Decodes Hoffman encoded file with 8 bit character set
     * @param inputFileName
     * @param outputFileName
     */
    public Decode(String inputFileName, String outputFileName){
        try(
                BitInputStream in = new BitInputStream(new FileInputStream(inputFileName));
                OutputStream out = new FileOutputStream(outputFileName))
        {
            int[] characterFrequency = readCharacterFrequency(in);//
            int frequencySum = Arrays.stream(characterFrequency).sum();
            BinNode root = HoffmanTree.HoffmanTreeFactory(characterFrequency).rootNode;
            //Generate Hoffman tree and get root

            int bit;
            BinNode currentNode = root;
            int byteCounter = 0;

            while ((bit = in.readBit()) != -1 & frequencySum >= byteCounter){
                //Walk the tree based on the incoming bits
                if (bit == 0){
                    currentNode = currentNode.leftLeg;
                } else {
                    currentNode = currentNode.rightLeg;
                }

                //If at end of tree, treat node as leaf and consider key as character instead of weight
                if (currentNode.leftLeg == null){
                    out.write(currentNode.k); //Write character
                    currentNode = root; //Reset walk
                    byteCounter++; //Increment byteCounter to protect from EOF 0 fill
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    /**
     * Reads the character frequencies from the beginning of the file
     * @param in
     * @return
     * @throws IOException
     */
    private int[] readCharacterFrequency(BitInputStream in) throws IOException {
        int[] freq = new int[n];
        for(int i = 0; i < n; i++){
            freq[i] = in.readInt();
        }
        return freq;
    }

    public static void main(String[] args){
        new Decode(args[0], args[1]);
    }
}
