import logging

from zoom_python_client.client_components.rooms.rooms_component import (
    RoomsListDict,
    RoomType,
)
from zoom_python_client.utils.logger import setup_logs
from zoom_python_client.zoom_api_client import ZoomApiClient

logger = setup_logs(log_level=logging.DEBUG)

zoom_client = ZoomApiClient.init_from_dotenv(use_path=".")

parameters = RoomsListDict(
    type=RoomType.ZOOM_ROOM,
)

result = zoom_client.rooms.get_rooms(parameters)

print(f"Found {len(result['rooms'])} rooms:")

for room in result["rooms"]:
    print(f"\t- {room['name']} - {room['room_id']} - {room['status']}")
