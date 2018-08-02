from google.cloud import pubsub as PubSub

def send(_type, id, action):
    
    pubsub = PubSub.PublisherClient()
    topic_name = "events-v1"

    attributes = {
        "type": _type,
        "id": id,
        "action": action
    }

    data = b"{}"

    return pubsub.publish(topic_name, data, **attributes)
