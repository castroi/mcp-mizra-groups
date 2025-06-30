# Mizra Member & Group Search - MCP Server  
A Model Context Protocol (MCP) server for querying Mizra members and groups by Hebrew name, group name, or year. Designed to integrate with [Goose AI](https://github.com/block/goose) as an extension.

---

## 🔧 Features  
- **Search Members by Hebrew Name**: First name, last name, or both.  
- **Search Members by Group**: Find all members in a specific Hebrew-named group.  
- **Search Groups by Year**: List groups created in a specific year.  
- **Goose AI Integration**: Works seamlessly with Goose's MCP extension system.  

---

## 🧪 Available Tools  

### 1. `find_members_by_name`  
**Purpose**: Search members using Hebrew name components.  
**Parameters**:  
- `first_name` (optional): Hebrew first name.  
- `last_name` (optional): Hebrew last name.  

**Returns**:  
```json
{
  "members": [
    {
      "firstName": "רואי",
      "lastName": "שמיר",
      "groupName": "Group A",
      "year": 2023
    }
  ]
}
```

**Example**:  
```python
find_members_by_name(first_name="רואי", last_name="שמיר")
```

---

### 2. `find_members_by_group`  
**Purpose**: Get members of a specific Hebrew-named group.  
**Parameters**:  
- `group_name`: Hebrew group name (e.g., ` עומר`).  

**Returns**:  
```json
{
  "members": ["רואי שמיר", "יונתן כהן"]
}
```

**Example**:  
```python
find_members_by_group(group_name="Group A")
```

---

### 3. `find_groups_by_year`  
**Purpose**: Find groups created in a specific year.  
**Parameters**:  
- `year`: Year as a string (e.g., `"2023"`).  

**Returns**:  
```json
{
  "groups": ["Group A", "Group B"]
}
```

---

## 🚀 Installation & Setup  

### Prerequisites  
- Python 3.10+  
- [`uv`](https://github.com/astral-sh/uv) (for dependency management)  

### 1. Install Dependencies  
```bash
uv add "mcp[cli]"
```

### 2. Clone the Repo  
```bash
git clone https://github.com/castroi/mcp-mizra-groups.git
cd mcp-mizra-groups
```

---

## 🧪 Testing with MCP Inspector  
Use the [MCP Inspector](https://modelcontextprotocol.org/tools/inspector) to debug your server:    

```bash
uv sync
source .venv/bin/activate
mcp dev src/mcp_mizra_groups/server.py
```
Then visit `http://127.0.0.1:6274` to interact with the tools.

---

## 📚 Dependencies  
- [`mcp[cli]`](https://github.com/modelcontextprotocol/mcp): FastMCP server implementation.  
- [`uv`](https://github.com/astral-sh/uv): Fast Python dependency manager.  

---

## ▶️ Usage  

### Run the Server  
```bash
source .venv/bin/activate
mcp dev src/mcp_mizra_groups/server.py
```

### Testing the CLI
```bash
uv pip install .
ls .venv/bin/  # Verify your CLI is available
mcp-mizra-groups --help
```


### Integrate with Goose AI  
[Goose AI](https://github.com/block/goose)

To add your MCP server as an extension in Goose:
Go to Settings > Extensions > Add.
Provide the ID, name, and description for your extension.
In the Command field, provide the absolute path to your executable. For example:

```bash
uv run /home/user/mcp-mizra-groups/.venv/bin/mcp-mizra-groups
```
More details: 
https://block.github.io/goose/docs/tutorials/custom-extensions


---

## 📌 License  
MIT License.
