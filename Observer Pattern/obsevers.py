from core import inventory

def send_slack_message(event: dict):
    print(f"Welcome user, {event['name'].title()} from slack service")

receiver = inventory.attach(event_type="message", observer=send_slack_message)
