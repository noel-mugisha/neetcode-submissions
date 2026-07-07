class LRUCache {
    private static class Node {
        int key;
        int value;
        Node prev;
        Node next;

        Node (int key, int value) {
            this.key = key;
            this.value = value;
        }
    }
    private int capacity;
    private Node head;
    private Node tail;
    private Map<Integer, Node> map;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        map = new HashMap<>();
    }
    
    public int get(int key) {
        if (!map.containsKey(key))
            return -1;

        Node node = map.get(key);

        detachNode(node);
        attachToTail(node);

        return node.value;
    }
    
    public void put(int key, int value) {
        if (map.containsKey(key)) {
            Node node = map.get(key);
            node.value = value;
            detachNode(node);
            attachToTail(node);
        } else {
            if (capacity == map.size()) {
                map.remove(head.key);
                detachNode(head);
            }

            Node newNode = new Node(key, value);
            map.put(key, newNode);
            attachToTail(newNode);
        }
    }

    void detachNode(Node node) {
        if (head == node && tail == node) {
            head = null;
            tail = null;
        }

        else if (node == head) {
            head = node.next;
            head.prev = null;
        }

        else if (node == tail) {
            tail = node.prev;
            tail.next = null;
        }

        else {
            node.prev.next = node.next;
            node.next.prev = node.prev;
        }

        node.prev = null;
        node.next = null;
    }

    void attachToTail(Node node) {
        if (tail == null) {
            head = node;
        }
        else {
            tail.next = node;
            node.prev = tail;
        }
        tail = node;
    }
}