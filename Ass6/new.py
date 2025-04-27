class Password_manager:
    def __init__(self):
        self.old_passwords = []

    def get_password(self):
        # Return the current password (last item in the list)
        return self.old_passwords[-1] if self.old_passwords else None

    def set_password(self, new_password):
        # Check if the new password is different from all past passwords
        if new_password not in self.old_passwords:
            self.old_passwords.append(new_password)
            return True
        return False

    def is_correct(self, password):
        # Check if the provided password is the current password
        return password == self.get_password()

# Function to take user input for passwords
def manage_passwords():
    pm = Password_manager()
    
    while True:
        action = input("Choose an action: (1) Set Password, (2) Get Current Password, (3) Check Password, (4) Exit: ")
        if action == '1':
            new_password = input("Enter new password: ")
            if pm.set_password(new_password):
                print("Password set successfully.")
            else:
                print("Password already used. Try a different one.")
        elif action == '2':
            current_password = pm.get_password()
            if current_password:
                print(f"Current password is: {current_password}")
            else:
                print("No password set yet.")
        elif action == '3':
            password_to_check = input("Enter password to check: ")
            if pm.is_correct(password_to_check):
                print("Password is correct.")
            else:
                print("Password is incorrect.")
        elif action == '4':
            break
        else:
            print("Invalid action. Please choose a valid option.")

# Call the function to start the password manager
manage_passwords()
