import csv
from datetime import datetime

def load_data(filename):
    items = []
    with open(filename, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["daily_usage"] = float(row["daily_usage"])
            row["current_stock"] = float(row["current_stock"])
            row["next_delivery"] = datetime.strptime(row["next_delivery"], "%Y-%m-%d")
            items.append(row)
    return items

def days_until_stockout(item):
    if item["daily_usage"] == 0:
        return float("inf")
    return item["current_stock"] / item["daily_usage"]

def generate_report(items, safety_days=7):
    today = datetime.today()
    report = []
    report.append("MEDICINE STOCK-OUT EARLY WARNING REPORT")
    report.append(f"Generated on: {today.strftime('%Y-%m-%d')}")
    report.append("")

    for item in items:
        runout_days = days_until_stockout(item)
        delivery_days = (item["next_delivery"] - today).days

        report.append(f"Medicine: {item['name']}")
        report.append(f"  Current stock: {item['current_stock']}")
        report.append(f"  Daily usage: {item['daily_usage']}")
        report.append(f"  Estimated days until stock runs out: {runout_days:.1f}")
        report.append(f"  Days until next delivery: {delivery_days}")
        
        if runout_days < delivery_days:
            report.append("  WARNING: Stock will run out before next delivery.")
        elif runout_days < safety_days:
            report.append("  WARNING: Stock is below the safety threshold.")
        else:
            report.append("  Status: Sufficient for now.")

        report.append("")

    return "\n".join(report)

def main():
    filename = "sample_data.csv"
    items = load_data(filename)
    report = generate_report(items)
    print(report)

if __name__ == "__main__":
    main()
