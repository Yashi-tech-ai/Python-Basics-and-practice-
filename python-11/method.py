class employee:
    a = 1 
    @classmethod  # this will print the class attribute only even though there will be an object attribute 
    def show(cls):
        print(f"The class attribute is {cls.a}")
    @property # you can return anything 
    def name(self):
        return f"{self.fname} {self.lname}"
    @name.setter
    def set(self,value):
        self.fname = value.split()[0] # splits into list and stores in a  list so here first name is fname 
        self.lname = value.split()[1]

# Create the object
o = employee()
# Set the name using setter
o.name = "Yashi Sharma"
# Get the name using the property
print(o.name)  # ✅ Should print: Yashi Sharma
# Optional: show class attribute
o.show()       # ✅ Should print: The class attribute is 1
