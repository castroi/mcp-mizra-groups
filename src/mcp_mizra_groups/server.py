
from mcp.server.fastmcp import FastMCP
import json
import os

mcp = FastMCP("mizra")

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "groups.json")

# Load JSON data globally
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Function: Find groups by member first + last name
@mcp.tool()
def find_members_by_name(first_name: str = None, last_name: str = None):
    """
    Find all matching members across all groups based on Hebrew name components.
    
    Search behavior:
    - Both names provided: returns members matching both first AND last Hebrew name
    - Only first name: returns members with matching Hebrew first name
    - Only last name: returns members with matching Hebrew last name
    
    Parameters:
    first_name (str, optional): Hebrew first name to match. Defaults to None.
    last_name (str, optional): Hebrew last name to match. Defaults to None.
    
    Returns:
    dict: Dictionary with 'members' key containing list of matching member records
          with Hebrew names preserved in original casing
    
    Raises:
    ValueError: If both first_name and last_name are None
    
    Example record format:
    {
        "firstName": " רואי",
        "lastName": "שמיר",
        "groupName": "Group A",
        "year": 2023
    }
    """
    results = []
    for group in data["groups"]:
        for member in group["members"]:
            # Case 1: Both names provided
            if first_name and last_name:
                if member["firstName"].lower() == first_name.lower() and \
                   member["lastName"].lower() == last_name.lower():
                    results.append({
                        "firstName": member["firstName"],
                        "lastName": member["lastName"],
                        "groupName": group["name"],
                        "year": group["year"]
                    })
            elif first_name:
            # Case 2: Only first name provided
                if member["firstName"].lower() == first_name.lower():
                    results.append({
                        "firstName": member["firstName"],
                        "lastName": member["lastName"],
                        "groupName": group["name"],
                        "year": group["year"]
                    })
            # Case 3: Only last name provided
            elif last_name:
                if member["lastName"].lower() == last_name.lower():
                    results.append({
                        "firstName": member["firstName"],
                        "lastName": member["lastName"],
                        "groupName": group["name"],
                        "year": group["year"]
                    })
    
    # Validate at least one parameter was provided
    if not (first_name or last_name):
        raise ValueError("At least one search parameter (first_name or last_name) is required")
    
    return {"members": results}
# Function: Find members in a specific group
@mcp.tool()
def find_members_by_group(group_name: str):
    """
    Purpose: Returns members of a specific group by Hebrew group name
    Parameters: 
    - group_name: Hebrew string for the group's name
    Returns: Dictionary with list of full member names (first + last) in the group
    """
    for group in data["groups"]:
        if group["name"] == group_name:
            return {
                "members": [f"{m['firstName']} {m['lastName']}" for m in group["members"]]
            }
    return {"members": []}

# Function: Find groups by year
@mcp.tool()
def find_groups_by_year(year: str):
    """
    Purpose: Finds groups created in a specific  year
    Parameters: 
    - year: Year value
    Returns: Dictionary with list of groups matching the specified year
    """
    results = []
    for group in data["groups"]:
        if group["year"] == year:
            results.append({
                "groupName": group["name"],
                "year": group["year"]
            })
    return {"groups": results}

