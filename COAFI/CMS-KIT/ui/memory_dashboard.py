#!/usr/bin/env python3
"""
Memory Dashboard for COAFI System
Provides a streamlined interface for monitoring and analyzing memory operations,
vector storage efficiency, and semantic retrieval performance.
"""

import os
import json
import time
import logging
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Tuple

import dash
from dash import dcc, html, Input, Output, State, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import requests

# Import local memory service if available
try:
    from services.memory import memory_service, MemoryQuery, MemoryStats
    LOCAL_SERVICE_AVAILABLE = True
except ImportError:
    LOCAL_SERVICE_AVAILABLE = False

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("coafi.memory_dashboard")

# Configuration
FASTAPI_URL = os.environ.get("FASTAPI_URL", "http://localhost:8000")
REFRESH_INTERVAL = int(os.environ.get("REFRESH_INTERVAL", "30"))  # seconds
THEME = os.environ.get("DASHBOARD_THEME", "BOOTSTRAP")
AEROSPACE_COLOR_PALETTE = ["#1E88E5", "#FFC107", "#D81B60", "#004D40", "#5E35B1"]

# Initialize the Dash app
app = dash.Dash(
    __name__,
    external_stylesheets=[getattr(dbc.themes, THEME)],
    title="COAFI Memory Dashboard",
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
    suppress_callback_exceptions=True
)

# Define the layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1("COAFI Memory Dashboard", className="text-center my-4"),
            html.P("Aerospace Memory System Monitoring", className="text-center text-muted"),
        ], width=12)
    ]),
    
    # Tabs for different dashboard views
    dbc.Tabs([
        # Overview Tab
        dbc.Tab(label="Overview", children=[
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader("System Status", className="bg-primary text-white"),
                        dbc.CardBody([
                            dbc.Row([
                                dbc.Col([
                                    html.Div([
                                        html.H3(id="total-vectors", children="0"),
                                        html.P("Total Vectors"),
                                    ], className="text-center border rounded p-3"),
                                ], width=3),
                                dbc.Col([
                                    html.Div([
                                        html.H3(id="total-memory", children="0 MB"),
                                        html.P("Memory Usage"),
                                    ], className="text-center border rounded p-3"),
                                ], width=3),
                                dbc.Col([
                                    html.Div([
                                        html.H3(id="avg-query-time", children="0 ms"),
                                        html.P("Avg Query Time"),
                                    ], className="text-center border rounded p-3"),
                                ], width=3),
                                dbc.Col([
                                    html.Div([
                                        html.H3(id="cache-status", children="N/A"),
                                        html.P("Cache Status"),
                                    ], className="text-center border rounded p-3"),
                                ], width=3),
                            ]),
                        ]),
                    ], className="mb-4"),
                ], width=12),
            ]),
            
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader("Vector Storage Distribution", className="bg-primary text-white"),
                        dbc.CardBody([
                            dcc.Graph(id="vector-distribution"),
                        ]),
                    ]),
                ], width=6),
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader("Query Performance", className="bg-primary text-white"),
                        dbc.CardBody([
                            dcc.Graph(id="query-performance"),
                        ]),
                    ]),
                ], width=6),
            ], className="mb-4"),
            
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader("Memory Usage Trend", className="bg-primary text-white"),
                        dbc.CardBody([
                            dcc.Graph(id="memory-trend"),
                        ]),
                    ]),
                ], width=12),
            ], className="mb-4"),
        ]),
        
        # Query Explorer Tab
        dbc.Tab(label="Query Explorer", children=[
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader("Semantic Query", className="bg-primary text-white"),
                        dbc.CardBody([
                            dbc.Row([
                                dbc.Col([
                                    html.Label("Query Text:"),
                                    dbc.Textarea(
                                        id="query-text",
                                        placeholder="Enter your semantic query here...",
                                        style={"height": "100px"},
                                        className="mb-3"
                                    ),
                                ], width=12),
                            ]),
                            dbc.Row([
                                dbc.Col([
                                    html.Label("Mood:"),
                                    dcc.Dropdown(
                                        id="query-mood",
                                        options=[
                                            {"label": "All", "value": "all"},
                                            {"label": "Aerospace", "value": "aerospace"},
                                            {"label": "Technical", "value": "technical"},
                                            {"label": "Creative", "value": "creative"},
                                        ],
                                        value="aerospace",
                                        clearable=False,
                                    ),
                                ], width=4),
                                dbc.Col([
                                    html.Label("Min Similarity:"),
                                    dcc.Slider(
                                        id="min-similarity",
                                        min=0.5,
                                        max=0.95,
                                        step=0.05,
                                        value=0.7,
                                        marks={i/100: f"{i/100}" for i in range(50, 100, 10)},
                                    ),
                                ], width=4),
                                dbc.Col([
                                    html.Label("Token Limit:"),
                                    dbc.Input(
                                        id="token-limit",
                                        type="number",
                                        value=1000,
                                        min=100,
                                        max=5000,
                                        step=100
                                    ),
                                ], width=4),
                            ], className="mb-3"),
                            dbc.Row([
                                dbc.Col([
                                    dbc.Button(
                                        "Execute Query", 
                                        id="execute-query-button", 
                                        color="primary", 
                                        className="w-100"
                                    ),
                                ], width={"size": 4, "offset": 4}),
                            ]),
                        ]),
                    ], className="mb-4"),
                ], width=12),
            ]),
            
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader("Query Results", className="bg-primary text-white"),
                        dbc.CardBody([
                            html.Div(id="query-results-container", children=[
                                html.P("Execute a query to see results", className="text-center text-muted")
                            ]),
                        ]),
                    ], className="mb-4"),
                ], width=12),
            ]),
            
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader("Query Statistics", className="bg-primary text-white"),
                        dbc.CardBody([
                            html.Div(id="query-stats-container"),
                        ]),
                    ]),
                ], width=12),
            ]),
        ]),
        
        # Memory Management Tab
        dbc.Tab(label="Memory Management", children=[
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader("Memory Operations", className="bg-primary text-white"),
                        dbc.CardBody([
                            dbc.Tabs([
                                dbc.Tab(label="Add Memory", children=[
                                    dbc.Form([
                                        dbc.Row([
                                            dbc.Col([
                                                html.Label("Content:"),
                                                dbc.Textarea(
                                                    id="memory-content",
                                                    placeholder="Enter memory content...",
                                                    style={"height": "150px"},
                                                    className="mb-3"
                                                ),
                                            ], width=12),
                                        ]),
                                        dbc.Row([
                                            dbc.Col([
                                                html.Label("Source Type:"),
                                                dcc.Dropdown(
                                                    id="memory-source-type",
                                                    options=[
                                                        {"label": "Message", "value": "message"},
                                                        {"label": "Conversation", "value": "conversation"},
                                                        {"label": "Summary", "value": "summary"},
                                                        {"label": "Memory Layer", "value": "memory_layer"},
                                                    ],
                                                    value="memory_layer",
                                                ),
                                            ], width=4),
                                            dbc.Col([
                                                html.Label("Mood:"),
                                                dcc.Dropdown(
                                                    id="memory-mood",
                                                    options=[
                                                        {"label": "Aerospace", "value": "aerospace"},
                                                        {"label": "Technical", "value": "technical"},
                                                        {"label": "Creative", "value": "creative"},
                                                    ],
                                                    value="aerospace",
                                                ),
                                            ], width=4),
                                            dbc.Col([
                                                html.Label("Folder ID:"),
                                                dbc.Input(
                                                    id="memory-folder",
                                                    type="text",
                                                    placeholder="Optional folder ID"
                                                ),
                                            ], width=4),
                                        ], className="mb-3"),
                                        dbc.Row([
                                            dbc.Col([
                                                dbc.Button(
                                                    "Add to Memory", 
                                                    id="add-memory-button", 
                                                    color="success", 
                                                    className="w-100"
                                                ),
                                            ], width={"size": 4, "offset": 4}),
                                        ]),
                                    ]),
                                ]),
                                dbc.Tab(label="Memory Cleanup", children=[
                                    dbc.Form([
                                        dbc.Row([
                                            dbc.Col([
                                                html.Label("Cleanup Type:"),
                                                dcc.Dropdown(
                                                    id="cleanup-type",
                                                    options=[
                                                        {"label": "Remove Duplicates", "value": "duplicates"},
                                                        {"label": "Remove Low Quality", "value": "low_quality"},
                                                        {"label": "Compress Similar", "value": "compress"},
                                                    ],
                                                    value="duplicates",
                                                ),
                                            ], width=6),
                                            dbc.Col([
                                                html.Label("Target Folder:"),
                                                dbc.Input(
                                                    id="cleanup-folder",
                                                    type="text",
                                                    placeholder="Optional folder ID to clean"
                                                ),
                                            ], width=6),
                                        ], className="mb-3"),
                                        dbc.Row([
                                            dbc.Col([
                                                html.Label("Similarity Threshold:"),
                                                dcc.Slider(
                                                    id="cleanup-threshold",
                                                    min=0.7,
                                                    max=0.99,
                                                    step=0.01,
                                                    value=0.92,
                                                    marks={i/100: f"{i/100}" for i in range(70, 100, 5)},
                                                ),
                                            ], width=12),
                                        ], className="mb-3"),
                                        dbc.Row([
                                            dbc.Col([
                                                dbc.Button(
                                                    "Run Cleanup", 
                                                    id="run-cleanup-button", 
                                                    color="warning", 
                                                    className="w-100"
                                                ),
                                            ], width={"size": 4, "offset": 4}),
                                        ]),
                                    ]),
                                ]),
                            ]),
                        ]),
                    ], className="mb-4"),
                ], width=12),
            ]),
            
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader("Operation Results", className="bg-primary text-white"),
                        dbc.CardBody([
                            html.Div(id="operation-results-container", children=[
                                html.P("Execute an operation to see results", className="text-center text-muted")
                            ]),
                        ]),
                    ]),
                ], width=12),
            ]),
        ]),
        
        # Settings Tab
        dbc.Tab(label="Settings", children=[
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader("Dashboard Settings", className="bg-primary text-white"),
                        dbc.CardBody([
                            dbc.Row([
                                dbc.Col([
                                    html.Label("API Endpoint:"),
                                    dbc.InputGroup([
                                        dbc.Input(
                                            id="api-endpoint",
                                            value=FASTAPI_URL,
                                            placeholder="http://localhost:8000"
                                        ),
                                        dbc.Button("Update", id="update-endpoint-button"),
                                    ]),
                                ], width=6),
                                dbc.Col([
                                    html.Label("Refresh Interval (seconds):"),
                                    dbc.InputGroup([
                                        dbc.Input(
                                            id="refresh-interval",
                                            type="number",
                                            value=REFRESH_INTERVAL,
                                            min=5,
                                            max=300,
                                            step=5
                                        ),
                                        dbc.Button("Update", id="update-interval-button"),
                                    ]),
                                ], width=6),
                            ], className="mb-3"),
                            dbc.Row([
                                dbc.Col([
                                    html.Label("Theme:"),
                                    dcc.Dropdown(
                                        id="theme-selector",
                                        options=[
                                            {"label": "Bootstrap", "value": "BOOTSTRAP"},
                                            {"label": "Darkly", "value": "DARKLY"},
                                            {"label": "Flatly", "value": "FLATLY"},
                                            {"label": "Cyborg", "value": "CYBORG"},
                                            {"label": "Journal", "value": "JOURNAL"},
                                        ],
                                        value=THEME,
                                        clearable=False,
                                    ),
                                ], width=6),
                                dbc.Col([
                                    html.Label("Connection Mode:"),
                                    dbc.RadioItems(
                                        id="connection-mode",
                                        options=[
                                            {"label": "API", "value": "api"},
                                            {"label": "Direct (Local Service)", "value": "direct"},
                                        ],
                                        value="api" if not LOCAL_SERVICE_AVAILABLE else "direct",
                                        inline=True,
                                    ),
                                ], width=6),
                            ], className="mb-3"),
                            dbc.Row([
                                dbc.Col([
                                    dbc.Button(
                                        "Apply Settings", 
                                        id="apply-settings-button", 
                                        color="primary", 
                                        className="w-100"
                                    ),
                                ], width={"size": 4, "offset": 4}),
                            ]),
                        ]),
                    ], className="mb-4"),
                ], width=12),
            ]),
            
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader("System Information", className="bg-primary text-white"),
                        dbc.CardBody([
                            html.Div(id="system-info-container"),
                        ]),
                    ]),
                ], width=12),
            ]),
        ]),
    ]),
    
    # Refresh interval
    dcc.Interval(
        id="refresh-interval-component",
        interval=REFRESH_INTERVAL * 1000,
        n_intervals=0,
    ),
    
    # Store components for data
    dcc.Store(id="memory-data"),
    dcc.Store(id="query-data"),
    dcc.Store(id="settings-data"),
    
    # Footer
    dbc.Row([
        dbc.Col([
            html.Hr(),
            html.P(
                "COAFI Memory Dashboard © 2024 | Aerospace Documentation System",
                className="text-center text-muted",
            ),
        ], width=12),
    ]),
], fluid=True)

# Helper functions
def format_bytes(size_bytes):
    """Format bytes to human readable format"""
    if size_bytes == 0:
        return "0 B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB")
    i = int(np.floor(np.log(size_bytes) / np.log(1024)))
    p = np.power(1024, i)
    s = round(size_bytes / p, 2)
    return f"{s} {size_name[i]}"

def fetch_memory_stats():
    """Fetch memory statistics from API"""
    try:
        response = requests.get(f"{FASTAPI_URL}/semantic-query/stats")
        if response.status_code == 200:
            return response.json()
        else:
            logger.error(f"Error fetching memory stats: {response.status_code}")
            return {}
    except Exception as e:
        logger.error(f"Error fetching memory stats: {e}")
        return {}

def fetch_memory_trend(days=7):
    """Fetch memory usage trend data"""
    try:
        response = requests.get(f"{FASTAPI_URL}/semantic-query/trend", params={"days": days})
        if response.status_code == 200:
            return response.json()
        else:
            logger.error(f"Error fetching memory trend: {response.status_code}")
            return {"dates": [], "values": []}
    except Exception as e:
        logger.error(f"Error fetching memory trend: {e}")
        return {"dates": [], "values": []}

def execute_semantic_query(query_text, mood_id=None, min_similarity=0.7, token_limit=1000):
    """Execute a semantic query via API"""
    try:
        payload = {
            "query": query_text,
            "mood_id": mood_id if mood_id != "all" else None,
            "min_similarity": min_similarity,
            "token_limit": token_limit,
            "include_metadata": True
        }
        
        response = requests.post(f"{FASTAPI_URL}/semantic-query/", json=payload)
        if response.status_code == 200:
            return response.json()
        else:
            logger.error(f"Error executing query: {response.status_code}")
            return {"results": [], "total_results": 0, "processing_time": 0}
    except Exception as e:
        logger.error(f"Error executing query: {e}")
        return {"results": [], "total_results": 0, "processing_time": 0}

def add_to_memory(content, source_type, mood_id=None, folder_id=None):
    """Add content to memory via API"""
    try:
        payload = {
            "content": content,
            "source_type": source_type,
            "metadata": {
                "mood_id": mood_id,
                "folder_id": folder_id,
                "timestamp": datetime.now().isoformat()
            }
        }
        
        response = requests.post(f"{FASTAPI_URL}/memory/", json=payload)
        if response.status_code == 200:
            return response.json()
        else:
            logger.error(f"Error adding to memory: {response.status_code}")
            return {"success": False, "error": f"API error: {response.status_code}"}
    except Exception as e:
        logger.error(f"Error adding to memory: {e}")
        return {"success": False, "error": str(e)}

def run_memory_cleanup(cleanup_type, similarity_threshold, folder_id=None):
    """Run memory cleanup operation via API"""
    try:
        payload = {
            "cleanup_type": cleanup_type,
            "similarity_threshold": similarity_threshold,
            "folder_id": folder_id
        }
        
        response = requests.post(f"{FASTAPI_URL}/memory/cleanup", json=payload)
        if response.status_code == 200:
            return response.json()
        else:
            logger.error(f"Error running cleanup: {response.status_code}")
            return {"success": False, "error": f"API error: {response.status_code}"}
    except Exception as e:
        logger.error(f"Error running cleanup: {e}")
        return {"success": False, "error": str(e)}

def fetch_document_interdependencies():
    """Fetch document interdependencies from API"""
    try:
        response = requests.get(f"{FASTAPI_URL}/document-interdependencies")
        if response.status_code == 200:
            return response.json()
        else:
            logger.error(f"Error fetching document interdependencies: {response.status_code}")
            return {}
    except Exception as e:
        logger.error(f"Error fetching document interdependencies: {e}")
        return {}

def fetch_document_status():
    """Fetch document status from API"""
    try:
        response = requests.get(f"{FASTAPI_URL}/document-status")
        if response.status_code == 200:
            return response.json()
        else:
            logger.error(f"Error fetching document status: {response.status_code}")
            return {}
    except Exception as e:
        logger.error(f"Error fetching document status: {e}")
        return {}

def fetch_update_related_documents():
    """Fetch update related documents from API"""
    try:
        response = requests.get(f"{FASTAPI_URL}/update-related-documents")
        if response.status_code == 200:
            return response.json()
        else:
            logger.error(f"Error fetching update related documents: {response.status_code}")
            return {}
    except Exception as e:
        logger.error(f"Error fetching update related documents: {e}")
        return {}

def fetch_integrate_version_control():
    """Fetch integrate version control from API"""
    try:
        response = requests.get(f"{FASTAPI_URL}/integrate-version-control")
        if response.status_code == 200:
            return response.json()
        else:
            logger.error(f"Error fetching integrate version control: {response.status_code}")
            return {}
    except Exception as e:
        logger.error(f"Error fetching integrate version control: {e}")
        return {}

# Callbacks
@app.callback(
    [
        Output("memory-data", "data"),
    ],
    [
        Input("refresh-interval-component", "n_intervals"),
        Input("apply-settings-button", "n_clicks"),
    ]
)
def update_memory_data(n_intervals, n_clicks):
    """Update memory data periodically"""
    memory_stats = fetch_memory_stats()
    return [json.dumps(memory_stats)]

@app.callback(
    [
        Output("total-vectors", "children"),
        Output("total-memory", "children"),
        Output("avg-query-time", "children"),
        Output("cache-status", "children"),
    ],
    [Input("memory-data", "data")]
)
def update_overview_stats(memory_data):
    """Update overview statistics"""
    if not memory_data:
        return "0", "0 MB", "0 ms", "N/A"
    
    try:
        data = json.loads(memory_data)
        
        total_vectors = data.get("vector_db", {}).get("total_vectors", 0)
        memory_usage = data.get("vector_db", {}).get("memory_usage", 0)
        avg_query_time = data.get("metrics", {}).get("avg_query_time_ms", 0)
        
        cache_info = data.get("cache", {})
        cache_hit_rate = cache_info.get("hit_rate", 0) * 100
        cache_type = cache_info.get("using_redis", False) and "Redis" or "Local"
        cache_status = f"{cache_hit_rate:.1f}% ({cache_type})"
        
        return str(total_vectors), format_bytes(memory_usage), f"{avg_query_time:.1f} ms", cache_status
    except Exception as e:
        logger.error(f"Error updating overview stats: {e}")
        return "Error", "Error", "Error", "Error"

@app.callback(
    Output("vector-distribution", "figure"),
    [Input("memory-data", "data")]
)
def update_vector_distribution(memory_data):
    """Update vector distribution chart"""
    if not memory_data:
        return go.Figure()
    
    try:
        data = json.loads(memory_data)
        
        # Extract distribution data
        distribution = data.get("vector_db", {}).get("distribution", {})
        
        if not distribution:
            # Create mock data if not available
            distribution = {
                "message": 35,
                "conversation": 25,
                "summary": 20,
                "memory_layer": 20
            }
        
        # Create pie chart
        fig = px.pie(
            names=list(distribution.keys()),
            values=list(distribution.values()),
            title="Vector Distribution by Source Type",
            color_discrete_sequence=AEROSPACE_COLOR_PALETTE
        )
        
        fig.update_traces(textposition="inside", textinfo="percent+label")
        fig.update_layout(template="plotly_white")
        
        return fig
    except Exception as e:
        logger.error(f"Error updating vector distribution: {e}")
        return go.Figure()

@app.callback(
    Output("query-performance", "figure"),
    [Input("memory-data", "data")]
)
def update_query_performance(memory_data):
    """Update query performance chart"""
    if not memory_data:
        return go.Figure()
    
    try:
        data = json.loads(memory_data)
        
        # Extract performance data
        performance = data.get("metrics", {}).get("query_performance", {})
        
        if not performance:
            # Create mock data if not available
            performance = {
                "last_24h": [
                    {"hour": "00:00", "avg_time": 120, "count": 5},
                    {"hour": "04:00", "avg_time": 110, "count": 8},
                    {"hour": "08:00", "avg_time": 150, "count": 15},
                    {"hour": "12:00", "avg_time": 180, "count": 25},
                    {"hour": "16:00", "avg_time": 160, "count": 20},
                    {"hour": "20:00", "avg_time": 130, "count": 10}
                ]
            }
        
        # Create performance chart
        performance_data = performance.get("last_24h", [])
        
        if not performance_data:
            return go.Figure()
        
        df = pd.DataFrame(performance_data)
        
        fig = go.Figure()
        
        # Add bar chart for query count
        fig.add_trace(go.Bar(
            x=df["hour"],
            y=df["count"],
            name="Query Count",
            marker_color=AEROSPACE_COLOR_PALETTE[0],
            opacity=0.7
        ))
        
        # Add line chart for average query time
        fig.add_trace(go.Scatter(
            x=df["hour"],
            y=df["avg_time"],
            name="Avg Query Time (ms)",
            mode="lines+markers",
            marker=dict(color=AEROSPACE_COLOR_PALETTE[1]),
            yaxis="y2"
        ))
        
        # Update layout
        fig.update_layout(
            title="Query Performance (Last 24 Hours)",
            xaxis=dict(title="Hour"),
            yaxis=dict(
                title="Query Count",
                side="left"
            ),
            yaxis2=dict(
                title="Avg Query Time (ms)",
                side="right",
                overlaying="y",
                showgrid=False
            ),
            legend=dict(x=0.01, y=0.99),
            template="plotly_white"
        )
        
        return fig
    except Exception as e:
        logger.error(f"Error updating query performance: {e}")
        return go.Figure()

@app.callback(
    Output("memory-trend", "figure"),
    [Input("memory-data", "data")]
)
def update_memory_trend(memory_data):
    """Update memory usage trend chart"""
    # Fetch trend data
    trend_data = fetch_memory_trend()
    
    try:
        dates = trend_data.get("dates", [])
        values = trend_data.get("values", [])
        
        if not dates:
            # Create mock data if not available
            now = datetime.now()
            dates = [(now - timedelta(days=i)).strftime("%Y-%m-%d") for i in range(7, -1, -1)]
            values = [50, 55, 60, 65, 75, 85, 90, 100]  # MB
        
        # Create trend chart
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=dates,
            y=values,
            mode="lines+markers",
            name="Memory Usage",
            line=dict(color=AEROSPACE_COLOR_PALETTE[0], width=3),
            fill="tozeroy",
            fillcolor=f"rgba({int(AEROSPACE_COLOR_PALETTE[0][1:3], 16)}, {int(AEROSPACE_COLOR_PALETTE[0][3:5], 16)}, {int(AEROSPACE_COLOR_PALETTE[0][5:7], 16)}, 0.2)"
        ))
        
        fig.update_layout(
            title="Memory Usage Trend",
            xaxis=dict(title="Date"),
            yaxis=dict(title="Memory Usage (MB)"),
            template="plotly_white"
        )
        
        return fig
    except Exception as e:
        logger.error(f"Error updating memory trend: {e}")
        return go.Figure()

@app.callback(
    [
        Output("query-results-container", "children"),
        Output("query-stats-container", "children"),
    ],
    [Input("execute-query-button", "n_clicks")],
    [
        State("query-text", "value"),
        State("query-mood", "value"),
        State("min-similarity", "value"),
        State("token-limit", "value"),
    ],
    prevent_initial_call=True
)
def execute_query(n_clicks, query_text, mood, min_similarity, token_limit):
    """Execute semantic query and display results"""
    if not query_text:
        return html.P("Please enter a query", className="text-center text-danger"), html.Div()
    
    # Execute query
    query_results = execute_semantic_query(
        query_text=query_text,
        mood_id=mood,
        min_similarity=min_similarity,
        token_limit=token_limit
    )
    
    # Create results display
    if not query_results or not query_results.get("results"):
        return html.P("No results found", className="text-center text-warning"), html.Div()
    
    results = query_results.get("results", [])
    processing_time = query_results.get("processing_time", 0)
    total_tokens = query_results.get("token_count", 0)
    validation_score = query_results.get("validationScore", 0)
    
    # Create results cards
    result_cards = []
    for i, result in enumerate(results):
        similarity = result.get("similarity_score", 0) * 100
        source_type = result.get("source_type", "unknown")
        content = result.get("content", "")
        metadata = result.get("metadata", {})
        
        # Format metadata display
        metadata_items = []
        for key, value in metadata.items():
            if key not in ["content", "source_type"]:
                metadata_items.append(html.Span(f"{key}: {value}", className="badge bg-light text-dark me-2"))
        
        # Create card
        card = dbc.Card([
            dbc.CardHeader([
                html.Span(f"Result #{i+1}", className="fw-bold"),
                html.Span(f" - {source_type.capitalize()}", className="text-muted"),
                html.Span(f" - {similarity:.1f}% match", className="ms-2 badge bg-primary")
            ]),
            dbc.CardBody([
                html.P(content),
                html.Div(metadata_items, className="mt-2")
            ])
        ], className="mb-3")
        
        result_cards.append(card)
    
    # Create stats display
    stats_display = dbc.Card([
        dbc.CardBody([
            dbc.Row([
                dbc.Col([
                    html.Div([
                        html.H4(f"{len(results)}", className="mb-0"),
                        html.P("Results Found", className="text-muted mb-0")
                    ], className="text-center")
                ], width=3),
                dbc.Col([
                    html.Div([
                        html.H4(f"{total_tokens}", className="mb-0"),
                        html.P("Total Tokens", className="text-muted mb-0")
                    ], className="text-center")
                ], width=3),
                dbc.Col([
                    html.Div([
                        html.H4(f"{processing_time * 1000:.1f} ms", className="mb-0"),
                        html.P("Processing Time", className="text-muted mb-0")
                    ], className="text-center")
                ], width=3),
                dbc.Col([
                    html.Div([
                        html.H4(f"{validation_score:.2f}", className="mb-0"),
                        html.P("Validation Score", className="text-muted mb-0")
                    ], className="text-center")
                ], width=3),
            ])
        ])
    ])
    
    return result_cards, stats_display

@app.callback(
    Output("operation-results-container", "children"),
    [
        Input("add-memory-button", "n_clicks"),
        Input("run-cleanup-button", "n_clicks")
    ],
    [
        State("memory-content", "value"),
        State("memory-source-type", "value"),
        State("memory-mood", "value"),
        State("memory-folder", "value"),
        State("cleanup-type", "value"),
        State("cleanup-threshold", "value"),
        State("cleanup-folder", "value")
    ],
    prevent_initial_call=True
)
def handle_memory_operations(add_clicks, cleanup_clicks, content, source_type, mood, folder, 
                            cleanup_type, cleanup_threshold, cleanup_folder):
    """Handle memory operations (add or cleanup)"""
    ctx = dash.callback_context
    if not ctx.triggered:
        return html.P("No operation executed", className="text-center text-muted")
    
    button_id = ctx.triggered[0]["prop_id"].split(".")[0]
    
    if button_id == "add-memory-button":
        if not content:
            return html.P("Please enter content to add", className="text-center text-danger")
        
        # Add to memory
        result = add_to_memory(content, source_type, mood, folder)
        
        if result.get("success", False):
            return html.Div([
                html.H4("Memory Added Successfully", className="text-success"),
                html.P(f"ID: {result.get('id')}"),
                html.P(f"Content length: {len(content)} characters"),
                html.P(f"Estimated tokens: {len(content) // 4}")
            ])
        else:
            return html.Div([
                html.H4("Error Adding Memory", className="text-danger"),
                html.P(result.get("error", "Unknown error"))
            ])
    
    elif button_id == "run-cleanup-button":
        # Run cleanup
        result = run_memory_cleanup(cleanup_type, cleanup_threshold, cleanup_folder)
        
        if result.get("success", False):
            stats = result.get("stats", {})
            return html.Div([
                html.H4("Cleanup Completed Successfully", className="text-success"),
                html.P(f"Operation: {cleanup_type}"),
                html.P(f"Items processed: {stats.get('processed', 0)}"),
                html.P(f"Items removed/merged: {stats.get('affected', 0)}"),
                html.P(f"Space saved: {format_bytes(stats.get('bytes_saved', 0))}")
            ])
        else:
            return html.Div([
                html.H4("Error Running Cleanup", className="text-danger"),
                html.P(result.get("error", "Unknown error"))
            ])
    
    return html.P("No operation executed", className="text-center text-muted")

@app.callback(
    Output("system-info-container", "children"),
    [Input("refresh-interval-component", "n_intervals")]
)
def update_system_info(n_intervals):
    """Update system information display"""
    try:
        memory_stats = fetch_memory_stats()
        
        vector_db_info = memory_stats.get("vector_db", {})
        cache_info = memory_stats.get("cache", {})
        metrics_info = memory_stats.get("metrics", {})
        
        return html.Div([
            dbc.Row([
                dbc.Col([
                    html.H5("Vector Database"),
                    html.P(f"Type: {vector_db_info.get('type', 'N/A')}"),
                    html.P(f"Dimension: {vector_db_info.get('dimension', 'N/A')}"),
                    html.P(f"Total vectors: {vector_db_info.get('total_vectors', 0)}"),
                    html.P(f"Memory usage: {format_bytes(vector_db_info.get('memory_usage', 0))}")
                ], width=4),
                dbc.Col([
                    html.H5("Cache"),
                    html.P(f"Type: {cache_info.get('using_redis', False) and 'Redis' or 'Local'}"),
                    html.P(f"Size: {cache_info.get('size', 'N/A')}"),
                    html.P(f"Hit rate: {cache_info.get('hit_rate', 0) * 100:.1f}%"),
                    html.P(f"Hits/Misses: {cache_info.get('hits', 0)}/{cache_info.get('misses', 0)}")
                ], width=4),
                dbc.Col([
                    html.H5("API"),
                    html.P(f"Endpoint: {FASTAPI_URL}"),
                    html.P(f"Status: {'Connected' if memory_stats else 'Disconnected'}"),
                    html.P(f"Local service: {'Available' if LOCAL_SERVICE_AVAILABLE else 'Unavailable'}"),
                    html.P(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                ], width=4)
            ])
        ])
    except Exception as e:
        logger.error(f"Error updating system info: {e}")
        return html.P(f"Error fetching system information: {str(e)}", className="text-danger")

@app.callback(
    Output("operation-results-container", "children"),
    [
        Input("adjust-license-button", "n_clicks")
    ],
    [
        State("license-id", "value"),
        State("feedback", "value")
    ],
    prevent_initial_call=True
)
def adjust_license(n_clicks, license_id, feedback):
    """Adjust license state based on feedback and context changes"""
    if not license_id or not feedback:
        return html.P("Please provide license ID and feedback", className="text-center text-danger")
    
    try:
        payload = {
            "license_id": license_id,
            "feedback": feedback
        }
        
        response = requests.post(f"{FASTAPI_URL}/adjust_license", json=payload)
        if response.status_code == 200:
            result = response.json()
            if result.get("success", False):
                return html.Div([
                    html.H4("License Adjusted Successfully", className="text-success"),
                    html.P(f"Adjusted State: {result.get('id')}")
                ])
            else:
                return html.Div([
                    html.H4("Error Adjusting License", className="text-danger"),
                    html.P(result.get("error", "Unknown error"))
                ])
        else:
            logger.error(f"Error adjusting license: {response.status_code}")
            return html.Div([
                html.H4("Error Adjusting License", className="text-danger"),
                html.P(f"API error: {response.status_code}")
            ])
    except Exception as e:
        logger.error(f"Error adjusting license: {e}")
        return html.Div([
            html.H4("Error Adjusting License", className="text-danger"),
            html.P(str(e))
        ])

@app.callback(
    Output("document-interdependencies", "children"),
    [Input("refresh-interval-component", "n_intervals")]
)
def update_document_interdependencies(n_intervals):
    """Update document interdependencies display"""
    try:
        interdependencies = fetch_document_interdependencies()
        return html.Div([
            html.H5("Document Interdependencies"),
            html.Pre(json.dumps(interdependencies, indent=2))
        ])
    except Exception as e:
        logger.error(f"Error updating document interdependencies: {e}")
        return html.P(f"Error fetching document interdependencies: {str(e)}", className="text-danger")

@app.callback(
    Output("document-status", "children"),
    [Input("refresh-interval-component", "n_intervals")]
)
def update_document_status(n_intervals):
    """Update document status display"""
    try:
        status = fetch_document_status()
        return html.Div([
            html.H5("Document Status"),
            html.Pre(json.dumps(status, indent=2))
        ])
    except Exception as e:
        logger.error(f"Error updating document status: {e}")
        return html.P(f"Error fetching document status: {str(e)}", className="text-danger")

@app.callback(
    Output("update-related-documents", "children"),
    [Input("refresh-interval-component", "n_intervals")]
)
def update_related_documents(n_intervals):
    """Update related documents display"""
    try:
        updates = fetch_update_related_documents()
        return html.Div([
            html.H5("Update Related Documents"),
            html.Pre(json.dumps(updates, indent=2))
        ])
    except Exception as e:
        logger.error(f"Error updating related documents: {e}")
        return html.P(f"Error fetching related documents: {str(e)}", className="text-danger")

@app.callback(
    Output("integrate-version-control", "children"),
    [Input("refresh-interval-component", "n_intervals")]
)
def update_integrate_version_control(n_intervals):
    """Update integrate version control display"""
    try:
        version_control = fetch_integrate_version_control()
        return html.Div([
            html.H5("Integrate Version Control"),
            html.Pre(json.dumps(version_control, indent=2))
        ])
    except Exception as e:
        logger.error(f"Error updating integrate version control: {e}")
        return html.P(f"Error fetching integrate version control: {str(e)}", className="text-danger")

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8050)))
