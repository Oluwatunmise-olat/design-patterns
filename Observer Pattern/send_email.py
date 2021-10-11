from core import inventory

def send_email_message(event: dict):
    print(f"Welcome user, {event['name'].title()} from mail service")

email = inventory.attach(event_type="message", observer=send_email_message)
