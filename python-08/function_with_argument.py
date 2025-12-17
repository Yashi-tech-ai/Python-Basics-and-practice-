def greeting(name, ending_salutations):
    message = "Good morning! " + name + " " + ending_salutations
    return message  # 👈 This *sends back* the message

a = greeting("Yashi", "Thank you")  # 👈 Now a receives the returned message
print(a)  # 👈 We print what was returned
