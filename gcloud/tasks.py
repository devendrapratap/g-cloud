from google.cloud import datastore
from . import events

datastore_client = datastore.Client('my-gcp-project')

def exists(task_id):
    key = datastore_client.key("tasks", task_id)

    entity = datastore_client.get(key)

    return entity is not None

def create(task):

    with datastore_client.transaction():
        key = datastore_client.key("tasks", task["id"])

        task.managerState = "Active"
        entity = {
            "key": key,
            "exclude_from_indexes": [
                "id", "data", "attributes"
            ],
            "data": task
        }

        datastore_client.put(entity)

def update_manager_state(task_id, state, percentage_complete):
    with datastore_client.transaction():
        key = datastore_client.key("tasks", task_id)

        results = datastore_client.get(key)
        results["managerState"] = state
        results["percentageComplete"] = percentage_complete

        datastore_client.put({
            "key": key, 
            "data": results
        })

        print("TaskId state updated to", state)

        events.send("tasks", task_id, "updated")

def run_manager(task, manager_method):
    if exists(task["id"]):
        print("TaskId exists already. No further action required.")
    else:
        create(task)
        print("TaskId", task["id"], "created")

        manager_method(task)
