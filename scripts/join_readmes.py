import os

# TODO: move assets files from tutorial directory to main directory folder assets
order = (
    "basic_readme",
    "introduction",
    "why_mongodb",
    "python_mongodb_tools",
    "project_setup",
    "mongodb_atlas",
    "connection_to_db",
    "data_structure",
    "crud_queries",
    "data_generators",
    "tests",
    "resources",
)

project_directory = os.getcwd()
new_line = "\n"
if os.path.exists(f"{project_directory}/README.md"):
    os.remove(f"{project_directory}/README.md")
for index, tutorial_chapter in enumerate(order):
    temp_text = ""
    with open(
        os.path.join(f"{project_directory}/tutorial/{tutorial_chapter}", "README.md")
    ) as f:
        temp_text = f.read()
    with open(f"{project_directory}/README.md", "a") as f:
        f.write(f"{ new_line * 2 if index > 0 else ''}{temp_text}")
