import sys
class LootBag(object):
	def __init__(self):
		self.contents = set();
		self.nice_list = list();

	def add_toy_for_child(self, toy_name, child_name):
		self.contents.add((toy_name, child_name));
		self.set_nice_list_from_bag_contents();

	def remove_toy_for_child(self, child_name, toy_name):
		self.contents.discard((toy_name, child_name));
		self.set_nice_list_from_bag_contents();


	def list_children_getting_toys(self):
		nice_children = set();
		for child in self.nice_list:
			nice_children.add(child["name"]);
		return nice_children;

	def set_nice_list_from_bag_contents(self):
		self.nice_list = list();
		for tup in self.contents:
			self.nice_list.append({"name": tup[1], "delivered": False});

	def list_toys_for_child(self, child_name):
		items_for_child = set()
		for tup in self.contents:
			if tup[1] == child_name:
				items_for_child.add(tup[0]);
		return items_for_child;

	def set_child_delivery_status(self, child_name, delivery_status=False):
		for child in self.nice_list:
			if child["name"] == child_name:
				child["delivered"] = delivery_status;

	def get_child_delivery_status(self, child_name):
		for child in self.nice_list:
			if child["name"] == child_name:
				return child["delivered"];