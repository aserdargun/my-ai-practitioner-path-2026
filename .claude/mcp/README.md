# MCP Tools

Model Context Protocol (MCP) tool definitions for extending Claude's capabilities.

## Overview

MCP provides a standardized way to connect Claude to external tools and data sources. This folder contains tool contracts and stub implementations.

## Tool Contracts

### evaluate_progress

Evaluate learner progress and return scores.

```json
{
  "name": "evaluate_progress",
  "description": "Evaluate learner progress based on signals",
  "input_schema": {
    "type": "object",
    "properties": {
      "learner_level": {
        "type": "string",
        "enum": ["Beginner", "Intermediate", "Advanced"]
      },
      "month": {
        "type": "integer",
        "minimum": 1,
        "maximum": 12
      },
      "week": {
        "type": "integer",
        "minimum": 1,
        "maximum": 4
      }
    },
    "required": ["learner_level", "month", "week"]
  }
}
```

### suggest_adaptation

Suggest curriculum adaptations based on evaluation.

```json
{
  "name": "suggest_adaptation",
  "description": "Suggest path adaptations based on progress",
  "input_schema": {
    "type": "object",
    "properties": {
      "evaluation_result": {
        "type": "object"
      },
      "allowed_mutations": {
        "type": "array",
        "items": {
          "type": "string",
          "enum": ["level_change", "month_reorder", "remediation_week", "project_swap"]
        }
      }
    },
    "required": ["evaluation_result"]
  }
}
```

### log_event

Log a progress event to the memory system.

```json
{
  "name": "log_event",
  "description": "Log an event to progress_log.jsonl",
  "input_schema": {
    "type": "object",
    "properties": {
      "event": {
        "type": "string"
      },
      "details": {
        "type": "object"
      }
    },
    "required": ["event"]
  }
}
```

## Usage

These tools are used by Claude Code when executing commands like `/evaluate` and `/adapt-path`. The actual implementations are in the `path-engine/` folder using Python stdlib.

## Adding New Tools

1. Define the tool contract in this README
2. Implement the tool logic in `path-engine/`
3. Update the command catalog to use the new tool
