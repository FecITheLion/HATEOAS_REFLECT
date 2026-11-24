import ast
from typing import Any


def serialize_function(func_def: ast.FunctionDef) -> str:
    """Convert an ast.FunctionDef node into a serialized AST string."""
    return ast.dump(func_def)


def deserialize_ast_node(serialized_ast: str) -> ast.AST:
    """Reconstruct a live AST node from an ast.dump() string."""
    expr_ast = ast.parse(serialized_ast, mode="eval")
    node = eval(compile(expr_ast, filename="<serialized-ast>", mode="eval"), {"ast": ast})
    if not isinstance(node, ast.AST):
        raise TypeError(f"Expected ast.AST instance, got {type(node).__name__}")
    return ast.fix_missing_locations(node)


def _find_called_names(node: ast.AST) -> set[str]:
    """Find direct function names called inside an AST node."""
    called: set[str] = set()
    for sub in ast.walk(node):
        if isinstance(sub, ast.Call) and isinstance(sub.func, ast.Name):
            called.add(sub.func.id)
    return called


def define_function_from_ast(
    name: str,
    serialized_ast: str,
    namespace: dict[str, Any],
) -> Any:
    """Compile serialized AST `name` into a live `def <name>(...)` inside `namespace`."""
    node = deserialize_ast_node(serialized_ast)
    if not isinstance(node, ast.FunctionDef):
        raise ValueError(f"AST entry '{name}' is not an ast.FunctionDef")

    node.name = name
    module = ast.Module(body=[node], type_ignores=[])
    ast.fix_missing_locations(module)

    exec(compile(module, filename=f"<ast:{name}>", mode="exec"), namespace)
    return namespace[name]


class ASTProgram:
    """
    Holds a serialized AST registry (`list1`) and automatically compiles
    the entrypoint + only the AST functions it depends on inside `__init__`,
    attaching them directly so you can call `program.entrypoint(...)`.
    """

    def __init__(self, registry: dict[str, str], entrypoint_key: str = "entrypoint") -> None:
        self.registry = registry
        self.entrypoint_key = entrypoint_key
        self.runtime_ns: dict[str, Any] = {"__builtins__": __builtins__}
        self._compiled: set[str] = set()

        # Automatically compile needed functions + entrypoint during construction
        self._compile_needed(entrypoint_key)

    def _compile_needed(self, key: str) -> Any:
        if key in self._compiled:
            return self.runtime_ns[key]
        if key not in self.registry:
            raise KeyError(f"'{key}' not found in AST registry")

        node = deserialize_ast_node(self.registry[key])

        # Recursively compile only referenced functions in the registry first
        for dep_name in _find_called_names(node):
            if dep_name in self.registry and dep_name != key:
                self._compile_needed(dep_name)

        fn = define_function_from_ast(key, self.registry[key], self.runtime_ns)
        self._compiled.add(key)

        # Attach each dynamically defined function onto `self` (e.g., self.ast1, self.entrypoint)
        setattr(self, key, staticmethod(fn).__get__(self, type(self)))
        return fn

    def __init_subclass__(
        cls,
        registry: dict[str, str] | None = None,
        entrypoint_key: str = "entrypoint",
        **kwargs: Any,
    ) -> None:
        """
        Allows calling `MyProgram.entrypoint(n=3)` directly on the class without instantiating.
        """
        super().__init_subclass__(**kwargs)
        if registry is None:
            return

        instance = cls(registry=registry, entrypoint_key=entrypoint_key)
        cls.runtime_ns = instance.runtime_ns
        for fn_name in instance._compiled:
            setattr(cls, fn_name, staticmethod(instance.runtime_ns[fn_name]))


# ---------------------------------------------------------------------------
# Serialized AST Registry (`list1`)
# ---------------------------------------------------------------------------
def _fn_ast_str(source: str) -> str:
    fn = ast.parse(source).body[0]
    assert isinstance(fn, ast.FunctionDef)
    return serialize_function(fn)


list1: dict[str, str] = {
    "ast1": _fn_ast_str(
        """
def helper_one(x):
    return x * 2 + 1
"""
    ),
    "ast2": _fn_ast_str(
        """
def helper_two(y):
    return ast1(y) ** 2
"""
    ),
    "unused_ast": _fn_ast_str(
        """
def never_needed(z):
    return z - 999
"""
    ),
    "entrypoint": _fn_ast_str(
        """
def entrypoint(n):
    return ast2(n) + 10
"""
    ),
}


# Subclass automatically compiles `list1` at class creation time
class MyASTApp(ASTProgram, registry=list1, entrypoint_key="entrypoint"):
    pass


if __name__ == "__main__":
    # Option A: Class-level call directly (`MyASTApp.entrypoint(n=3)`)
    print("Class call MyASTApp.entrypoint(n=3) ->", MyASTApp.entrypoint(n=3))
    print("Compiled functions:", [k for k in MyASTApp.runtime_ns if k != "__builtins__"])

    # Option B: Instance constructor (`app = ASTProgram(list1)` -> `app.entrypoint(n=3)`)
    app = ASTProgram(list1)
    print("Instance call app.entrypoint(n=3)  ->", app.entrypoint(n=3))
