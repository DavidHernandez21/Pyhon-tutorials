import yaml

from lettere_a_numeri.helper_functions import converted_numbers_joined

# import re

with open("config.yaml", "r") as f:
    config_pattern = yaml.safe_load(f)

# pickle_pattern_attached, pickle_pattern_200_900, pickle_pattern_nta_nti, pickle_main_pattern = _pickled_objects_for_matching("config.yaml")

# phrase = "dsdsa ottoseicentodue90novantaquattro7ottantaduetreottanta9 cinque due otto duecento cento novantatre 5-0/5_9-2"
# phrase = "settecentoquattordici novecento seicentonovantanove67 zero+"


def main():
    phrase = (
        "il mio codice conto è seicentonovantadue5novantaquattro7ottantadueottantadue9"
    )
    # phrase = "uno"
    conv = converted_numbers_joined(
        file_path="config.yaml", phrase=phrase, findall=True
    )

    print(conv)
    print(len(conv))


if __name__ == "__main__":
    main()
