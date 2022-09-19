from urllib.parse import unquote_plus


def unquote(payload):
    unquoted_payload = unquote_plus(payload)
    return payload if unquoted_payload == payload else unquoted_payload


def remove_new_line(payload):
    return ' '.join(payload.strip().splitlines())


def remove_whitespace(payload):
    return ' '.join(payload.split())
