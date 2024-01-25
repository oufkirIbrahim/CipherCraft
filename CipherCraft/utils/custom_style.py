from colorama import Fore, Style


def success(message):
    """Return a success-styled message."""
    return f"{Fore.GREEN}{Style.BRIGHT}[SUCCESS] {message}{Style.RESET_ALL}"


def notice(message):
    """Return a notice-styled message."""
    return f"{Fore.YELLOW}{Style.BRIGHT}[NOTICE] {message}{Style.RESET_ALL}"


def message(message):
    """Return a notice-styled message."""
    return f"{Fore.LIGHTBLUE_EX}{Style.BRIGHT}{message}{Style.RESET_ALL}"


def comment(message):
    """Return a notice-styled message."""
    return f"{Fore.MAGENTA}{Style.BRIGHT}[SYNTAX] {message}{Style.RESET_ALL}"


def warning(message):
    """Return a warning-styled message."""
    return f"{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}[WARNING] {message}{Style.RESET_ALL}"


def error(message):
    """Return an error-styled message."""
    return f"{Fore.RED}{Style.BRIGHT}[ERROR] {message}{Style.RESET_ALL}"