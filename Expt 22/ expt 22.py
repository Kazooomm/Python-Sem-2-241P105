'''exp 22'''
# Class representing a product
class Product:
    def _init_(self, product_id, name, price, stock):
        # Initializes the product with ID, name, price, and available stock
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
        # Reduces the stock when a product is added to the cart
        # Returns True if the stock is sufficient, else False
        if self.stock >= quantity:
            self.stock -= quantity
            return True
        else:
            return False

    def restock(self, quantity):
        # Adds stock back when an item is removed from the cart
        self.stock += quantity

    def _str_(self):
        # String representation of the product details
        return f"{self.name} (ID: {self.product_id}) - ${self.price} (Stock: {self.stock})"


# Class representing a customer's shopping cart
class ShoppingCart:
    def _init_(self):
        # Initializes an empty dictionary to hold the cart items
        self.items = {}

    def add_item(self, product, quantity):
        # Adds an item to the cart if enough stock is available
        if product.update_stock(quantity):
            if product.product_id in self.items:
                # If product is already in the cart, increase the quantity
                self.items[product.product_id]['quantity'] += quantity
            else:
                # If product is not in the cart, add it
                self.items[product.product_id] = {'product': product, 'quantity': quantity}
            print(f"Added {quantity} of {product.name} to the cart.")
        else:
            # Not enough stock to add the item
            print(f"Not enough stock for {product.name}. Available stock: {product.stock}")

    def remove_item(self, product, quantity):
        # Removes an item from the cart, restocking it to the store
        if product.product_id in self.items:
            if self.items[product.product_id]['quantity'] >= quantity:
                # If the quantity to be removed is valid, reduce the quantity and restock
                self.items[product.product_id]['quantity'] -= quantity
                product.restock(quantity)
                print(f"Removed {quantity} of {product.name} from the cart.")
            else:
                # If there is not enough quantity to remove
                print(f"Not enough quantity of {product.name} in the cart to remove.")
        else:
            # If the item is not in the cart
            print(f"{product.name} is not in the cart.")

    def calculate_total(self):
        # Calculates and returns the total cost of all items in the cart
        total = 0
        for item in self.items.values():
            total += item['product'].price * item['quantity']
        return total

    def checkout(self):
        # Finalizes the order by calculating the total and clearing the cart
        total = self.calculate_total()
        print(f"Total cost of your cart: ${total}")
        self.items.clear()  # Empty the cart after checkout
        print("Checkout complete. Cart is now empty.")


# Class representing a customer
class Customer:
    def _init_(self, customer_id, name):
        # Initializes the customer with an ID, name, and an empty shopping cart
        self.customer_id = customer_id
        self.name = name
        self.cart = ShoppingCart()

    def add_to_cart(self, product, quantity):
        # Adds an item to the customer's cart
        self.cart.add_item(product, quantity)

    def remove_from_cart(self, product, quantity):
        # Removes an item from the customer's cart
        self.cart.remove_item(product, quantity)

    def view_cart(self):
        # Displays the customer's cart details
        print(f"Cart of {self.name}:")
        for item in self.cart.items.values():
            print(f"{item['product'].name} - Quantity: {item['quantity']} - ${item['product'].price} each")
        print(f"Total: ${self.cart.calculate_total()}")

    def checkout(self):
        # Proceeds with the checkout process for the customer
        self.cart.checkout()


# Class representing the store
class Store:
    def _init_(self):
        # Initializes the store with an empty product catalog
        self.products = {}

    def add_product(self, product):
        # Adds a product to the store's inventory
        self.products[product.product_id] = product

    def get_product_by_id(self, product_id):
        # Retrieves a product by its ID from the store's inventory
        return self.products.get(product_id, None)

    def list_products(self):
        # Displays all available products in the store
        print("Available Products:")
        for product in self.products.values():
            print(product)


# Function to display the menu options
def display_menu():
    print("\n===== Online Shopping System =====")
    print("1. View All Products")
    print("2. Add Product to Cart")
    print("3. Remove Product from Cart")
    print("4. View Cart")
    print("5. Checkout")
    print("6. Exit")
    print("==================================")


# Main function that runs the shopping system
def main():
    # Create the store and add some products
    store = Store()
    apple = Product(1, "Apple", 1.0, 100)
    banana = Product(2, "Banana", 0.5, 150)
    orange = Product(3, "Orange", 0.8, 50)

    store.add_product(apple)
    store.add_product(banana)
    store.add_product(orange)

    # Create a customer
    customer = Customer(1, "John Doe")

    # Main loop: displays the menu and handles user choices
    while True:
        display_menu()  # Show the menu to the user
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            # View all available products
            store.list_products()
        
        elif choice == '2':
            # Add a product to the cart
            store.list_products()  # Show available products
            product_id = int(input("Enter the product ID you want to add to the cart: "))
            quantity = int(input("Enter the quantity: "))
            product = store.get_product_by_id(product_id)
            if product:
                customer.add_to_cart(product, quantity)
            else:
                print("Invalid product ID.")
        
        elif choice == '3':
            # Remove a product from the cart
            store.list_products()  # Show available products
            product_id = int(input("Enter the product ID you want to remove from the cart: "))
            quantity = int(input("Enter the quantity: "))
            product = store.get_product_by_id(product_id)
            if product:
                customer.remove_from_cart(product, quantity)
            else:
                print("Invalid product ID.")
        
        elif choice == '4':
            # View the customer's cart
            customer.view_cart()
        
        elif choice == '5':
            # Proceed to checkout
            customer.checkout()
        
        elif choice == '6':
            # Exit the program
            print("Thank you for using the Online Shopping System.")
            break  # Exit the loop and terminate the program
        
        else:
            # Handle invalid menu choices
            print("Invalid choice. Please try again.")


# Run the system if the script is executed directly
if _name_ == "_main_":
    main()
