import random
import argparse

libraries = ["Albany Village Library", "Avondale Library", "Birkenhead Library",
             "Blockhouse Bay Library", "Botany Library", "Central City Library",
             "Devonport Library", "East Coast Bays Library", "Epsom Library",
             "Glen Eden Library", "Glen Innes Library", "Glenfield Library",
             "Great Barrier Library", "Grey Lynn Library", "Helensville Library",
             "Heritage Collections Reading Room", "Highland Park Library",
             "Howick Library", "Kumeū Library", "Leys Institute Library (Ponsonby)",
             "Leys Institute Little Library", "Mahurangi East Library",
             "Māngere Bridge Library", "Māngere East Library", 
             "Māngere Town Centre Library", "Manukau Library", "Manurewa Library",
             "Mt Albert Library", "Mt Roskill Library", "New Lynn War Memorial Library", 
             "North Mobile Library", "Northcote Library", "Onehunga Library",
             "Ōrewa Library", "Ōtāhuhu Library", "Ōtara Library", "Pakuranga Library",
             "Panmure Library", "Papatoetoe War Memorial Library", "Parnell Library",
             "Pt Chevalier Library", "Pukekohe Library", "Rānui Library", 
             "Remuera Library", "Research Central", "Research South", "Rural libraries",
             "Sir Edmund Hillary Library (Papakura)", "South and East Mobile Library",
             "St Heliers Library", "Takaanini Library and Community Hub",
             "Takapuna Library", "Tamariki Mobile Library - Rodney", 
             "Te Atatū Peninsula Library", "Te Manawa (Westgate)", "Titirangi Library",
             "Tupu Youth Library", "Waiheke Library", "Waimāhia (Clendon)", 
             "Waitākere Central Library (Henderson)", "Waiuku Library", 
             "Warkworth War Memorial Library", "Wellsford War Memorial Library",
             "Whangaparāoa Library"]


def main():
    parser = argparse.ArgumentParser(
        description="Randomly pick Auckland libraries."
    )

    parser.add_argument(
        "-n", "--number",
        type=int,
        default=1,
        help="How many libraries to pick (default: 1)."
    )

    parser.add_argument(
        "-a", "--all",
        action="store_true",
        help="Show all libraries instead of picking randomly."
    )

    args = parser.parse_args()

    if args.all:
        print("All available libraries:")
        for lib in libraries:
            print(" -", lib)
    else:
        selected = random.sample(libraries, k=min(args.number, len(libraries)))
        print("Selected library/libraries:")
        for lib in selected:
            print(" -", lib)

if __name__ == "__main__":
    main()