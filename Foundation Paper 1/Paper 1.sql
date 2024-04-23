USE properties;

SET SQL_SAFE_UPDATES = 0;

-- 1. Clean Data

UPDATE properties SET price = REPLACE(price, "$", "");

-- 2. Top Earning

SELECT company_name as "Company", SUM(price) AS " Total Price"
FROM properties
GROUP BY company_name
LIMIT 10;
 
 
-- 3. Family Friendly
 
SELECT property_id AS "Property Name", review_text "Review"
FROM reviews
WHERE review_text LIKE "%family%" OR review_text LIKE "%kid%";

-- 4. 
DELIMITER //
CREATE PROCEDURE most_expensive_property ()
BEGIN

SELECT city, MAX(price) AS "Maximum Price"
FROM properties
GROUP BY city;

END //
DELIMITER ;

-- 5.

SELECT property_id AS "Property ID", AVG(score) AS "Average Score"
FROM reviews
GROUP BY property_id
ORDER BY AVG(score) ASC
LIMIT 1;
