import ast


class CodeFeatureExtractor(ast.NodeVisitor):
    def __init__(self):

        # Loop features
        self.num_loops = 0
        self.current_loop_depth = 0
        self.max_loop_depth = 0
        self.num_if_statements = 0
        self.num_return_statements = 0
        self.assignment_operations = 0
        self.augmented_assignments = 0
        self.comparison_operations = 0

        # Function & recursion
        self.function_names = set()
        self.function_calls = []
        self.num_functions = 0
        self.recursive_call_count = 0

        # Data structures
        self.uses_list = 0
        self.uses_dict = 0
        self.uses_set = 0
        self.uses_append = 0
        self.uses_pop = 0

        # Subscript / DP / hashing
        self.uses_2d_list = 0
        self.uses_subscript_assignment = 0
        self.dict_subscript_usage = 0
        self.nested_subscript_usage = 0
        self.dict_update_count = 0
        self.membership_checks = 0

        # General
        self.uses_sorted = 0
        self.uses_range = 0
        self.uses_enumerate = 0

    # -------------------------
    # Loops
    # -------------------------
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

    # -------------------------
    # Functions
    # -------------------------
    def visit_FunctionDef(self, node):
        self.num_functions += 1
        self.function_names.add(node.name)
        self.generic_visit(node)

    def visit_Call(self, node):

        if isinstance(node.func, ast.Name):
            self.function_calls.append(node.func.id)

            if node.func.id == "sorted":
                self.uses_sorted = 1
            if node.func.id == "range":
                self.uses_range = 1
            if node.func.id == "enumerate":
                self.uses_enumerate = 1

        if isinstance(node.func, ast.Attribute):
            if node.func.attr == "append":
                self.uses_append = 1
            if node.func.attr == "pop":
                self.uses_pop = 1
            if node.func.attr == "update":
                self.dict_update_count += 1

        self.generic_visit(node)

    # -------------------------
    # Returns
    # -------------------------
    def visit_Return(self, node):
        self.num_return_statements += 1
        self.generic_visit(node)

    # -------------------------
    # Conditionals
    # -------------------------
    def visit_If(self, node):
        self.num_if_statements += 1
        self.generic_visit(node)

    def visit_Compare(self, node):
        self.comparison_operations += 1

        for op in node.ops:
            if isinstance(op, ast.In):
                self.membership_checks += 1

        self.generic_visit(node)

    # -------------------------
    # Assignments
    # -------------------------
    def visit_Assign(self, node):
        self.assignment_operations += 1

        for target in node.targets:
            if isinstance(target, ast.Subscript):
                self.uses_subscript_assignment = 1

        self.generic_visit(node)

    def visit_AugAssign(self, node):
        self.augmented_assignments += 1
        self.generic_visit(node)

    # -------------------------
    # Data Structures
    # -------------------------
    def visit_List(self, node):
        self.uses_list = 1
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

    def visit_Subscript(self, node):
        if isinstance(node.value, ast.Subscript):
            self.nested_subscript_usage += 1

        if isinstance(node.value, ast.Name):
            self.dict_subscript_usage += 1

        self.generic_visit(node)


def extract_features(code: str) -> dict:
    try:
        tree = ast.parse(code)
    except SyntaxError:
        raise ValueError("Invalid Python syntax")

    extractor = CodeFeatureExtractor()
    extractor.visit(tree)

    recursive_call_count = sum(
        1 for call in extractor.function_calls
        if call in extractor.function_names
    )

    has_recursion = int(recursive_call_count > 0)
    recursion_with_loop = int(has_recursion and extractor.num_loops > 0)

    return {
        # Loop features
        "num_loops": extractor.num_loops,
        "max_loop_depth": extractor.max_loop_depth,
        "num_if_statements": extractor.num_if_statements,
        "num_return_statements": extractor.num_return_statements,
        "assignment_operations": extractor.assignment_operations,
        "augmented_assignments": extractor.augmented_assignments,
        "comparison_operations": extractor.comparison_operations,

        # Recursion
        "has_recursion": has_recursion,
        "recursive_call_count": recursive_call_count,
        "recursion_with_loop": recursion_with_loop,

        # Data structures
        "uses_list": extractor.uses_list,
        "uses_dict": extractor.uses_dict,
        "uses_set": extractor.uses_set,
        "uses_append": extractor.uses_append,
        "uses_pop": extractor.uses_pop,

        # DP / hashing
        "uses_2d_list": extractor.uses_2d_list,
        "uses_subscript_assignment": extractor.uses_subscript_assignment,
        "dict_subscript_usage": extractor.dict_subscript_usage,
        "nested_subscript_usage": extractor.nested_subscript_usage,
        "dict_update_count": extractor.dict_update_count,
        "membership_checks": extractor.membership_checks,

        # General
        "uses_sorted": extractor.uses_sorted,
        "uses_range": extractor.uses_range,
        "uses_enumerate": extractor.uses_enumerate,
        "lines_of_code": len(code.splitlines()),
        "num_functions": extractor.num_functions,
    }