# Running the role quartet on an ADR draft

The parent agent should launch four `Task` tool calls **in a single
message** so they run in parallel. Each subagent receives:

1. The full ADR draft.
2. Pointers to the governing canon (GDD sections, scope doc, any
   affected domain docs and tech designs).
3. Its signature prompt (baked into each subagent's `.cursor/agents/*.md`).

## Invocation shape

For each of `architect`, `engineer`, `game-designer`, `operator`,
invoke the Task tool with:

- `subagent_type: generalPurpose` (or equivalent) with the subagent
  file referenced explicitly, OR
- the named subagent directly if Cursor's subagent runtime supports it.

The prompt to each subagent must include:

```
You are reviewing a proposed ADR.

ADR draft:
<paste full draft>

Governing canon:
- <path>: <why it matters>
- <path>: <why it matters>

Output strictly in your signature format.
```

## Collecting outputs

After all four return, synthesize into the ADR's `Addressed concerns`
section. Structure:

```
## Addressed concerns

### architect
- Concern: ...
  - Resolution: ... | Accepted as consequence | Deferred: see follow-up #N

### engineer
...

### game-designer
...

### operator
...
```

## Cost discipline

The quartet is expensive. Do not invoke it for Tier B or C changes.
If the user asks for a quartet review on a non-Tier-A change, decline
and explain the tier rule.
