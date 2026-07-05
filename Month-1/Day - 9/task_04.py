# Task 4: **kwargs — variable keyword arguments


def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


show_info(name="Alice", age=25, city="New York")
print("---")
show_info(title="Manager", department="Engineering")
