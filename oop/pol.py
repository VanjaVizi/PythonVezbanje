
from enum import Enum

class Pol(Enum):
    MUSKI = "Muški"
    ZENSKI = "Ženski"

    @staticmethod
    def valid_pol_str(string):
        # Pretvaranje unesenog stringa u mala slova radi case insensitive poređenja
        string_lower = string.lower()

        # Provera da li string odgovara nazivu ili vrednosti jedne od Pol instanci
        for pol in Pol:
            if string_lower == pol.name.lower() or string_lower == pol.value.lower():
                return True
        return False

print(Pol.valid_pol_str("Muški"))  # Output: True
print(Pol.valid_pol_str("ženski"))  # Output: True
print(Pol.valid_pol_str("MALE"))  # Output: True (case insensitive)
print(Pol.valid_pol_str("Drugo"))  # Output: False
#%%
