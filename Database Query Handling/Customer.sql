SELECT c.customer_id, c.name, SUM(od.quantity) AS total_books_purchased
FROM Customers c
JOIN Orders o ON c.customer_id = o.customer_id
JOIN OrderDetails od ON o.order_id = od.order_id
WHERE o.order_date >= DATE_SUB(CURDATE(), INTERVAL 1 YEAR)
GROUP BY c.customer_id, c.name
ORDER BY total_books_purchased DESC
LIMIT 5;
