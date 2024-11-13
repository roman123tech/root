import csv

sales_data = {}
with open('sales_data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        region = row["Region"]
        item = row["Item"]
        count = int(row["Count"])

        if region not in sales_data:
            sales_data[region] = {"TV": 0, "computer": 0, "total": 0}
        
        sales_data[region][item] += count
        sales_data[region]["total"] += count

def calculate_weights(region, item):
    region_sales = sales_data[region][item]
    region_total_sales = sales_data[region]["total"]
    item_total_sales_both_regions = sum(sales_data[r][item] for r in sales_data)

    t_weight = (region_sales / region_total_sales * 100) if region_total_sales > 0 else 0
    d_weight = (region_sales / item_total_sales_both_regions * 100) if item_total_sales_both_regions > 0 else 0
    return t_weight, d_weight

table_data = []
regions = ["Europe", "North_America"]
for region in regions:
    row = [region, sales_data[region]["TV"], 0, 0, sales_data[region]["computer"], 0, 0]

    t_weight_tv, d_weight_tv = calculate_weights(region, "TV")
    row[2] = f"{t_weight_tv:.2f}%"
    row[3] = f"{d_weight_tv:.2f}%"

    t_weight_computer, d_weight_computer = calculate_weights(region, "computer")
    row[5] = f"{t_weight_computer:.2f}%"
    row[6] = f"{d_weight_computer:.2f}%"

    row.append(sales_data[region]["total"])
    row.append("100.00%")
    
    combined_d_weight = min(d_weight_tv + d_weight_computer, 100.00)
    row.append(f"{combined_d_weight:.2f}%")
    table_data.append(row)
combined_tv = sum(sales_data[region]["TV"] for region in sales_data)
combined_computer = sum(sales_data[region]["computer"] for region in sales_data)
combined_total = combined_tv + combined_computer
total_row = [
    "both_regions", 
    combined_tv, 
    "100.00%", 
    "100.00%", 
    combined_computer, 
    "100.00%", 
    "100.00%", 
    combined_total, 
    "100.00%", 
    "100.00%"
]
table_data.append(total_row)
headers = ["Location", "TV Count", "TV T-Weight", "TV D-Weight", "Computer Count", "Computer T-Weight", "Computer D-Weight", "Total Count", "Total T-Weight", "Total D-Weight"]
header_row = " | ".join(f"{header: <20}" for header in headers)
print(header_row)
print("-" * len(header_row))
for row in table_data:
    print(" | ".join(f"{str(item): <20}" for item in row))
