# ADR template — DO NOT MODIFY

This file is a pointer, not the real template. The canonical ADR
template lives at [`.cursor/templates/adr.md`](../../.cursor/templates/adr.md)
so it can be referenced by the `propose-adr` skill without bumping
ADR numbering.

When drafting a new ADR:

1. List existing ADRs (`ls design/decisions/*.md`, excluding this file).
2. Pick the next four-digit number.
3. Copy the body of `.cursor/templates/adr.md`.
4. Write to `design/decisions/NNNN-<slug>.md`.
5. The canonical-edit-gate hook will prompt the human for approval on
   the write.
