from view.View import View


class Main:
    def __init__(self):
        self._view = View()

    def run(self):
        self._view.print_suspended_licenses()
        self._view.print_valid_licenses()
        self._view.print_licenses_by_category()


if __name__ == "__main__":
    Main().run()
        
