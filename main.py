from store import Store
from products import Product
from products import NonStockedProduct
from products import LimitedProduct


def start(store):
    while True:
        print("\n---------- MENU ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            products = store.get_all_products()
            print("\n--- Products in Store ---")
            for product in products:
                print(product.show())

        elif choice == "2":
            total_quantity = store.get_total_quantity()
            print(f"\nTotal amount in store: {total_quantity}")

        elif choice == "3":
            shopping_list = []
            while True:
                product_name = input("Enter the product name (or 'done' to finish: ")
                if product_name == "done":
                    break

                quantity = int(input("Enter the quantity: "))
                product = next((p for p in store.products if p.name == product_name), None)
                if product is None:
                    print("Product not found.")
                    continue

                shopping_list.append((product, quantity))

            total_price = store.order(shopping_list)
            print(f"\nTotal price of the order: {total_price} dollars")

        elif choice == "4":
            print("Thank you for using the store. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


def main():
    # setup initial stock of inventory
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250),
                    NonStockedProduct("Windows License", price=125),
                    LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
                    ]

    best_buy = Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()