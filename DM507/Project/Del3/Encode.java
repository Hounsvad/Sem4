/**
 * @Author Frederik Alexander Hounsvad: frhou18 - Oliver Lind Nordestgaard: olnor18
 */

import java.io.*;
import java.util.List;

public class Encode {
    public static final int n = 256;

    int[] characterFrequency = new int[n];

    /**
     * Encode file with Hoffman encoding with a 8 bit character set.
     * @param inputFileName File path
     * @param outputFileName File path
     */
    public Encode(String inputFileName, String outputFileName){
        calculateCharacterFrequency(inputFileName);
        HoffmanTree tree = HoffmanTree.HoffmanTreeFactory(characterFrequency); //Generates a Hoffman tree
        String[] keywords = tree.getHoffmanKeywords();
        try(BitOutputStream out = new BitOutputStream(new FileOutputStream(outputFileName)); InputStream in = new FileInputStream(inputFileName);) {
            //Writing frequencies to start of compressed file
            for (int frequency : characterFrequency) {
                out.writeInt(frequency);
            }

            //EncodeFile
            int character;
            while ((character = in.read()) != -1) {
                for (char c : keywords[character].toCharArray()) {
                    out.writeBit(Integer.parseInt("" + c));
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    /**
     * Calculates frequencies of characters.
     * @param inputFileName
     */
    private void calculateCharacterFrequency(String inputFileName){
        try(InputStream inputStream = new FileInputStream(inputFileName)) {
            int character = 0;
            while ((character = inputStream.read()) != -1){
                characterFrequency[character] += 1;
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args){
        new Encode(args[0], args[1]);
    }
}