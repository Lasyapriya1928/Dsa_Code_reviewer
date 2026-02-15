from backend.analyzer import analyze_code
from backend.database import init_db

# Initialize database once
init_db()

sample_code = """
def example(n):
    for i in range(n):
        for j in range(n):
            print(i, j)
"""

result = analyze_code(sample_code, "Test Problem")

print(result)
