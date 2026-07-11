# Task 4: Sets — creation, add, remove, discard, membership

unique_ids = set()

# add — idempotent
unique_ids.add(101)
unique_ids.add(102)
unique_ids.add(101)  # ignored
print("After adds:", unique_ids)

# remove — raises KeyError if missing
unique_ids.remove(101)
print("After remove 101:", unique_ids)

# discard — silent if missing
unique_ids.discard(999)  # no error
print("After discard 999:", unique_ids)

# membership
print("102 in set:", 102 in unique_ids)
print("999 in set:", 999 in unique_ids)
