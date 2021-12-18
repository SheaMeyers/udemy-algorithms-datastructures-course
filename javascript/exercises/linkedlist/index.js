// --- Directions
// Implement classes Node and Linked Lists
// See 'directions' document

class Node {
    constructor(data, next = null) {
        this.data = data;
        this.next = next;
    }
}

class LinkedList {
    constructor() {
        this.head = null;
    }

    insertFirst(data) {
        this.head = new Node(data, this.head);
        this.count += 1;
    }

    size() {
        let counter = 0;
        let node = this.head;

        while (node) {
            counter++;
            node = node.next;
        }

        return counter;
    }

    getFirst() {
        return this.head;
    }

    getLast() {
        if (this.head === null) {
            return null;
        }

        let node = this.head;

        while (true) {
            if (node.next === null) {
                break;
            }
            node = node.next;
        }

        return node;
    }

    clear() {
        this.head = null;
    }

    removeFirst() {
        if (this.head === null) {
            return;
        }

        this.head = this.head.next;
    }

    removeLast() {
        if (this.head === null) {
            return;
        }

        if (this.head.next === null) {
            this.head = null;
            return;
        }

        let currentNode = this.head;
        let nextNode = this.head.next;

        while (nextNode.next) {  // Not at the last one
            currentNode = nextNode;
            nextNode = nextNode.next;
        }

        currentNode.next = null;

        // Alternative solution
        // let node = this.head;

        // while (true) {
        //     if (node.next.next === null) {
        //         break;
        //     }
        //     node = node.next;
        // }

        // node.next = null;
    }

    insertLast(data) {
        const currentLast = this.getLast();
        const newLast = new Node(data);

        if (currentLast) {
            currentLast.next = newLast;
        } else {
            this.head = newLast;
        }
        
    }

    getAt(index) {
        let node = this.head;
        for (let i = 0; i < index; i++) {
            if (node === null) {
                return null;
            }
            node = node.next;
        }
        return node;
    }

    removeAt(index) {
        if (this.head === null) {
            return;
        }

        if (index === 0) {
            this.head = this.head.next;
        }

        let node = this.getAt(index-1);
        
        if (node === null || node.next === null) {
            return;
        }
        
        node.next = node.next.next;
    }

    insertAt(data, index) {
        // If out of bounds, put at end of the list

        if (this.head === null) {
            this.head = new Node(data);
            return;
        }

        if (index === 0) {
            this.head = new Node(data, this.head);
            return;
        }

        const previous = this.getAt(index - 1) || this.getLast();
        const node = new Node(data, previous.next);
        previous.next = node;
    }
}

module.exports = { Node, LinkedList };
