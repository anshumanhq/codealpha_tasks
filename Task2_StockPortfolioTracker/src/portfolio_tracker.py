"""
Stock Portfolio Tracker - CodeAlpha Python Internship Task 2
Reads stock holdings from a CSV file, calculates investment value,
and generates a formatted portfolio report.
"""

import csv
from pathlib import Path
from datetime import datetime


# Hardcoded current market prices (in real-world, fetch from API)
CURRENT_PRICES = {
    "AAPL": 175.50,
    "GOOGL": 2950.00,
    "MSFT": 340.75,
    "TSLA": 800.00,
    "AMZN": 3450.00,
}


def read_portfolio(file_path: Path) -> list[dict]:
    """Read stock holdings from CSV file.

    Args:
        file_path: Path to the CSV file.

    Returns:
        List of dicts with keys: symbol, quantity, buy_price.

    Raises:
        FileNotFoundError: If CSV file doesn't exist.
    """
    if not file_path.exists():
        raise FileNotFoundError(f"Portfolio file not found: {file_path}")

    holdings = []
    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                holdings.append({
                    "symbol": row["symbol"].strip().upper(),
                    "quantity": int(row["quantity"]),
                    "buy_price": float(row["buy_price"]),
                })
            except (KeyError, ValueError) as e:
                print(f"⚠️  Skipping invalid row: {row} ({e})")
    return holdings


def calculate_metrics(holdings: list[dict]) -> list[dict]:
    """Calculate investment, current value, and P/L for each holding."""
    results = []
    for h in holdings:
        symbol = h["symbol"]
        qty = h["quantity"]
        buy_price = h["buy_price"]
        current_price = CURRENT_PRICES.get(symbol)

        if current_price is None:
            print(f"⚠️  No market price for {symbol}. Skipping.")
            continue

        invested = qty * buy_price
        current_value = qty * current_price
        profit_loss = current_value - invested
        pl_percent = (profit_loss / invested) * 100 if invested else 0

        results.append({
            "symbol": symbol,
            "quantity": qty,
            "buy_price": buy_price,
            "current_price": current_price,
            "invested": invested,
            "current_value": current_value,
            "profit_loss": profit_loss,
            "pl_percent": pl_percent,
        })
    return results


def print_report(results: list[dict]) -> None:
    """Print a nicely formatted report to the terminal."""
    if not results:
        print("⚠️  No valid holdings to report.")
        return

    print("\n" + "=" * 90)
    print("                    📊 STOCK PORTFOLIO REPORT")
    print("=" * 90)
    print(f"Generated: {datetime.now().strftime('%A, %d %B %Y %I:%M %p')}")
    print("-" * 90)

    header = (
        f"{'Symbol':<8} {'Qty':>5} {'Buy':>10} {'Current':>10} "
        f"{'Invested':>12} {'Value':>12} {'P/L':>12} {'%':>8}"
    )
    print(header)
    print("-" * 90)

    for r in results:
        sign = "+" if r["profit_loss"] >= 0 else ""
        print(
            f"{r['symbol']:<8} "
            f"{r['quantity']:>5} "
            f"{r['buy_price']:>10.2f} "
            f"{r['current_price']:>10.2f} "
            f"{r['invested']:>12.2f} "
            f"{r['current_value']:>12.2f} "
            f"{sign}{r['profit_loss']:>11.2f} "
            f"{sign}{r['pl_percent']:>6.2f}%"
        )

    print("-" * 90)

    total_invested = sum(r["invested"] for r in results)
    total_value = sum(r["current_value"] for r in results)
    total_pl = total_value - total_invested
    total_pl_pct = (total_pl / total_invested) * 100 if total_invested else 0

    sign = "+" if total_pl >= 0 else ""
    print(
        f"{'TOTAL':<8} {'':>5} {'':>10} {'':>10} "
        f"{total_invested:>12.2f} {total_value:>12.2f} "
        f"{sign}{total_pl:>11.2f} {sign}{total_pl_pct:>6.2f}%"
    )
    print("=" * 90 + "\n")


def save_report(results: list[dict], file_path: Path) -> None:
    """Save report to CSV file."""
    if not results:
        return

    file_path.parent.mkdir(parents=True, exist_ok=True)

    with open(file_path, "w", encoding="utf-8", newline="") as f:
        fieldnames = [
            "symbol", "quantity", "buy_price", "current_price",
            "invested", "current_value", "profit_loss", "pl_percent",
        ]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    print(f"✅ Report saved to: {file_path}")


def main():
    base_dir = Path(__file__).resolve().parent.parent
    input_file = base_dir / "data" / "stocks.csv"
    output_file = base_dir / "output" / "portfolio_report.csv"

    print("=" * 90)
    print("        📈 STOCK PORTFOLIO TRACKER - CodeAlpha Task 2")
    print("=" * 90)

    try:
        holdings = read_portfolio(input_file)
        results = calculate_metrics(holdings)
        print_report(results)
        save_report(results, output_file)

    except FileNotFoundError as e:
        print(f"❌ Error: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")


if __name__ == "__main__":
    main()