# ============================================================
# 0. IMPORT + LOAD DATA
# ============================================================

import pandas as pd
import numpy as np


# Load 9 file CSV
customers = pd.read_csv("olist_customers_dataset.csv")
geolocation = pd.read_csv("olist_geolocation_dataset.csv")
orders = pd.read_csv("olist_orders_dataset.csv")
order_items = pd.read_csv("olist_order_items_dataset.csv")
payments = pd.read_csv("olist_order_payments_dataset.csv")
reviews = pd.read_csv("olist_order_reviews_dataset.csv")
products = pd.read_csv("olist_products_dataset.csv")
sellers = pd.read_csv("olist_sellers_dataset.csv")
category_translation = pd.read_csv(
    "product_category_name_translation.csv"
)


# ============================================================
# 3.1 ĐÁNH GIÁ CHẤT LƯỢNG DỮ LIỆU
# NGƯỜI 1
# ============================================================

# 3.1.1 Kích thước dữ liệu

# TODO:
# Kiểm tra số dòng, số cột của từng bảng


# 3.1.2 Kiểu dữ liệu

# TODO:
# Kiểm tra dtype của các cột


# 3.1.3 Giá trị thiếu

# TODO:
# Kiểm tra missing values


# 3.1.4 Dữ liệu trùng lặp

# TODO:
# Kiểm tra duplicate toàn bộ dòng


# 3.1.5 Giá trị bất thường

# TODO:
# Kiểm tra các giá trị bất thường


# 3.1.6 Quan hệ giữa các bảng

# TODO:
# Kiểm tra PK / FK
# Ví dụ:
# order_items.order_id -> orders.order_id
# order_items.product_id -> products.product_id


# ============================================================
# 3.2 XỬ LÝ DỮ LIỆU TRÙNG LẶP
# NGƯỜI 1
# ============================================================

# 3.2.1 Duplicate toàn bộ dòng

# TODO:


# 3.2.2 Duplicate theo business key

# TODO:
# Xác định business key
# Ví dụ:
# order_id + order_item_id + product_id


# ============================================================
# 3.3 XỬ LÝ GIÁ TRỊ THIẾU
# NGƯỜI 2
# ============================================================

# 3.3.1 price

# TODO:


# 3.3.2 product_category

# TODO:


# 3.3.3 review

# TODO:


# 3.3.4 delivery date

# TODO:


# ============================================================
# 3.4 XỬ LÝ GIÁ TRỊ KHÔNG HỢP LỆ
# NGƯỜI 2
# ============================================================

# 3.4.1 price <= 0

# TODO:


# 3.4.2 review_score ngoài [1, 5]

# TODO:


# 3.4.3 Các giá trị số bất hợp lệ khác

# TODO:


# ============================================================
# 3.5 KIỂM TRA TÍNH NHẤT QUÁN
# NGƯỜI 3
# ============================================================

# 3.5.1 Purchase -> Approved

# TODO:


# 3.5.2 Purchase -> Delivery

# TODO:


# 3.5.3 Carrier -> Customer delivery

# TODO:


# 3.5.4 Referential integrity

# TODO:


# ============================================================
# 3.6 LỌC THEO QUY TẮC NGHIỆP VỤ
# NGƯỜI 3
# ============================================================

# 3.6.1 order_status = delivered

# TODO:


# 3.6.2 Chỉ giữ bản ghi đủ thông tin phục vụ phân tích

# TODO:


# ============================================================
# 4. CHUYỂN ĐỔI DỮ LIỆU
# NGƯỜI 1 + NGƯỜI 3
# ============================================================

# 4.1 Chuyển kiểu dữ liệu

# TODO:


# 4.2 Chuyển đổi ngày

# TODO:


# 4.3 Ghép các bảng

# TODO:


# 4.4 Xử lý quan hệ 1-N

# TODO:
# Payment
# Review
# Các bảng có nhiều dòng cho một order


# 4.5 Xác định grain

# TODO:
# Xác định:
# 1 dòng trong dataset cuối đại diện cho cái gì?


# 4.6 Aggregate

# TODO:
# Aggregate theo:
# product_category_name_english
# order_year
# order_month


# ============================================================
# 5. KỸ THUẬT ĐẶC TRƯNG
# NGƯỜI 2
# ============================================================

# 5.1 total_item_value

# TODO:


# 5.2 delivery_days

# TODO:


# 5.3 delivery_delay_days

# TODO:


# 5.4 log_price

# TODO:


# 5.5 price_deviation_pct

# TODO:


# 5.6 promo_proxy

# TODO:


# ============================================================
# 6. KIỂM TRA TÍNH HỢP LỆ
# CẢ 3 NGƯỜI
# ============================================================

# 6.1 Kiểm tra duplicate

# TODO:


# 6.2 Kiểm tra missing

# TODO:


# 6.3 Kiểm tra price

# TODO:


# 6.4 Kiểm tra category

# TODO:


# 6.5 Kiểm tra date logic

# TODO:


# 6.6 Kiểm tra feature

# TODO:


# 6.7 Xác nhận dataset cuối cùng

# TODO:


# ============================================================
# 7. EXPORT
# CẢ 3 NGƯỜI
# ============================================================

# TODO:
# Xuất dataset sạch

# TODO:
# Xuất dataset aggregate