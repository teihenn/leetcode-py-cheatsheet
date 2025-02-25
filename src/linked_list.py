"""
Linked List operations module.

This module provides functionality for manipulating singly linked lists,
including operations like reversing the list.
"""


class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def reverse_linked_list(head: ListNode) -> ListNode:
    """
    Reverses a singly linked list.

    Args:
        head (ListNode): The head node of the linked list

    Returns:
        ListNode: The head node of the reversed linked list
    """
    prev = None
    current = head

    while current is not None:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp

    return prev
