from itertools import cycle
from colorama import init, Fore, Back, Style
from shutil import get_terminal_size
from threading import Thread
from time import sleep


class LoadingSpinner:
    def __init__(self, desc: str = "Loading...", end: str = "Done!", timeout: int = 0.1) -> None:
        self.desc = desc
        self.end  = end
        self.timeout = timeout
        self._thread = Thread(target=self._animate, daemon=True)
        # self.steps = ["◐ ", "◓ ", "◑ ", "◒ "]
        self.steps = [
            f"{Style.BRIGHT}{Back.RED    }{Fore.WHITE}⢿{Style.RESET_ALL}  ",
            f"{Style.BRIGHT}{Back.GREEN  }{Fore.WHITE}⣻{Style.RESET_ALL}  ",
            f"{Style.BRIGHT}{Back.YELLOW }{Fore.WHITE}⣽{Style.RESET_ALL}  ",
            f"{Style.BRIGHT}{Back.BLUE   }{Fore.WHITE}⣾{Style.RESET_ALL}  ",
            f"{Style.BRIGHT}{Back.MAGENTA}{Fore.WHITE}⣷{Style.RESET_ALL}  ",
            f"{Style.BRIGHT}{Back.CYAN   }{Fore.WHITE}⣯{Style.RESET_ALL}  ",
            f"{Style.BRIGHT}{Back.RED    }{Fore.WHITE}⣟{Style.RESET_ALL}  ",
            f"{Style.BRIGHT}{Back.GREEN  }{Fore.WHITE}⡿{Style.RESET_ALL}  "
        ]
        self.done  = False

    def start(self):
        self._thread.start()
        return self

    def _animate(self):
        for c in cycle(self.steps):
            if self.done:
                break
            print(f"\r{self.desc} {c}", flush=True, end="")
            sleep(self.timeout)

    def __enter__(self):
        self.start()

    def stop(self):
        self.done = True
        cols = get_terminal_size((80, 20)).columns
        print("\r" + " " * cols, end="", flush=True)
        print(f"{self.desc} {self.end}")

    def __exit__(self, exc_type, exc_value, tb):
        # handle exceptions with those variables ^
        self.stop()
