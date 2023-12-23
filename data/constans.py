from dataclasses import dataclass


@dataclass
class ErrorValidationMsg:
    CITY_VALIDATION = "Please provide a valid city."
    STATE_VALIDATION = "Please provide a valid state."
    ZIP_VALIDATION = "Please provide a valid zip."
    AGREEMENT_VALIDATION = "You must agree before submitting."


class FileCheck:
    FOLDER = 'Downloads'
    FILE_NAME = "sample_text.txt"
    ADDITIONAL_FILE = "sample_text (1).txt"
