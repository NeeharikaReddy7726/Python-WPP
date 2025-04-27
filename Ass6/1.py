class Password_manager:
    def __init__(self):
        self.old_passwords = []

    def get_password(self):
        # Returns the current password, which is the last item in the list
        return self.old_passwords[-1] if self.old_passwords else None

    def set_password(self, new_password):
        if new_password not in self.old_passwords:
            self.old_passwords.append(new_password)
            print("Password updated successfully.")
        else:
            print("Password has been used before. Please choose a different password.")

    def is_correct(self, password):
        # Checks if the given password is the current password
        return password == self.get_password()
pm = Password_manager()
pm.set_password("password1")
print(pm.get_password())  # Output: password1
print(pm.is_correct("password1"))  # Output: True
print(pm.is_correct("password2"))  # Output: False
pm.set_password("password2")
print(pm.get_password())  
pm.set_password("password1")  
