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
- [ ] Decide whether `sources/source-registry.csv` is a registry of all known/planned external sources or only sources whose artifacts currently exist in the repository.
- [ ] Define the intended meaning of `raw_cache_path` when a source is registered but its artifact is not currently cached in the repository.
- [ ] Ensure the registry documentation clearly describes this scope and path semantics.

### 5.3 Synchronize Source Registry metadata
- [ ] Compare `sources/source-registry.csv` against `docs/learning-material/sources/source-registry.md`.
- [ ] Resolve mismatches in documented source roles.
- [ ] Resolve field-name mismatches such as `cefr_coverage` vs `proficiency_coverage`.
- [ ] Verify that every registry value conforms to the documented field semantics and allowed values.
- [ ] Decide whether undocumented source roles (for example `exam`) should be added to the model or changed to an existing documented role.

### 5.4 Verify source identity and artifact paths
- [ ] Verify that each source artifact currently present in the repository has a corresponding registry entry.
- [ ] Verify that each repository path recorded in `raw_cache_path` actually exists when the field is intended to point to a repository artifact.
- [ ] Resolve the `destination-c1-c2` path mismatch between the registry and the actual `sources/destination-c1-c2/` directory.
- [ ] Verify `source_id` consistency between the registry, source files, `source-segments.yaml`, Segment metadata, and downstream references.
- [ ] Verify source version/edition metadata where the repository contains a concrete source artifact.

### 5.5 Final Step 5 verification
- [ ] Re-run the stale-reference audit after all fixes.
- [ ] Re-run source-registry consistency checks.
- [ ] Confirm that no unresolved Step 5 issues remain.
- [ ] Mark Step 5 complete in `WORK-IN-PROGRESS.md`.

## Working rule

Resolve **one issue at a time**. Before changing a canonical document or source metadata, discuss the finding and agree on the intended model. This file records the working process; canonical documentation remains the final source of truth.
