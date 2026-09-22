# Source Registry

## Purpose

The Source Registry records source artifacts that actually exist in the repository.

It is a small, human-readable index that connects a stable source identity to the source artifact stored in the repository.

The registry is not a catalogue of planned, external, or unavailable sources.

## Registry Format

The registry is stored at:

`sources/source-registry.yaml`

Each registry item contains only:

| Field | Meaning |
|---|---|
| `id` | Stable source identifier used by the repository |
| `name` | Human-readable source name |
| `type` | Source type, such as `book` or `exam` |
| `artifact` | Repository path to the source artifact |

Example:

```yaml
sources:
  - id: destination-c1-c2
    name: Destination C1 & C2
    type: book
    artifact: sources/Destination_C1-C2.pdf
```

## Scope Rule

A source may be registered only when its source artifact actually exists in the repository.

Do not add entries for sources that are merely planned, referenced externally, or intended for future acquisition.

The `artifact` path must identify the actual source artifact in the repository.

Detailed extraction and segmentation metadata belongs with the source-processing artifacts, not in the registry.

## Provenance

The registry provides source identity and artifact location. It does not replace detailed provenance carried by Segments, evidence, or Knowledge Atoms.

Source-derived data must remain traceable to the registered source and its structural evidence.
