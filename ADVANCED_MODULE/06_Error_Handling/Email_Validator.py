import re
from typing import Dict


class NameTooShortError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__("Name must be more than 4 characters")


class MustContainAtSymbol(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__("Email must contain @")


class InvalidDomainError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__("Domain must be one of the following: .com, .bg, .org, .net")


email_regex_string: str = (
    r"^(?P<User>[\w\d\_\-\.]+)(?P<AtSign>@?)(?P<Hostname>\w+)(?P<Domain>\.\w+)$"
)

email_regex = re.compile(email_regex_string, flags=re.IGNORECASE)


def main() -> None:
    while (email := input()) != "End":
        reg_res: Dict[str, str] = email_regex.match(email).groupdict()
        if not reg_res["Domain"] in (
            ".com",
            ".bg",
            ".org",
            ".net",
        ):
            raise InvalidDomainError
        elif reg_res["AtSign"] != "@":
            raise MustContainAtSymbol
        elif len(reg_res["User"]) < 5:
            raise NameTooShortError
        else:
            print("Email is valid")


if __name__ == "__main__":
    main()
