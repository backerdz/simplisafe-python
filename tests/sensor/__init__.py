"""Define tests for sensors."""
import aiohttp
import pytest

from simplipy import get_api
from simplipy.entity import EntityTypes

from tests.common import TEST_EMAIL, TEST_PASSWORD, TEST_SYSTEM_ID


async def test_properties_base(v2_server):
    """Test that base sensor properties are created properly."""
    async with v2_server:
        async with aiohttp.ClientSession() as session:
            simplisafe = await get_api(TEST_EMAIL, TEST_PASSWORD, session)
            systems = await simplisafe.get_systems()
            system = systems[TEST_SYSTEM_ID]

            sensor = system.sensors["195"]
            assert sensor.name == "Garage Keypad"
            assert sensor.serial == "195"
            assert sensor.type == EntityTypes.keypad
