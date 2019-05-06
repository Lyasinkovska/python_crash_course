def sandwich(*products):
    print("You wants to add the next products to your sandwich:")
    for product in products:
        print("- "+product)

sandwich("bread", "cheese")