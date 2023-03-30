# ===================================================================================
# How to Integrate a Dimension table. In other words, how to look-up Foreign Key
# values FROM a dimension table and add them to new Fact table columns.
#
# First, go to Edit -> Preferences -> SQL Editor and disable 'Safe Edits'.
# Close SQL Workbench and Reconnect to the Server Instance.
# ===================================================================================

USE wahoo_nation_vehicles;

# first, convert text dates to date type
ALTER TABLE wahoo_nation_vehicles.sales
MODIFY COLUMN order_date DATE;

# ==============================================================
# Step 1: Add New Column(s)
# ==============================================================
ALTER TABLE wahoo_nation_vehicles.sales
ADD COLUMN order_date_key int NOT NULL AFTER order_date;

# ==============================================================
# Step 2: Update New Column(s) with value from Dimension table
#         WHERE Business Keys in both tables match.
# ==============================================================
SET SQL_SAFE_UPDATES = 0;
UPDATE wahoo_nation_vehicles.sales AS fo
JOIN wahoo_nation_vehicles.sale_date_dim AS dd
ON DATE(fo.order_date) = dd.full_date
SET fo.order_date_key = dd.date_key;

# ==============================================================
# Step 3: Validate that newly updated columns contain valid data
# ==============================================================
SELECT order_date, order_date_key
FROM wahoo_nation_vehicles.sales
LIMIT 10;

# =============================================================
# Step 4: If values are correct then drop old column(s)
# =============================================================
ALTER TABLE wahoo_nation_vehicles.sales
DROP COLUMN order_date,

# =============================================================
# Step 5: Validate Finished Fact Table.
# =============================================================
SELECT * FROM wahoo_nation_vehicles.sales
LIMIT 10;
