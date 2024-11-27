import os

def generate_config_files():
    """
    Generates configuration files in different formats for testing.
    Cleans up existing files before regenerating.
    """
    config_files = {
        "config.ini": """\
[Database]
host = localhost
port = 5432
user = admin
password = secret

[API]
key = abc123
secret = xyz789
""",
        "config.json": """\
{
    "Database": {
        "host": "localhost",
        "port": 5432,
        "user": "admin",
        "password": "secret"
    },
    "API": {
        "key": "abc123",
        "secret": "xyz789"
    }
}
""",
        "config.yaml": """\
Database:
  host: localhost
  port: 5432
  user: admin
  password: secret

API:
  key: abc123
  secret: xyz789
""",
        "config.properties": """\
Database.host=localhost
Database.port=5432
Database.user=admin
Database.password=secret
API.key=abc123
API.secret=xyz789
""",
        "config.txt": """\
This is a plain text configuration file.
It contains no specific structure.
"""
    }

    # Clean up existing files
    for filename in config_files.keys():
        if os.path.exists(filename):
            os.remove(filename)
            print(f"Deleted {filename}")

    # Generate new files
    for filename, content in config_files.items():
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)
            print(f"Created {filename}")

if __name__ == "__main__":
    generate_config_files()
