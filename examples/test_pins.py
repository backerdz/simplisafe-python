"""Run an example script to interact with locks."""
import asyncio
import logging

from aiohttp import ClientSession

from simplipy import get_api
from simplipy.errors import SimplipyError

_LOGGER = logging.getLogger()

SIMPLISAFE_CLIENT_ID = "<CLIENT ID>"
SIMPLISAFE_EMAIL = "<EMAIL>"  # nosec
SIMPLISAFE_PASSWORD = "<PASSWORD>"  # nosec


async def main() -> None:
    """Create the aiohttp session and run the example."""
    async with ClientSession() as session:
        logging.basicConfig(level=logging.DEBUG)

        try:
            simplisafe = await get_api(
                SIMPLISAFE_EMAIL,
                SIMPLISAFE_PASSWORD,
                client_id=SIMPLISAFE_CLIENT_ID,
                session=session,
            )
            systems = await simplisafe.get_systems()
            for system in systems.values():
                await system.set_pin("Test PIN", "1235")
                await asyncio.sleep(3)
                await system.remove_pin("Test PIN")
        except SimplipyError as err:
            _LOGGER.error(err)


asyncio.run(main())
