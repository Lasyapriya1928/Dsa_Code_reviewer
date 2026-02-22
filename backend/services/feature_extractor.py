import ast

class CodeFeatureExtractor(ast.NodeVisitor):
    def __init__(self):
        self.num_loops = 0
        self.current_loop_depth = 0
        self.max_loop_depth = 0
        self.function_names = set()
        self.function_calls = []
        self.uses_list = 0
        self.uses_dict = 0
        self.uses_set = 0
        self.num_functions = 0
        self.uses_append = 0
        self.uses_pop = 0

        # 🔥 NEW FEATURES
        self.uses_2d_list = 0
        self.uses_subscript_assignment = 0
        self.uses_sorted = 0
        self.num_if_statements = 0

    def visit_For(self, node):
        self.num_loops += 1
        self.current_loop_depth += 1
        self.max_loop_depth = max(self.max_loop_depth, self.current_loop_depth)
        self.generic_visit(node)
        self.current_loop_depth -= 1

    def visit_While(self, node):
        self.num_loops += 1
        self.current_loop_depth += 1
        self.max_loop_depth = max(self.max_loop_depth, self.current_loop_depth)
        self.generic_visit(node)
        self.current_loop_depth -= 1

    def visit_FunctionDef(self, node):
        self.num_functions += 1
        self.function_names.add(node.name)
        self.generic_visit(node)

    def visit_Call(self, node):
        # function calls
        if isinstance(node.func, ast.Name):
            self.function_calls.append(node.func.id)

            # detect sorted()
            if node.func.id == "sorted":
                self.uses_sorted = 1

        # detect append / pop
        if isinstance(node.func, ast.Attribute):
            if node.func.attr == "append":
                self.uses_append = 1
            if node.func.attr == "pop":
                self.uses_pop = 1

        self.generic_visit(node)

    def visit_List(self, node):
        self.uses_list = 1

        # 🔥 Detect nested list (possible 2D list)
        for elt in node.elts:
            if isinstance(elt, ast.List):
                self.uses_2d_list = 1

        self.generic_visit(node)

    def visit_Dict(self, node):
        self.uses_dict = 1
        self.generic_visit(node)

    def visit_Set(self, node):
        self.uses_set = 1
        self.generic_visit(node)

    # 🔥 Detect dp[i] = ...
    def visit_Assign(self, node):
        for target in node.targets:
            if isinstance(target, ast.Subscript):
                self.uses_subscript_assignment = 1
        self.generic_visit(node)

    # 🔥 Count if-statements
    def visit_If(self, node):
        self.num_if_statements += 1
        self.generic_visit(node)


def extract_features(code: str) -> dict:
    try:
        tree = ast.parse(code)
    except SyntaxError:
        raise ValueError("Invalid Python syntax")

    extractor = CodeFeatureExtractor()
    extractor.visit(tree)

    has_recursion = int(
        any(fn in extractor.function_calls for fn in extractor.function_names)
    )

    return {
        "num_loops": extractor.num_loops,
        "max_loop_depth": extractor.max_loop_depth,
        "has_recursion": has_recursion,
        "uses_list": extractor.uses_list,
        "uses_dict": extractor.uses_dict,
        "uses_set": extractor.uses_set,
        "lines_of_code": len(code.splitlines()),
        "num_functions": extractor.num_functions,
        "uses_append": extractor.uses_append,
        "uses_pop": extractor.uses_pop,

        # 🔥 NEW FEATURES
        "uses_2d_list": extractor.uses_2d_list,
        "uses_subscript_assignment": extractor.uses_subscript_assignment,
        "uses_sorted": extractor.uses_sorted,
        "num_if_statements": extractor.num_if_statements,
    }