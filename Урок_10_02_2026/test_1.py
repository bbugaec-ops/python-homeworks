#кількісь замовлень

("""SELECT client_id, COUNT(*) AS orders_count
FROM orders
GROUP BY client_id;
""")

# середня сума
("""SELECT client_id, AVG(total_price) AS avg_order_amount
FROM orders
GROUP BY client_id;
                  """)

# вся сума продажів
("""SELECT date(order_date) AS order_day, SUM(total_price) AS total_sales
FROM orders
GROUP BY date(order_date)
ORDER BY order_day; 
   """)


# три товари з найбільшою ціною
("""SELECT p.name, SUM(o.total_price) AS total_sales
FROM orders o
JOIN products p ON p.id = o.product_id
GROUP BY p.name
ORDER BY total_sales DESC
LIMIT 3;
 """)