import time
import random
from colorama import Fore, Style, init

# Инициализация colorama
init(autoreset=True)

# Список доступных цветов
colors = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.MAGENTA, Fore.CYAN]

# Текст для вывода
text = "С Наступающим Новым Годом!"

# Печать текста как гирлянды
while True:
    colorful_text = "".join(random.choice(colors) + char for char in text)
    print(f"\r{colorful_text}", end="")
    time.sleep(0.1)  # Задержка для обновления
