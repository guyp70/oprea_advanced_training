from datetime import datetime
from pathlib import Path
from typing import List


class Terrorist:
    def __init__(self, first_name: str, last_name: str, date_of_birth: datetime, organization: str):
        """
        Initialize `Terrorist` with all attributes as inputs.

        :param first_name: The terrorist's first name.
        :param last_name: The terrorist's last name.
        :param date_of_birth: The terrorist's date of birth.
        :param organization: The organization the terrorist is a part of.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.organization = organization

    def __repr__(self) -> str:
        return (
            f'Terrorist {self.first_name} {self.last_name} of {self.organization}, born on {self.date_of_birth}'
        )


def add_terrorist_sighting(terrorists: List[Terrorist], path: Path) -> None:
    """
    Log a terrorist sighting to a file, including the number of terrorists spotted and the attributes of each terrorist.

    :param terrorists: A list of all of the terrorists that were spotted.
    :param path: The path to an existing file where the sighting will be logged.
    :return: None.
    """
    with open(str(path), 'a') as f:
        f.write(f'Spotted {len(terrorists)} terrorists:\n')
        for terrorists in terrorists:
            f.write(f'{repr(terrorists)}\n')
