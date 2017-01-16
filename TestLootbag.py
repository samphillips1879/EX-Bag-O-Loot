import unittest 
from lootbag import *


class Test_LootBag(unittest.TestCase):
	
	# 1. Items can be added to bag, and assigned to a child.
	def test_toy_for_child_can_bed_added_to_LootBag(self):
		bag = LootBag();
		bag.add_toy_for_child("Teddy Bear", "Theodore");
		bag.add_toy_for_child("Slinky", "Theodore");
		self.assertIn("Teddy Bear", bag.list_toys_for_child("Theodore"));

	# 1. Items can be removed from bag, per child. Removing `ball` from the bag should not be allowed. A child's name must be specified.
	def test_toy_for_child_can_be_removed_from_LootBag(self):
		bag = LootBag();
		bag.add_toy_for_child("Teddy Bear", "Theodore");
		bag.add_toy_for_child("Slinky", "Theodore");
		bag.remove_toy_for_child("Theodore", "Slinky");
		self.assertNotIn("Slinky", bag.list_toys_for_child("Theodore"));

	# 1. Must be able to list all children who are getting a toy.
	def test_children_getting_toys_can_be_listed(self):
		bag = LootBag();
		bag.add_toy_for_child("Teddy Bear", "Theodore");
		bag.add_toy_for_child("Stuffed Bunny", "Lorelai");
		self.assertIn("Lorelai", bag.list_children_getting_toys());
		self.assertIn("Theodore", bag.list_children_getting_toys());

	# 1. Must be able to list all toys for a given child's name.
	def test_toys_for_a_given_child_can_be_listed(self):
		bag = LootBag();
		bag.add_toy_for_child("Teddy Bear", "Theodore");
		bag.add_toy_for_child("Slinky", "Theodore");
		bag.add_toy_for_child("Keyboard", "Theodore");
		self.assertEqual({"Teddy Bear", "Slinky", "Keyboard"}, bag.list_toys_for_child("Theodore"));


	# 1. Must be able to set the *delivered* property of a child, which defaults to `false` to `true`.
	def test_able_to_set_and_get_delivery_status_for_a_child(self):
		bag = LootBag();
		bag.add_toy_for_child("Teddy Bear", "Theodore");
		self.assertFalse(bag.get_child_delivery_status("Theodore"));
		bag.set_child_delivery_status("Theodore", True);
		self.assertTrue(bag.get_child_delivery_status("Theodore"));


if __name__ == "__main__":
	unittest.main()