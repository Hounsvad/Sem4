import java.util.ArrayList;
import java.util.List;

public class PQHeap implements PQ{
    private List<Element> elements = new ArrayList<>();
    public PQHeap() {
    }

    @Override
    public Element extractMin() {
        Element smallestElement = elements.get(0);
        elements.set(0, elements.get(elements.size()-1));
        elements.remove(elements.size()-1);
        minHeapify(0);
        return smallestElement;
    }

    @Override
    public void insert(Element e) {
        elements.add(e);
        int i = elements.size()-1;
        while (i > 0 && elements.get(parent(i)).getKey() >= e.getKey()){
            Element parent = elements.get(parent(i));
            Element child = elements.get(i);
            elements.set(parent(i), child);
            elements.set(i, parent);
            i = parent(i);
        }
    }

    private int parent(int i){
        return (i-1) / 2;
    }

    private int leftChild(int i){
        return 2*i+1;
    }

    private int rightChild(int i){
        return 2*i+2;
    }

    private void minHeapify(int index){
        int left = leftChild(index);
        int right = rightChild(index);       
        int smallest = index;
        if (left < elements.size() && elements.get(left).getKey() < elements.get(smallest).getKey()){    
            smallest = left;
        }
        if (right < elements.size() && elements.get(right).getKey() < elements.get(smallest).getKey()){
            smallest = right;
        }
        if (smallest != index){
            Element indexElement = elements.get(index);
            Element smallestElement = elements.get(smallest);
            elements.set(index, smallestElement);
            elements.set(smallest, indexElement);
            minHeapify(smallest);  			
        }
    }
}
