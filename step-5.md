# Step 5 — Clean stale references and verify source registry

> Working document for resolving Step 5 issues one at a time. This file is temporary and records the issues, decisions, and resolution status for this step. Final decisions must be reflected in the appropriate canonical documentation; this file is not the source of truth.

## Goal

Ensure that the repository contains no stale references from the pre-reorganization model and that source identity, registry metadata, and actual source artifacts are consistent.

## Resolution order

### 5.1 Audit stale references
- [x] Search the repository for references to obsolete paths, files, schema names, and architecture concepts.
- [x] Remove obsolete architecture documentation and stale references that are no longer needed.
- [x] Confirm that current documentation describes only the active Adaptive Learning model.

### 5.2 Clarify the scope and semantics of the Source Registry
- [x] Decide that the Source Registry contains only sources whose artifacts actually exist in the repository.
- [x] Replace the CSV registry with a human-readable YAML registry.
- [x] Reduce each registry item to `id`, `name`, `type`, and `artifact`.
- [x] Define `artifact` as the repository path to the actual source artifact.
- [x] Update the related documentation to reflect the new registry scope and structure.

### 5.3 Synchronize Source Registry metadata
- [ ] Compare `sources/source-registry.yaml` against `docs/learning-material/sources/source-registry.md`.
- [ ] Verify that every registry value conforms to the documented field semantics.
- [ ] Resolve any remaining source identity or metadata mismatches.

### 5.4 Verify source identity and artifact paths
- [ ] Verify that each source artifact currently present in the repository has a corresponding registry entry.
- [ ] Verify that each `artifact` path recorded in the registry actually exists.
- [ ] Verify `source_id` consistency between the registry, source files, `source-segments.yaml`, Segment metadata, and downstream references.
- [ ] Verify source version/edition metadata where the repository contains a concrete source artifact.

### 5.5 Final Step 5 verification
- [ ] Re-run the stale-reference audit after all fixes.
- [ ] Re-run source-registry consistency checks.
- [ ] Confirm that no unresolved Step 5 issues remain.
- [ ] Mark Step 5 complete in `WORK-IN-PROGRESS.md`.

## Working rule

Resolve **one issue at a time**. Before changing a canonical document or source metadata, discuss the finding and agree on the intended model. This file records the working process; canonical documentation remains the final source of truth.
