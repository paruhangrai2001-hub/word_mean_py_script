#!/usr/bin/env python3
"""Calculate R2 values for a voltage divider circuit.

Vout = Vin * R2 / (R1 + R2)  =>  R2 = R1 * Vout / (Vin - Vout)
"""
# Usage: python Scripts/voltage_divider.py --vin 3.3 --vout 1.8 --r1 1000 2200 5100 4700 6800

import argparse
import sys


def calculate_r2(vin: float, vout: float, r1: float) -> float:
    if vin <= vout:
        raise ValueError("Vin must be greater than Vout")
    if vin == 0:
        raise ValueError("Vin cannot be zero")
    return r1 * vout / (vin - vout)


def main():
    parser = argparse.ArgumentParser(description="Calculate R2 for a voltage divider")
    parser.add_argument("--vin", type=float, required=True, help="Input voltage (single value)")
    parser.add_argument("--vout", type=float, required=True, help="Output voltage (single value)")
    parser.add_argument("--r1", type=float, nargs="+", required=True, help="R1 resistance value(s)")
    args = parser.parse_args()

    print(f"Vin:  {args.vin} V")
    print(f"Vout: {args.vout} V")
    print()
    print(f"{'R1':>12} | {'R2':>12}")
    print(f"{'-'*12}-+-{'-'*12}")

    for r1 in args.r1:
        try:
            r2 = calculate_r2(args.vin, args.vout, r1)
            print(f"{r1:>12.2f} | {r2:>12.2f}")
        except ValueError as e:
            print(f"{r1:>12.2f} | ERROR: {e}")


if __name__ == "__main__":
    main()
