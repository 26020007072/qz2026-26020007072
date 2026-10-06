import json
def analyze_log(filepath):
    result = {"total": 0,"by_level":{},"by_user":{},"last_error":None}
    try:
        f = open(filepath,"r",encoding="utf-8")
    except FileNotFoundError:
        return result
    with f:
        for line in f:

            try:
                file = json.load(line)
            except json.JSONDecodeError:
                continue

            result["total"] += 1

            level = file["level"]
            if level in result["by_level"]:
                result["by_level"][level] = result["by_level"][level] + 1
            else:
                result["by_level"][level] = 1

            user = file["user"]
            if user in result["by_user"]:
                result["by_user"][user] = result["by_user"][user] + 1
            else:
                result["by_user"][user] = 1
            if level == "ERROR":
                result["last_error"] = file["message"]

    