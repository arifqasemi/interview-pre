####################
#######  Data modeling in Python refers to the process of structuring and organizing data
# within Python programs, mirroring real-world entities and their relationships. It involves 
# defining data types, relationships, and constraints to create a blueprint for how data is 
# stored and manipulated. Python's data model formalizes the language's building blocks, such as
# sequences, iterators, and classes


class SaleOrder:
    def __init__(self, customer_name: str, items: list[dict]):
        """
        items: List of {'product_name': str, 'quantity': int}
        """
        if not customer_name.strip():
            raise ValueError("Customer name cannot be empty")
        if not items:
            raise ValueError("Items list cannot be empty")
        
        self.customer_name = customer_name
        self.items = items  # [{'product_name': str, 'quantity': int}]
    
    def get_total_quantity(self) -> int:
        """Return sum of quantities across all items."""
        total = 0
        for item in self.items:
            quantity = item.get('quantity', 0)
            if quantity > 0:
                total += quantity
        return total

# Test cases
order = SaleOrder("John Doe", [
    {'product_name': 'Laptop', 'quantity': 2},
    {'product_name': 'Phone', 'quantity': 3}
])
print(order.get_total_quantity())  # Output: 5
try:
    SaleOrder("", [])  # Raises ValueError
except ValueError as e:
    print(e)  # Output: Customer name cannot be empty
    
    




class DiscountedSaleOrder(SaleOrder):
    def __init__(self, customer_name: str, items: list[dict], discount: float):
        super().__init__(customer_name, items)
        if not 0 <= discount <= 100:
            raise ValueError("Discount must be between 0 and 100")
        self.discount = discount
    
    def get_total_quantity(self) -> float:
        """Return total quantity after applying discount."""
        parent_total = super().get_total_quantity()
        return parent_total * (1 - self.discount / 100)

# Test cases
order = DiscountedSaleOrder("Jane Doe", [
    {'product_name': 'Tablet', 'quantity': 4},
    {'product_name': 'Mouse', 'quantity': 2}
], discount=20)
print(order.get_total_quantity())  # Output: 4.8 (6 * 0.8)
try:
    DiscountedSaleOrder("John", [], 150)  # Raises ValueError
except ValueError as e:
    print(e)  # Output: Items list cannot be empty
    
    
    
    
    
    

class Item:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def update_quantity(self, amount):
        self.quantity += amount

    def __str__(self):
        return f"{self.name}: {self.quantity} units @ ${self.price:.2f} each"


class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        if item.name in self.items:
            self.items[item.name].update_quantity(item.quantity)
        else:
            self.items[item.name] = item

    def remove_item(self, item_name, quantity):
        if item_name in self.items:
            item = self.items[item_name]
            if item.quantity >= quantity:
                item.update_quantity(-quantity)
                print(f"{quantity} {item_name}(s) removed.")
            else:
                print(f"Not enough {item_name} in stock.")
        else:
            print(f"{item_name} not found in inventory.")

    def get_inventory(self):
        for item in self.items.values():
            print(item)
