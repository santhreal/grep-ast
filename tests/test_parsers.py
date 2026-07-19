from tree_sitter_languages import get_parser

from grep_ast.dump import dump  # noqa: F401
from grep_ast.parsers import PARSERS, filename_to_lang


def test_get_parser_for_all_parsers():
    for lang in PARSERS.values():
        assert get_parser(lang) is not None


def test_filename_to_lang_dot_extension():
    assert filename_to_lang("g.dot") == "dot"

