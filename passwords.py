class password:
    def __init__ (self,password):
        self.password = password
        if len(self.password) >= 8 and any(char.isdigit() for char in self.password) and any(char.isupper() for char in self.password) and any(char.islower() for char in self.password) and any(char in "!@#$%^&*()-_=+[{]}\|;:'\",<.>/?`~" for char in self.password):
            print("Valid password")
        else:
            print("Invalid password.")


 if input(self.password) == self.password:
   print(Access granted)
 else:  
    print(Access denied)

    for i in range(2):
       input(self.password)
