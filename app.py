import os

from audit_engine import ThirdOrderAudit

API_KEY = os.getenv("OPENAI_API_KEY")

auditor = ThirdOrderAudit(API_KEY)

print("=== THIRD ORDER AUDIT ===")
print("Paste paper content.")
print("Type END on a new line when finished.\n")

lines = []

while True:
    line = input()

    if line.strip() == "END":
        break

    lines.append(line)

paper = "\n".join(lines)

result = auditor.audit(paper)

print("\n")
print(result)
