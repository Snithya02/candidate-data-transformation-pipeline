import re
import pandas as pd
import re


def normalize_phone(phone):

    if pd.isna(phone):
        return ""

    digits = re.sub(r"\D", "", str(phone))

    if digits.startswith("91") and len(digits) > 10:
        digits = digits[2:]

    if len(digits) == 10:
        return f"+91 {digits[:5]} {digits[5:]}"

    return ""