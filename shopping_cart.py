class ShoppingCart:

    # Initialization of shopping cart
    def __init__(self, total=0, employee_discount = None, items = []):  
        self.total = total
        self.employee_discount = employee_discount
        self.items = items 
        
         # Adds an item to the cart
    def add_item(self, name, price, quantity=1):
        self.items.append({"name" : name, "price" : price, "quantity" : quantity})  # Items are stored as a list of dictionarys
        self.total += price * quantity                                              # Each dictionary has keys and values 
        return self.total                                                           # for item name, price, and quantity
    
        # Finds mean item price for the cart
    def mean_item_price(self):
        item_counter = 0                                # Find mean by first counting item quantities,
        for item in self.items:                         # Then divide self.total by the number of individual items              
            item_counter += item["quantity"]           
        return round(self.total / item_counter, 2)      # Round the final result to two decimals

        # Finds median item price for the cart
    def median_item_price(self):   
        item_prices = []                                # Find median by first making a list of individual item prices.
        for item in self.items:                         # Then selecting the middle number or the average of the two middle numbers.        
            for i in range(0, item["quantity"]):
                item_prices.append(item["price"])
        item_prices.sort()
        if len(item_prices) % 2 == 0:
            middle_index_one = int(len(item_prices)/2)
            middle_index_two = middle_index_one + 1
            result = (item_prices[middle_index_one] + item_prices[middle_index_two]) / 2 # Round the final result to two decimals
            return round(result, 2)
        else:
            result_index = int(len(item_prices)/2) + 1
            return item_prices[result_index]
                

    def apply_discount(self):
        if bool(self.employee_discount):                               # If there is a discount, return what the total would be after
            return self.total - self.total * self.employee_discount    # The discount is applied
        else: 
            return "Sorry, there is no discount to apply to your cart :("
            

    def void_last_item(self):
        if self.items == []:
            return "There are no items in your cart!"
        else:
            self.total -= self.items[-1]["price"]                              # Drop the total to reflect voiding the item
            self.items[-1]["quantity"] -=  1                                   # Lower the quantity of the last item
            if self.items[-1]["quantity"] < 1:                                 # If said item's quantity is below one remove the item from 
                self.items.pop()                                               # self.items