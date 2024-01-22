import pytest
from word_generator.types import InsertedData
from pydantic_core._pydantic_core import ValidationError


def test_simple():
    data = InsertedData(
        key="key",
        category="image",
        value="some"
    )
    assert data


def test_category_values():
    assert InsertedData(
        key="key",
        category="image",
        value="some"
    )
    assert InsertedData(
        key="key",
        category="text",
        value="some"
    )
    with pytest.raises(ValidationError):
        InsertedData(
            key="key",
            category="test",
            value="some"
        )
