Node Reverse(Node head) {
    if(head == null || head.next == null) return head; // null list and last item in list

    Node remain = Reverse(head.next);   //recursion to reach last position

    head.next.next = head;              //switching the back position to go towards the front

    head.next = null;                   //setting the back to front position with a null case to find value

    return remain;                      //returning all the Nodes from back to front
}