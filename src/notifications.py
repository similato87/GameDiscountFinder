# notifications.py
from plyer import notification

def send_notifications(discounts):
    """
    Send a desktop notification to the user about new discounts.
    :param discounts: A list of dictionaries with discount details
    """
    for discount in discounts:
        # You might want to format this message in a more informative way
        title = f"Discount on {discount['name']}"
        message = f"{discount['name']} is now {discount['discount_percent']}% off! Final price: {discount['final_price']}"

        # Sending the notification
        notification.notify(
            title=title,
            message=message,
            app_name='Game Discount Finder'
        )
