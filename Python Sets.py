# Q1 Task 1

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

# Find destinations both airlines fly to (intersection)
common_destinations = our_routes.intersection(competitor_routes)
print("Destinations both airlines fly to:", common_destinations)

# Find destinations unique to your airline (difference)
unique_to_us = our_routes.difference(competitor_routes)
print("Destinations unique to your airline:", unique_to_us)

# Check if there are destinations neither airline shares (symmetric difference)
combined_routes = our_routes.union(competitor_routes)
neither_airline = combined_routes.difference(common_destinations)
if neither_airline:
    print("There are destinations neither airline shares:", neither_airline)
else:
    print("All destinations are covered by at least one airline.")


# Q2 Task 1

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

# Convert the list to a set to automatically remove duplicates
unique_customer_ids = set(customer_ids)

# Print the set of unique customer IDs
print("Unique customer IDs:", unique_customer_ids)


# Q1 Task 1

artist_names = ["The Lumineers", "Tame Impala", "Billie Eilish", "The Lumineers", "Arctic Monkeys", "Tame Impala"]
unique_artists = set()
duplicate_playlists = False

# Loop through artist names
for artist in artist_names:
    if artist in unique_artists:
        duplicate_playlists = True
        break  # Exit the loop if a duplicate is found
    unique_artists.add(artist)

# Print results
if duplicate_playlists:
    print("Duplicate playlists found:", duplicate_playlists)
else:
    print("Unique artist lineup:", unique_artists)

