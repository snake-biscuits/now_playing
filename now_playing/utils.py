def sanitise_str(unsafe: str) -> str:
    allowed = "._-"
    return "".join(x for x in unsafe if x.isalnum() or x in allowed)
