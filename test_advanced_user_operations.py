from advanced_user_operations import AdvancedUserOperations

advanced_user_ops = AdvancedUserOperations()

# Test creating a new user with profile information
print("Creating a new user...")
result_create = advanced_user_ops.create_user_with_profile('Joe', 'joe@example.com', 'joe123', age=39, gender='male', address='1200 Lewis Ave')
print("User creation result:", result_create)

# Test retrieving users based on specified criteria
print("\nRetrieving users...")
users = advanced_user_ops.retrieve_users_by_criteria(min_age=25, max_age=40, gender='female')
print("Retrieved users:", users)

# Test updating user profile information
print("\nUpdating user profile...")
result_update = advanced_user_ops.update_user_profile('john.doe@example.com', age=35, address='123 Lake St')
print("User profile update result:", result_update)

# Test deleting users based on specified criteria
print("\nDeleting users...")
result_delete = advanced_user_ops.delete_users_by_criteria(email="rob@mail.com")
print("User deletion result:", result_delete)


# Additional tests for edge cases 

# Tests  creating user with an existing email address
print("\nCreating a user with an existing email...")
result_existing_email = advanced_user_ops.create_user_with_profile('John', 'johnny@example.com', 'test123')
print("User creation with existing email result:", result_existing_email)

# Test updating a non-existing user profile
print("\nUpdating non-existing user profile...")
result_non_existing_user = advanced_user_ops.update_user_profile("flamingo@yahoo.com", age=46)
print("Update non-existing user result:", result_non_existing_user)
assert result_non_existing_user == False, "Expected False as the user does not exist."


# Test delete user by non-existing criteria
print("\nDelete a user by non-existing criteria...")
result_non_existing_criteria = advanced_user_ops.delete_users_by_criteria(email="1010 Fumigation Row")
print("User deletion from bad criteria:", result_non_existing_criteria)
assert result_non_existing_criteria == False, "Expected False as no users meet the specified criteria."

