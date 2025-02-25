"""
Test cases for linked list operations.
"""

import unittest

from src.linked_list import ListNode, reverse_linked_list


class TestLinkedList(unittest.TestCase):
    def test_reverse_linked_list(self):
        """Test reversing a normal linked list with multiple nodes [1->2->3]."""
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)

        reversed_head = reverse_linked_list(head)

        self.assertEqual(reversed_head.val, 3)
        self.assertEqual(reversed_head.next.val, 2)
        self.assertEqual(reversed_head.next.next.val, 1)
        self.assertIsNone(reversed_head.next.next.next)

    def test_reverse_single_node(self):
        """Test reversing a linked list with a single node [1]."""
        head = ListNode(1)
        reversed_head = reverse_linked_list(head)

        self.assertEqual(reversed_head.val, 1)
        self.assertIsNone(reversed_head.next)

    def test_reverse_empty_list(self):
        """Test reversing an empty linked list."""
        reversed_head = reverse_linked_list(None)
        self.assertIsNone(reversed_head)
