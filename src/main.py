# main.py
from steam import fetch_steam_discounts
from epic import fetch_epic_discounts
from data_handler import save_data, load_data
from notifications import send_notifications


def main():
    steam_discounts = fetch_steam_discounts()
    epic_discounts = fetch_epic_discounts()

    all_discounts = [steam_discounts, epic_discounts]

    save_data(all_discounts)
    send_notifications(all_discounts)


if __name__ == "__main__":
    main()
