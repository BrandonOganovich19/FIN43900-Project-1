"""Edition B checks on the Lab 10 Accenture model (accenture_proforma.py).

Runs boundary, monotonicity, grid, break-even and mechanical sensitivity
checks without editing the Lab 10 model. Every run starts from a fresh copy
of the base ASSUMPTIONS and OPENING, and the base is restored and re-verified
at the end.

USD millions unless stated; per-share values in USD.

Usage:
    python ACN_EditionB_checks.py                 # uses the prices below
    python ACN_EditionB_checks.py 196.64          # override the current price
"""

import copy
import sys
from math import isclose

import accenture_proforma as m

LAB10_PRICE = 177.41        # Sept 24, 2026 close (ACN_Lab10.md)
CURRENT_PRICE = 229.68      # Oct 16, 2026 close -- UPDATE to the recording-day close
CURRENT_PRICE_DATE = "Oct 16, 2026"
FY2025_REVENUE = 69_672.977      # FY2025 10-K (ACN_Lab10.md R1)
FY2026_ACTUAL_REVENUE = 74_180.0 # Oct 1, 2026 earnings release (unaudited), $74.18B
FY2026_ACTUAL_SHARES = 596.0     # "approximately 596 million" at Aug 31, 2026 (same release)

BASE_A = copy.deepcopy(m.ASSUMPTIONS)
BASE_O = copy.deepcopy(m.OPENING)


def run(**changes):
    """Value the model with only `changes` applied to a fresh base copy."""
    m.ASSUMPTIONS.clear()
    m.ASSUMPTIONS.update(copy.deepcopy(BASE_A))
    m.ASSUMPTIONS.update(changes)
    m.OPENING.clear()
    m.OPENING.update(copy.deepcopy(BASE_O))
    rows = m.project()
    v = m.value(rows)
    v["tv_share"] = v["pv_terminal"] / (v["pv_fcfe"] + v["pv_terminal"])
    return v


def ke_to_erp(ke):
    return (ke - BASE_A["risk_free_rate"]) / BASE_A["beta"]


def solve(fn, target, lo, hi, n=80):
    """Bisection for fn(x) = target; fn must be monotonic on [lo, hi]."""
    flo = fn(lo) - target
    for _ in range(n):
        mid = (lo + hi) / 2
        fmid = fn(mid) - target
        if (fmid > 0) == (flo > 0):
            lo, flo = mid, fmid
        else:
            hi = mid
    return (lo + hi) / 2


def growth_path(g):
    return [BASE_A["growth"][0]] + [g] * 4


def pf(ok):
    return "PASS" if ok else "FAIL"


def main():
    current = float(sys.argv[1]) if len(sys.argv) > 1 else CURRENT_PRICE
    print("ACN EDITION B CHECKS -- built on accenture_proforma.py (Lab 10), not a replacement for it")
    print("USD millions unless stated; per-share values in USD.\n")

    base = run()
    print("1. BASE")
    print(f"   Value per share: ${base['per_share']:.2f}   cost of equity {base['ke']:.2%}   "
          f"terminal growth {BASE_A['terminal_growth']:.1%}")
    print(f"   Terminal value share of value: {base['tv_share']:.1%}\n")

    print("2. BOUNDARY: terminal growth at or above cost of equity must be refused")
    for g in (base["ke"], 0.11):
        try:
            run(terminal_growth=g)
            print(f"   g = {g:.2%}: ran  -> FAIL (should be blocked)")
        except ValueError as e:
            print(f"   g = {g:.2%}: BLOCKED -> PASS  ({e})")
    print()

    print("3. MONOTONICITY")
    kes = [base["ke"] - 0.01, base["ke"], base["ke"] + 0.01]
    v_ke = [run(equity_risk_premium=ke_to_erp(k))["per_share"] for k in kes]
    print("   Cost of equity  " + "   ".join(f"{k:.2%}: ${v:.2f}" for k, v in zip(kes, v_ke)))
    print(f"   Higher discount rate -> lower value: {pf(v_ke[0] > v_ke[1] > v_ke[2])}")
    gs = [0.02, 0.03, 0.04]
    v_g = [run(growth=growth_path(g))["per_share"] for g in gs]
    print("   FY27-30 growth  " + "   ".join(f"{g:.1%}: ${v:.2f}" for g, v in zip(gs, v_g)))
    print(f"   Higher growth -> higher value: {pf(v_g[0] < v_g[1] < v_g[2])}")
    tgs = [0.02, 0.03, 0.04]
    v_tg = [run(terminal_growth=t)["per_share"] for t in tgs]
    print("   Terminal growth " + "   ".join(f"{t:.1%}: ${v:.2f}" for t, v in zip(tgs, v_tg)))
    print(f"   Higher terminal growth -> higher value: {pf(v_tg[0] < v_tg[1] < v_tg[2])}\n")

    print("4. GRID: value per share, cost of equity (rows) x terminal growth (columns)")
    print("   Ke \\ g      2.0%       3.0%       4.0%")
    grid_ok = True
    for k in kes:
        vals = [run(equity_risk_premium=ke_to_erp(k), terminal_growth=t)["per_share"] for t in tgs]
        grid_ok &= vals[0] < vals[1] < vals[2]
        print(f"   {k:6.2%}  " + "  ".join(f"${v:8.2f}" for v in vals))
    print(f"   Every row rises with g: {pf(grid_ok)}\n")

    print("5. DOWNSIDE AND BREAK-EVENS")
    opt600 = run(business_optimization=[BASE_A["business_optimization"][0]] + [600.0] * 4)
    print(f"   Optimization $600M/yr FY27-30: ${opt600['per_share']:.2f}")
    for label, price in (("Lab 10 price $%.2f (Sept 24, 2026)" % LAB10_PRICE, LAB10_PRICE),
                         ("Current price $%.2f (%s)" % (current, CURRENT_PRICE_DATE), current)):
        g_be = solve(lambda g: run(growth=growth_path(g))["per_share"], price, -0.05, 0.20)
        ke_be = solve(lambda k: run(equity_risk_premium=ke_to_erp(k))["per_share"], price, 0.06, 0.15)
        print(f"   {label}:")
        print(f"     FY27-30 growth that equates value to price: {g_be:.2%}")
        print(f"     Cost of equity that equates value to price: {ke_be:.2%}")
        tg_be = solve(lambda t: run(terminal_growth=t)["per_share"], price, 0.0, 0.06)
        print(f"     Terminal growth that equates value to price: {tg_be:.2%}")
        if price <= base["per_share"]:
            o_be = solve(lambda x: run(business_optimization=[BASE_A['business_optimization'][0]] + [x] * 4)["per_share"],
                         price, 0.0, 2_000.0)
            print(f"     Optimization cost/yr FY27-30 that equates value to price: ${o_be:,.0f}M")
        else:
            print("     Optimization break-even: n/a (price is above base value even at $0)")
    print()

    print("6. GUIDED FY27 ORGANIC GROWTH (Q4 FY26 call: 3-6% LC guide less 2-2.5% inorganic)")
    for label, g in (("low (3% - 2.5%)", 0.005), ("midpoint (4.5% - 2.25%)", 0.0225), ("high (6% - 2%)", 0.04)):
        print(f"   {label:24s} {g:.2%} held FY27-30: ${run(growth=growth_path(g))['per_share']:.2f}")
    combo = run(growth=growth_path(0.0225),
                business_optimization=[BASE_A["business_optimization"][0]] + [600.0] * 4)
    print(f"   Combined downside (2.25% growth AND $600M/yr optimization): ${combo['per_share']:.2f}")
    print()

    print("7. MECHANICAL SENSITIVITIES (not a roll-forward: buyback cash, FY26 cash flows and timing are not updated)")
    g26 = FY2026_ACTUAL_REVENUE / FY2025_REVENUE - 1
    a = run(growth=[g26] + BASE_A["growth"][1:])
    b = run(share_count=FY2026_ACTUAL_SHARES)
    c = run(growth=[g26] + BASE_A["growth"][1:], share_count=FY2026_ACTUAL_SHARES)
    print(f"   FY26 revenue set to actual $74.18B (growth {g26:.2%}): ${a['per_share']:.2f}")
    print(f"   Shares set to ~596M:                               ${b['per_share']:.2f}")
    print(f"   Both:                                              ${c['per_share']:.2f}\n")

    restored = run()
    same_in = m.ASSUMPTIONS == BASE_A and m.OPENING == BASE_O
    same_out = isclose(restored["per_share"], base["per_share"], rel_tol=0, abs_tol=1e-8)
    print("8. RESTORED BASE")
    print(f"   Inputs restored: {pf(same_in)}   value matches first base within 1e-8: {pf(same_out)}"
          f"   (${restored['per_share']:.2f})")


if __name__ == "__main__":
    main()
