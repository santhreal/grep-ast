from tree_sitter_languages import get_parser

from grep_ast.dump import dump  # noqa: F401
from grep_ast.parsers import PARSERS, filename_to_lang
from grep_ast.tsl import get_parser as get_pack_parser


def test_get_parser_for_all_parsers():
    for lang in PARSERS.values():
        assert get_parser(lang) is not None


def test_filename_to_lang_tsx_uses_tsx_grammar():
    lang = filename_to_lang("App.tsx")
    assert lang == "tsx"
    tree = get_pack_parser(lang).parse(b"const x = <div/>;")
    assert tree.root_node.has_error is False
