# Rego Märk
# Harjutused 14,13,7,6,5




# Harjutus 13

# arv = int(input("Sisesta arv: "))

# if arv % 2 == 0:
#     print(f"{arv} on paaris arv")
# else:
#     print(f"{arv} on paaritu arv")
# if arv ==0:
#     print(f"{arv} Null on null")


# Harjutus 6

# arv = int(input("Sisesta arv: "))

# if arv % 2 == 0:
#     print(f"{arv} on paaris arv")
# else:
#     print(f"{arv} on paaritu arv")
# if arv ==0:
#     print(f"{arv} Null on null")


# Harjutus 5

def shopping_list():
    items = []

    print("Sisesta toode (Vajuta enter et lõpetada):")
    
    while True:
        item = input("> ")
        if item: 
            items.append(item)
        else:
            break

    print("\nSinu poe nimekiri:")
    for idx, item in enumerate(items, 1):
        print(f"{idx}. {item}")

if __name__ == "__main__":
     shopping_list()