# sqli-brownbag-demo

Deliberately vulnerable Flask login demo for the SQL-injection code-review brownbag.

## Demo scenario

This branch plants **two common security problems** for you to spot during code review:

1. **SQL injection in `app.py`** — the `/login` route builds its SQL query by concatenating the `username` (and `password`) straight from the request into the query string, so an attacker can submit something like `' OR '1'='1` to bypass authentication.
2. **Hardcoded database password in `config.py`** — the file contains a literal database password (and other secrets) committed to source control instead of being loaded from environment variables or a secret manager.

Each planted issue is flagged in the pull-request review comments, one comment per issue, pointing at the file and line where it lives.
