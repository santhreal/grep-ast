from grep_ast.grep_ast import TreeContext


def test_verbose_empty_file_constructs():
    tc = TreeContext("empty.py", "", verbose=True)
    assert tc.lines == []
    assert tc.num_lines == 1
    assert tc.grep("x", False) == set()
    tc.add_context()
    assert tc.format() == ""


def test_verbose_whitespace_only_file_constructs():
    tc = TreeContext("ws.py", "   ", verbose=True)
    assert tc.lines == ["   "]
    assert tc.grep("x", False) == set()


def test_verbose_newline_only_file_constructs():
    # tree-sitter reports the module node on row 1, past splitlines()' single "".
    tc = TreeContext("nl.py", "\n", verbose=True)
    assert tc.lines == [""]
    assert tc.num_lines == 2
    assert tc.grep("x", False) == set()


def test_verbose_normal_file_still_greps():
    code = "def foo():\n    return 1\n"
    tc = TreeContext("good.py", code, verbose=True)
    assert tc.grep("foo", False) == {0}
    tc.add_lines_of_interest({0})
    tc.add_context()
    out = tc.format()
    assert "foo" in out
    assert "return 1" in out
