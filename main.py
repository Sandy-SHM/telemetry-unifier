from datetime import datetime

# Convert telemetry data from format 1 into the required unified format
def convertFromFormat1(jsonObject):
    result = {
        "deviceID": jsonObject["deviceID"],
        "deviceType": jsonObject["deviceType"],
        "timestamp": jsonObject["timestamp"],

        # Split location string into separate fields
        "location": {
            "country": jsonObject["location"].split("/")[0],
            "city": jsonObject["location"].split("/")[1],
            "area": jsonObject["location"].split("/")[2],
            "factory": jsonObject["location"].split("/")[3],
            "section": jsonObject["location"].split("/")[4]
        },

        # Map machine status and temperature into data section
        "data": {
            "status": jsonObject["operationStatus"],
            "temperature": jsonObject["temp"]
        }
    }
    return result


# Convert telemetry data from format 2 into the required unified format
def convertFromFormat2(jsonObject):

    # Convert ISO timestamp into milliseconds since epoch
    iso_time = jsonObject["timestamp"]
    dt = datetime.fromisoformat(iso_time.replace("Z", "+00:00"))
    millis = int(dt.timestamp() * 1000)

    result = {
        "deviceID": jsonObject["device"]["id"],
        "deviceType": jsonObject["device"]["type"],
        "timestamp": millis,

        # Create location object from separate fields
        "location": {
            "country": jsonObject["country"],
            "city": jsonObject["city"],
            "area": jsonObject["area"],
            "factory": jsonObject["factory"],
            "section": jsonObject["section"]
        },

        # Copy status and temperature data
        "data": {
            "status": jsonObject["data"]["status"],
            "temperature": jsonObject["data"]["temperature"]
        }
    }

    return result