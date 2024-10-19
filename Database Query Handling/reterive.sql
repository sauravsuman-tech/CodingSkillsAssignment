SELECT b.book_id, b.title, SUM(od.quantity) AS total_quantity_ordered
FROM Books b
JOIN OrderDetails od ON b.book_id = od.book_id
GROUP BY b.book_id, b.title
HAVING total_quantity_ordered > 10
ORDER BY total_quantity_ordered DESC;
