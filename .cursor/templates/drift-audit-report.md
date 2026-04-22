# Drift audit — <scope of audit> — <date>

- **Scope:** Full | `<subsystem>`
- **Date:** YYYY-MM-DD
- **Produced by:** `drift-audit` skill

## Summary

- Findings: <N red>, <N yellow>
- Worst finding: <one sentence>
- Recommended next step: <one sentence>

## Red findings — live contradictions

For each: canonical path, divergent path, one-line description,
proposed remediation (code fix OR ADR draft).

- **<finding title>**
  - Canon: `design/...` — says ...
  - Divergent: `path:line` — does ...
  - Remediation: <fix OR ADR via `propose-adr`>

## Yellow findings

### Stale — docs lag code
- ...

### Orphan — doc or code without a parent in the canon chain
- ...

### Missing — expected artifact does not exist
- ...

## Layer-by-layer status

### Scope vs GDD
- <verdict>

### Domain vs Scope
- <verdict>

### Tech vs Domain
- <verdict>

### ADRs vs Tech / Domain
- <verdict>

### Code vs Tech
- <verdict>

## Recommended remediations

Numbered list. Each remediation is either a code change (Tier
declared) or an ADR (`propose-adr`).

1. ...
2. ...
