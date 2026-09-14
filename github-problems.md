# GitHub Problems & Recovery Notes

> This file is **only** for problems encountered while operating on the GitHub repository through the GitHub connector/tooling, plus the verified recovery procedure for those GitHub-specific problems.
>
> Do **not** put learning-material architecture, ontology, parser design, grammar rules, or other project-domain principles here. Those belong in the appropriate project documentation.

---

## Problem 1 — Updating an existing file without the current blob SHA

### Observed failure

An attempt was made to update `docs/learning-material-principles.md` without first supplying the file's current blob SHA required by the GitHub `update_file` operation. The first update attempt therefore did not complete as intended.

### Root cause

The GitHub file-update operation uses optimistic concurrency: when replacing an existing file, it requires the **current content/blob SHA** so GitHub can verify that the file has not changed unexpectedly.

Knowing the repository path is not sufficient.

### Correct recovery procedure

When updating an existing file:

1. Call `fetch_file` for the exact repository path.
2. Read the returned `sha` field.
3. Prepare the complete replacement content.
4. Call `update_file` with the repository, exact path, complete content, meaningful commit message, and returned SHA.
5. Verify that the operation returns a new commit/content SHA.
6. If the update fails because the SHA is stale, fetch the file again and use the newest SHA. Do not blindly retry with the stale SHA.

Canonical pattern:

```text
fetch_file(path)
      ↓
read current sha
      ↓
prepare complete replacement content
      ↓
update_file(path, content, message, sha)
      ↓
verify commit/content SHA
```

### Permanent rule

> **Never call `update_file` on an existing GitHub file using a remembered or guessed SHA. Fetch the current file first when the current SHA is not guaranteed to be current.**

---

## Problem 2 — Creating a file that already exists

### Root cause

`create_file` is for a **new** file. Replacing an existing file requires `update_file` with the existing blob SHA.

### Correct recovery procedure

1. Call `fetch_file` on the target path.
2. If it exists, use `update_file` with the returned SHA.
3. If it does not exist, use `create_file`.
4. Do not guess from memory whether the path exists.

```text
fetch_file(path)
      ↓
exists?
 ┌────┴────┐
 YES       NO
  ↓         ↓
update    create
```

---

## Problem 3 — A successful GitHub write does not prove semantic correctness

### Root cause

A write returning a commit SHA proves that GitHub accepted the write. It does **not** prove that the requested document change was correct.

### Correct recovery procedure

After a consequential write:

1. Verify the returned commit/content SHA.
2. Fetch the resulting file again when the change is important.
3. Confirm the target path and relevant content.
4. Only then report the repository change as complete.

For large canonical documents, verify the changed section rather than relying only on the write response.

---

## Problem 4 — Use the GitHub connector for connected-repository operations

### Rule

When the user asks to inspect, modify, create, delete, or otherwise operate on the connected GitHub repository, use the GitHub connector/tool rather than generic web access.

Use web search for genuinely external research, not as a substitute for repository operations.

---

## Recovery checklist

Before any GitHub repository write:

- [ ] Exact repository?
- [ ] Exact target path?
- [ ] Does the target already exist?
- [ ] If it exists, do I have its **current** blob SHA?
- [ ] `update_file` for an existing file, `create_file` for a new file?
- [ ] Complete replacement content?
- [ ] Meaningful commit message?
- [ ] Write returned commit/content SHA?
- [ ] Should the result be fetched for verification?

### Permanent operating rule

> **Inspect current GitHub state before mutating it; use the correct create/update operation; verify consequential writes.**
