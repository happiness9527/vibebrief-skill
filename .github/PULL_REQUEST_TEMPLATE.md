## Summary

Describe the change in plain language.

## Scope

- [ ] Skill instructions
- [ ] References
- [ ] Examples
- [ ] Scripts
- [ ] Docs
- [ ] Project metadata

## Safety checklist

- [ ] No secrets, credentials, private customer data, or internal paths are included.
- [ ] Examples use fictional projects.
- [ ] Claims about verification are not invented.
- [ ] Changes stay within VibeBrief's scope.

## Checks

```bash
python3 vibebrief/scripts/doctor.py
python3 -m py_compile vibebrief/scripts/*.py
git diff --check
```
