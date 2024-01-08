from steam import fetch_steam_discounts
from epic import fetch_epic_discounts
from data_handler import save_data, load_data
from notifications import send_notifications

def main():
    # Fetch discount data from Steam and Epic Games Store
    steam_discounts = fetch_steam_discounts()
    epic_discounts = fetch_epic_discounts()

    # Save the fetched data
    save_data(steam_discounts, 'steam')
    save_data(epic_discounts, 'epic')

    # Load the saved data (if needed for further processing)
    steam_data = load_data('steam')
    epic_data = load_data('epic')

    # Send notifications to the user about new discounts
    send_notifications(steam_data, epic_data)

if __name__ == "__main__":
    main()