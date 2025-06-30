import argparse
from .server import mcp

def main():
    """MCP Mizra: Fetch members and groups."""
    parser = argparse.ArgumentParser(
        description="Fetch members and groups."
    )
    parser.parse_args()
    mcp.run()

if __name__ == "__main__":
    main()
