import unittest
import SLPriorityQueue

class PQTests(unittest.TestCase):

    def test_init(self):
        slq = SLPriorityQueue.PriorityQueue()
        self.assertIsInstance(slq, SLPriorityQueue.PriorityQueue)
        self.assertTrue(slq.is_empty(), "is_empty should return True at initialization.")
        self.assertTrue(slq.size()==0, "Size should be 0 at initialization.")

    def test_enqueue(self):
        slq = SLPriorityQueue.PriorityQueue()
        slq.enqueue(4)
        slq.enqueue(3)
        slq.enqueue(2)
        self.assertTrue(slq.size()==3, "Size should be 3 after enqueueing 3 items.")
        self.assertFalse(slq.is_empty(), "is_empty should return False after enqueueing 3 items.")
        slq.enqueue(2)
        self.assertTrue(slq.size()==4, "Size should be 4 after enqueueing 4 items.")
        self.assertFalse(slq.is_empty(), "is_empty should return False after enqueueing 3 items.")

    def test_size(self):
        slq = SLPriorityQueue.PriorityQueue()
        slq.enqueue(5)
        slq.enqueue(4)
        self.assertTrue(slq.size()==2, "size should be 2 after enqueueing 2 items")
        slq.enqueue(3)
        self.assertTrue(slq.size()==3, 'size should be 3 after enqueueing 3 items')

    def test_dequeue(self):
        slq = SLPriorityQueue.PriorityQueue()
        slq.enqueue(5)
        slq.enqueue(4)
        self.assertEqual(slq.dequeue(),4 , 'dequeue should return the top priority item.')
        slq.enqueue(3)
        self.assertEqual(slq.dequeue(), 3 , 'dequeue should return the top priority item.')
        self.assertTrue(slq.size()== 1, 'size should be 1 after dequeueing twice.')
        self.assertFalse(slq.is_empty(), 'is_empty should return False after 1 dequeue.')

    def test_first(self):
        slq = SLPriorityQueue.PriorityQueue()
        slq.enqueue(4)
        self.assertTrue(slq.first()==4, 'First should return the top priority item')
        slq.enqueue(3)
        self.assertTrue(slq.first()==3, 'First should return the top priority item')
        slq.enqueue(2)
        self.assertTrue(slq.first()==2, 'First should return the top priority item')

    def test_is_empty(self):
        slq = SLPriorityQueue.PriorityQueue()
        self.assertTrue(slq.is_empty(), 'is_empty should return True when there are no items in the Queue.')
        slq.enqueue(5)
        slq.enqueue(4)
        self.assertFalse(slq.is_empty(), 'is_empty should return False after enqueueing 2 items.')
        slq.dequeue()
        self.assertFalse(slq.is_empty(), 'is_empty should return False affter dequeueing 1 item.')
        slq.enqueue(3)
        self.assertFalse(slq.is_empty(), 'is_empty should return False after enqueueing 1 item.')
        slq.dequeue()
        slq.dequeue()
        self.assertTrue(slq.is_empty(), 'is_empty should return True after dequeueing all items in the Queue.')

    def test_empty_str(self):
        slq = SLPriorityQueue.PriorityQueue()
        #test empty
        self.assertEqual(str(slq), "", "An empty priority queue should return an empty string.")

    def test_str(self):
        slq = SLPriorityQueue.PriorityQueue()
        slq.enqueue(4)
        slq.enqueue(4)
        self.assertEqual(str(slq), "4\n4\n")
        slq.dequeue()
        slq.enqueue(3)
        slq.enqueue(2)
        self.assertEqual(str(slq), "2\n3\n4\n")

if __name__ == '__main__':
    unittest.main()