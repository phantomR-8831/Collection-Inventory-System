class CollectionItem:
    def __init__(self, name, category, purchase_price, current_value, location):
        self.name = name
        self.category = category
        self.purchase_price = purchase_price
        self.current_value = current_value
        self.location = location
        self.status = "In Inventory"

    def get_roi(self):
        """Рассчитывает рентабельность инвестиции в предмет"""
        return ((self.current_value - self.purchase_price) / self.purchase_price) * 100

# Пример работы системы
collection = [
    CollectionItem("Vintage Camera", "Electronics", 100, 150, "Shelf A1"),
    CollectionItem("Rare Coin", "Numismatics", 500, 750, "Safe Box 1")
]

print("--- Collection Status Report ---")
for item in collection:
    print(f"Item: {item.name} | ROI: {item.get_roi()}% | Location: {item.location}")