# write a python function to remove a given word from a list ad strip at the same time 

# Function to remove a given fruit and strip extra spaces
def remove_fruit_strip(list_of_fruits, fruit_to_remove):
    # Remove spaces from each fruit in the list
    clean_list = [fruit.strip() for fruit in list_of_fruits]
    
    # Strip spaces from the fruit to remove
    fruit_to_remove = fruit_to_remove.strip()
    
    print("Cleaned list of fruits:", clean_list)
    
    # Check if fruit exists before removing
    if fruit_to_remove in clean_list:
        clean_list.remove(fruit_to_remove)
        print("Updated fruits list is:", clean_list)
    else:
        print(f"'{fruit_to_remove}' not found in the list.")

# --- main part ---
list_of_fruits = []

for i in range(5):
    fruit = input(f"Enter fruit {i+1}: ")
    list_of_fruits.append(fruit)

print("Original list:", list_of_fruits)

fruit_to_remove = input("Enter the fruit you want to remove: ")

remove_fruit_strip(list_of_fruits, fruit_to_remove)
