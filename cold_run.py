"""Cold run: execute every check in this repository end to end and write cold_run_log.txt.

Run it from a fresh clone, in a fresh terminal, with plain Python 3 (standard library only):

    git clone https://github.com/BrandonOganovich19/FIN43900-AI-in-Finance-Project-1.git
    cd FIN43900-AI-in-Finance-Project-1
    python cold_run.py

The log records the UTC time, Python version, platform, git commit, a SHA-256 hash of every
tracked source file, the output of each step, and PASS/FAIL against the expected result.
A step that should fail (the break test) passes only if it fails in the expected way.
Exit code 0 = every check passed.
"""

import hashlib
import platform
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
LOG = HERE / "cold_run_log.txt"
PY = sys.executable

# (label, command, expected exit status: 0 or "nonzero", strings that must appear in the output)
STEPS = [
    ("Known answer: ABG training case reproduces $291.75",
     [PY, "proforma.py"], 0, ["Value per share: $291.75"]),
    ("Accenture model: five years balance, cash floor holds, value $182.00",
     [PY, "accenture_proforma.py"], 0,
     [f"FY{y}E  Assets - liabilities - equity: 0.0  Cash minimum: PASS" for y in range(2026, 2031)]
     + ["Value per share: $182.00"]),
    ("Break test fails loudly: gap equals the removed deferred-revenue link",
     [PY, "accenture_proforma.py", "--break-test"], "nonzero",
     ["AssertionError: FY2026E balance sheet gap: -238.3"]),
    ("Sensitivity runner: scenarios isolated, restored base matches",
     [PY, "accenture_sensitivity.py", "ACN_Lab11_inputs.json"], 0,
     ["Inputs: PASS; outputs and linked rows: PASS"]),
    ("Unit tests",
     [PY, "-m", "unittest", "-v", "test_accenture_sensitivity"], 0, ["OK"]),
    ("Peer P/E calculator reproduces the Oct 10, 2025 range",
     [PY, "accenture_comps_pe.py"], 0, ["Implied range:      $177.27 - $220.65"]),
    ("Edition B checks: boundary, monotonicity, grid, break-evens, restored base",
     [PY, "ACN_EditionB_checks.py"], 0,
     ["BLOCKED -> PASS", "Higher discount rate -> lower value: PASS",
      "Higher growth -> higher value: PASS", "Every row rises with g: PASS",
      "value matches first base within 1e-8: PASS"]),
]
if (HERE / "test_accenture_proforma.py").exists():
    STEPS.append(("Lab 10 unit tests", [PY, "-m", "unittest", "-v", "test_accenture_proforma"], 0, ["OK"]))


def git_commit():
    try:
        return subprocess.run(["git", "rev-parse", "HEAD"], cwd=HERE, capture_output=True,
                              text=True, timeout=10).stdout.strip() or "not a git checkout"
    except (OSError, subprocess.SubprocessError):
        return "git not available"


def main():
    lines = ["COLD RUN LOG", "=" * 72,
             f"UTC time:  {datetime.now(timezone.utc):%Y-%m-%d %H:%M:%S}",
             f"Python:    {platform.python_version()} ({PY})",
             f"Platform:  {platform.platform()}",
             f"Git HEAD:  {git_commit()}", "", "FILE HASHES (SHA-256)"]
    for f in sorted(HERE.iterdir()):
        if f.is_file() and f.suffix in {".py", ".json", ".md", ".txt"} and f.name != LOG.name:
            lines.append(f"  {hashlib.sha256(f.read_bytes()).hexdigest()}  {f.name}")
    results = []
    for label, cmd, want_exit, needles in STEPS:
        p = subprocess.run(cmd, cwd=HERE, capture_output=True, text=True, timeout=300)
        out = p.stdout + p.stderr
        exit_ok = (p.returncode == 0) if want_exit == 0 else (p.returncode != 0)
        missing = [n for n in needles if n not in out]
        ok = exit_ok and not missing
        results.append((label, ok))
        lines += ["", "-" * 72, f"[{'PASS' if ok else 'FAIL'}] {label}",
                  f"$ {' '.join(Path(c).name if c == PY else c for c in cmd)}   (exit {p.returncode})"]
        if missing:
            lines.append("  missing expected output: " + " | ".join(missing))
        tail = [l for l in out.splitlines() if l.strip()][-12:]
        lines += ["  " + l for l in tail]
    lines += ["", "=" * 72, "SUMMARY"]
    lines += [f"  {'PASS' if ok else 'FAIL'}  {label}" for label, ok in results]
    passed = sum(ok for _, ok in results)
    lines.append(f"\n{passed}/{len(results)} checks passed")
    LOG.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    sys.exit(0 if passed == len(results) else 1)


if __name__ == "__main__":
    main()
