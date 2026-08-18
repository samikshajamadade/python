print("=========== NAME SANITIZER ===========\n")

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

clean_first_name = first_name.strip()
clean_last_name = last_name.strip()

formatted_first_name = clean_first_name.title()
formatted_last_name = clean_last_name.title()

full_name = formatted_first_name + " " + formatted_last_name

print("\nClean Full Name:")
print(full_name)