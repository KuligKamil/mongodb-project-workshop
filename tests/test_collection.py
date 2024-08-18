import pytest

from src.models import User, Task


@pytest.mark.asyncio
async def test_inspect_status():
    for model in [User, Task]:
        inspected_collection = await model.inspect_collection()
        assert inspected_collection.status.value == "OK"
