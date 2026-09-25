"""Select events for an explicitly allowed list of string user IDs.

Inputs are ordinary lists; every event has a string user_id. Preserve event
order, repeated events, object identity and all other event fields. Neither
input may be modified. Duplicate allowed IDs have no additional effect.
"""


def select_events(events: list[dict], allowed_user_ids: list[str]) -> list[dict]:
    if type(events) is list and not events:
        return []

    allowed_users = allowed_user_ids
    if (type(events) is list and type(allowed_user_ids) is list
            and all(type(user_id) is str for user_id in allowed_user_ids)):
        allowed_users = set(allowed_user_ids)

    selected = []
    for event in events:
        # Custom mappings, keys or IDs can run callbacks that change the allowlist.
        # Permanently fall back to live list membership before invoking them.
        if allowed_users is not allowed_user_ids and (
                type(event) is not dict
                or any(type(key) is not str for key in event)):
            allowed_users = allowed_user_ids
        user_id = event['user_id']
        if type(user_id) is not str:
            allowed_users = allowed_user_ids
        if user_id in allowed_users:
            selected.append(event)
    return selected
