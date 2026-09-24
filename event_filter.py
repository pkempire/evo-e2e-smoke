"""Select events for an explicitly allowed list of string user IDs.

Inputs are ordinary lists; every event has a string user_id. Preserve event
order, repeated events, object identity and all other event fields. Neither
input may be modified. Duplicate allowed IDs have no additional effect.
"""


def select_events(events: list[dict], allowed_user_ids: list[str]) -> list[dict]:
    selected = []
    for event in events:
        if event['user_id'] in allowed_user_ids:
            selected.append(event)
    return selected
