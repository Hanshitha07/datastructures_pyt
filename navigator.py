class BrowserHistory:
    def __init__(self, homepage):
        self.back_stack = []
        self.forward_stack = []
        self.current = homepage

    def visit(self, url):
        self.back_stack.append(self.current)
        self.current = url
        self.forward_stack.clear()
        print("Visited:", self.current)

    def back(self):
        if self.back_stack:
            self.forward_stack.append(self.current)
            self.current = self.back_stack.pop()
            print("Back to:", self.current)
        else:
            print("No previous page")

    def forward(self):
        if self.forward_stack:
            self.back_stack.append(self.current)
            self.current = self.forward_stack.pop()
            print("Forward to:", self.current)
        else:
            print("No next page")

    def show_current(self):
        print("Current page:", self.current)


# Interactive Mode
browser = BrowserHistory("homepage.com")
print("Browser started at:", browser.current)
print("Commands: visit <url>, back, forward, show, quit")

while True:
    command = input("\nEnter command: ").strip().lower()

    if command.startswith("visit "):
        url = command.split(" ", 1)[1]
        browser.visit(url)

    elif command == "back":
        browser.back()

    elif command == "forward":
        browser.forward()

    elif command == "show":
        browser.show_current()

    elif command == "quit":
        print("Exiting browser history simulation.")
        break

    else:
        print("Unknown command! Try again.")
