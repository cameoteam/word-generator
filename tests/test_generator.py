import pytest
from word_generator import WordManager
from word_generator.types import InsertedData
import pathlib
from .utils import is_similar_word_files


class TestInit:
    def test_simple(self):
        path = (
            pathlib
            .Path(__file__)
            .parent
            .resolve()
            .joinpath("data", "simple.docx")
        )
        assert WordManager(path)

    def test_path(self):
        path = (
            pathlib
            .Path(__file__)
            .parent
            .resolve()
            .joinpath("data", "some.docx")
        )
        with pytest.raises(FileNotFoundError):
            assert WordManager(path)


class TestFileGeneration:
    template_path = (
        pathlib
        .Path(__file__)
        .parent
        .resolve()
        .joinpath("data", "simple.docx")
    )
    test_path = (
        pathlib
        .Path(__file__)
        .parent
        .resolve()
        .joinpath("data", "simple_test.docx")
    )
    result_path = (
        pathlib
        .Path(__file__)
        .parent
        .resolve()
        .joinpath("result_data", "simple.docx")
    )
    manager = WordManager(template_path)

    def test_insert_value(self):
        data = InsertedData(
            key="phone",
            category="text",
            value="some value",
        )
        self.manager.insert_value(data)
        self.manager.save(
            self.test_path
        )
        assert is_similar_word_files(
            self.test_path,
            self.result_path,
        )

    def test_insert_values(self):
        data = [
            InsertedData(
                key="phone",
                category="text",
                value="some value",
            ),
            InsertedData(
                key="website",
                category="text",
                value="some value",
            ),
        ]
        self.manager.insert_values(data)
        self.manager.save(
            self.test_path
        )
        assert is_similar_word_files(
            self.test_path,
            pathlib
            .Path(__file__)
            .parent
            .resolve()
            .joinpath("result_data", "simple1.docx"),
        )
