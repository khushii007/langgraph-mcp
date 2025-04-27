"""MCP Router using LangGraph

This module routes user message to appropriate MCP server.
- build_router_graph: builds and indexes a document for each MCP (Model Context Protocol) server
- assistant_graph: uses the index to:
    - decide which MCP server to route the user message to
    - decide which tool(s) in the MCP server to call
    - call the tool(s) and return the result(s)

"""

from langgraph_mcp.assistant_graph import graph as graph
from langgraph_mcp.build_router_graph import graph as index_graph


__all__ = ["graph", "index_graph"]
