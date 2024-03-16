from view.View import View


class Main:
    def __init__(self):
        self._view = View()

    def run(self):
        while True:
            self._view.display_menu()
            option = input("Enter your choice: ")
            self._view.execute_function(option)
            if option == "0":
                break

if __name__ == "__main__":
    Main().run()

        
