import json

def process_step(state_json, user_input):
    # Convert JSON to dict
    try:
        state = json.loads(state_json)
    except:
        state = {"room": "start"}

    room = state["room"]

    # Simple example rooms
    if room == "start":
        if user_input.lower() == "north":
            state["room"] = "forest"
            output = "You walk north into a dark forest."
        else:
            output = "You are in a small room. You can go NORTH."
    elif room == "forest":
        output = "Tall trees surround you. Type BACK to return."

        if user_input.lower() == "back":
            state["room"] = "start"
            output = "You return to the room."

    # Convert state back to JSON string
    new_state_json = json.dumps(state)
    return new_state_json, output
