# homework 1
# Define Task Class
class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.is_complete = False

    def mark_complete(self):
        self.is_complete = True

    def __str__(self):
        status = "Complete" if self.is_complete else "Incomplete"
        return f"Title: {self.title}\nDescription: {self.description}\nDue Date: {self.due_date}\nStatus: {status}\n"


# Define ToDoList Class
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()
            print(f"Task '{self.tasks[index].title}' marked as complete.")
        else:
            print("Invalid task number.")

    def list_all_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for i, task in enumerate(self.tasks):
                print(f"Task {i + 1}:\n{task}")

    def list_incomplete_tasks(self):
        incomplete_tasks = [task for task in self.tasks if not task.is_complete]
        if not incomplete_tasks:
            print("All tasks are complete!")
        else:
            for i, task in enumerate(incomplete_tasks):
                print(f"Incomplete Task {i + 1}:\n{task}")


# Main Program
def main():
    todo_list = ToDoList()

    while True:
        print("\n--- ToDo List Menu ---")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. List All Tasks")
        print("4. List Incomplete Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter task due date (YYYY-MM-DD): ")
            task = Task(title, description, due_date)
            todo_list.add_task(task)
            print("Task added successfully.")

        elif choice == '2':
            todo_list.list_all_tasks()
            try:
                index = int(input("Enter the task number to mark as complete: ")) - 1
                todo_list.mark_task_complete(index)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '3':
            todo_list.list_all_tasks()

        elif choice == '4':
            todo_list.list_incomplete_tasks()

        elif choice == '5':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select between 1 and 5.")


# Run the program
if __name__ == "__main__":
    main()

# homework 2
# Define Post Class
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nContent: {self.content}\n"


# Define Blog Class
class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)
        print(f"Post '{post.title}' added successfully!")

    def list_all_posts(self):
        if not self.posts:
            print("No posts available.")
        else:
            for i, post in enumerate(self.posts):
                print(f"\nPost {i + 1}:\n{post}")

    def display_posts_by_author(self, author_name):
        filtered_posts = [post for post in self.posts if post.author.lower() == author_name.lower()]
        if not filtered_posts:
            print(f"No posts found by author: {author_name}")
        else:
            for post in filtered_posts:
                print(post)

    def delete_post(self, index):
        if 0 <= index < len(self.posts):
            removed_post = self.posts.pop(index)
            print(f"Post '{removed_post.title}' deleted successfully!")
        else:
            print("Invalid post number.")

    def edit_post(self, index, new_title=None, new_content=None):
        if 0 <= index < len(self.posts):
            if new_title:
                self.posts[index].title = new_title
            if new_content:
                self.posts[index].content = new_content
            print("Post updated successfully!")
        else:
            print("Invalid post number.")

    def display_latest_posts(self, n):
        latest_posts = self.posts[-n:]
        if not latest_posts:
            print("No posts available.")
        else:
            for post in reversed(latest_posts):
                print(post)


# Main Program
def main():
    blog = Blog()

    while True:
        print("\n--- Blog System Menu ---")
        print("1. Add Post")
        print("2. List All Posts")
        print("3. Display Posts by Author")
        print("4. Delete a Post")
        print("5. Edit a Post")
        print("6. Display Latest Posts")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            title = input("Enter post title: ")
            content = input("Enter post content: ")
            author = input("Enter author name: ")
            post = Post(title, content, author)
            blog.add_post(post)

        elif choice == '2':
            blog.list_all_posts()

        elif choice == '3':
            author_name = input("Enter author name to search: ")
            blog.display_posts_by_author(author_name)

        elif choice == '4':
            blog.list_all_posts()
            try:
                index = int(input("Enter post number to delete: ")) - 1
                blog.delete_post(index)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '5':
            blog.list_all_posts()
            try:
                index = int(input("Enter post number to edit: ")) - 1
                new_title = input("Enter new title (leave blank to keep current): ")
                new_content = input("Enter new content (leave blank to keep current): ")
                blog.edit_post(index, new_title or None, new_content or None)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '6':
            try:
                n = int(input("Enter number of latest posts to display: "))
                blog.display_latest_posts(n)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '7':
            print("Exiting Blog System. Goodbye!")
            break

        else:
            print("Invalid choice. Please select between 1 and 7.")


# Run the program
if __name__ == "__main__":
    main()

# homework 3
# Define Account Class
class Account:
    def __init__(self, account_number, holder_name, balance=0.0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f} successfully.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance! Withdrawal failed.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f} successfully.")

    def __str__(self):
        return f"Account Number: {self.account_number}\nHolder Name: {self.holder_name}\nBalance: ${self.balance:.2f}"

    def transfer(self, target_account, amount):
        if amount > self.balance:
            print("Transfer failed! Insufficient balance.")
        elif amount <= 0:
            print("Transfer amount must be positive.")
        else:
            self.withdraw(amount)
            target_account.deposit(amount)
            print(f"Transferred ${amount:.2f} to Account {target_account.account_number}.")


# Define Bank Class
class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)
        print(f"Account for {account.holder_name} added successfully.")

    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def display_all_accounts(self):
        if not self.accounts:
            print("No accounts available.")
        else:
            for account in self.accounts:
                print("\n" + str(account))


# Main Program
def main():
    bank = Bank()

    while True:
        print("\n--- Banking System Menu ---")
        print("1. Add Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Transfer Money")
        print("6. Display All Account Details")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            account_number = input("Enter account number: ")
            holder_name = input("Enter account holder name: ")
            try:
                initial_balance = float(input("Enter initial deposit amount: "))
                account = Account(account_number, holder_name, initial_balance)
                bank.add_account(account)
            except ValueError:
                print("Invalid amount. Account creation failed.")

        elif choice == '2':
            account_number = input("Enter account number: ")
            account = bank.find_account(account_number)
            if account:
                print(f"Current Balance: ${account.balance:.2f}")
            else:
                print("Account not found.")

        elif choice == '3':
            account_number = input("Enter account number: ")
            account = bank.find_account(account_number)
            if account:
                try:
                    amount = float(input("Enter deposit amount: "))
                    account.deposit(amount)
                except ValueError:
                    print("Invalid amount.")
            else:
                print("Account not found.")

        elif choice == '4':
            account_number = input("Enter account number: ")
            account = bank.find_account(account_number)
            if account:
                try:
                    amount = float(input("Enter withdrawal amount: "))
                    account.withdraw(amount)
                except ValueError:
                    print("Invalid amount.")
            else:
                print("Account not found.")

        elif choice == '5':
            sender_account_number = input("Enter your account number: ")
            receiver_account_number = input("Enter receiver's account number: ")

            sender = bank.find_account(sender_account_number)
            receiver = bank.find_account(receiver_account_number)

            if sender and receiver:
                try:
                    amount = float(input("Enter amount to transfer: "))
                    sender.transfer(receiver, amount)
                except ValueError:
                    print("Invalid amount.")
            else:
                print("One or both accounts not found.")

        elif choice == '6':
            bank.display_all_accounts()

        elif choice == '7':
            print("Exiting Banking System. Goodbye!")
            break

        else:
            print("Invalid choice. Please select between 1 and 7.")


# Run the program
if __name__ == "__main__":
    main()
