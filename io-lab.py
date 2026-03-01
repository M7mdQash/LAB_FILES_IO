while True:
    answer = input("Do you want to add a new To-Do item? (y/n/exit): ").strip().lower()

    if answer == "exit":
        print("Programm terminating...")
        break
    elif answer == "y":
        item = input("Enter your new To-Do item: ").strip()
        with open("to_do.txt", "a") as file:
            file.write(item + "\n")
        print("To-Do item saved!")
    elif answer == "n":
        show = input("Do you want to list your To-Do items? (y/n): ").strip().lower()
        if show == "y":
            try:
                with open("to_do.txt", "r") as files:
                    items = files.readlines()
                if items:
                    print("Your To-Do list:")
                    for i, item in enumerate(items, 1):
                        print(f"{i}. {item.strip()}")
                else:
                    print("Your To-Do list is empty.")
            except FileNotFoundError:
                print("Your To-Do list is empty.")
