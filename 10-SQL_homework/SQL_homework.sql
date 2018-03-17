SET SQL_SAFE_UPDATES = 0;

USE sakila;

## 1a
SELECT first_name, last_name 
FROM actor

##1b
SELECT (first_name,last_name) 
AS `Actor Name`
FROM actor;



ALTER TABLE actor
ADD `Actor Name` VARCHAR(20);

UPDATE TABLE actor 
SET `Actor Name` = first_name || last_name;


##2a 
SELECT actor_id,first_name,last_name
FROM actor
WHERE first_name LIKE 'Joe%' 

##2b
SELECT actor_id,first_name,last_name
FROM actor
WHERE last_name LIKE '%gen%';

##2c 
USE sakila;
SELECT last_name,first_name
FROM actor
WHERE last_name LIKE '%li%';

##2d
SELECT country_id, country
FROM country
WHERE country IN ('Afghanistan','Bangladesh','China');

##3a
ALTER TABLE actor
ADD middle_name VARCHAR(10);

SELECT * FROM actor;

##3b
ALTER TABLE actor
ALTER COLUMN last_name blob(10);


##3c
ALTER TABLE actor
DROP COLUMN middle_name;

SELECT * FROM actor;

##4a
SELECT COUNT(last_name) AS `CountofLastName`,last_name 
FROM actor
GROUP BY last_name;

## 4b
SELECT COUNT(last_name) AS `CountofLastName`,last_name 
FROM actor
GROUP BY last_name
HAVING COUNT(last_name) >= 2;

#4c
SELECT first_name, last_name
FROM actor
WHERE first_name = 'GROUCHO' AND last_name='WILLIAMS';


UPDATE actor
SET first_name = 'HARPO'
WHERE first_name = 'GROUCHO' AND last_name='WILLIAMS';

SELECT first_name FROM actor WHERE first_name = 'HARPO';

#4d 
UPDATE actor
SET first_name = 'GROUCHO'
WHERE first_name = 'HARPO' AND last_name='WILLIAMS';

#5a

CREATE DATABASE address

#6a
SELECT staff.first_name, staff.last_name, address.address
FROM staff
INNER JOIN address ON staff.address_id = address.address_id;

#6b 
SELECT staff.staff_id,staff.first_name,staff.last_name, SUM(payment.amount)
FROM staff
INNER JOIN payment 
ON payment.payment_date LIKE '2005-08-%'
AND staff.staff_id = payment.staff_id
GROUP BY staff.staff_id;

#6c 
SELECT film.title, COUNT(film_actor.actor_id) AS `actorcounts`
FROM film
INNER JOIN film_actor
ON film.film_id = film_actor.film_id
GROUP BY film.title;

#6d 
SELECT film.title, COUNT(inventory.film_id) AS `Film Counts`
FROM film
INNER JOIN inventory
ON film.title LIKE 'Hunchback Impossible'
AND film.film_id = inventory.film_id
GROUP BY film.title;

#6e
SELECT customer.last_name, SUM(payment.amount)
FROM customer
INNER JOIN payment 
ON customer.customer_id = payment.customer_id
GROUP BY customer.last_name;

#7a
SELECT title
FROM film
WHERE (title LIKE 'K%' OR title LIKE 'Q%') 
AND language_id =

(
	SELECT language_id 
    FROM language 
    WHERE name='English'
);

#7b 
SELECT first_name,last_name
FROM actor
WHERE actor_id IN
(
	SELECT actor_id
    FROM film_actor 
    WHERE film_id IN
    ( 
		SELECT film_id
        FROM film
        WHERE title = 'ALONE TRIP'
	)
);
		


#7c

SELECT email 
FROM customer
WHERE address_id IN
(
	
	SELECT address_id
    FROM address
    WHERE city_id IN
    
    (
		SELECT city_id
        FROM country
        WHERE country = 'Canada'
	)
);

#7d
SELECT title
FROM film
WHERE film_id IN
(
	SELECT film_id 
    FROM film_category
    WHERE category_id IN
    (
		SELECT category_id
        FROM category 
        WHERE name = 'Family'
	)
);


#7e 
SELECT  COUNT(film.film_id) AS 'Movie Counts', film.title 
FROM film
JOIN inventory ON film.film_id = inventory.film_id
JOIN rental ON inventory.inventory_id = rental.inventory_id
GROUP BY title
ORDER BY `Movie Counts` DESC;

#7g ????
SELECT store.store_id, payment.amount
FROM store
JOIN 

#7h
SELECT category.name AS 'Top 5 Genres' , SUM(payment.amount) 'Gross Revenue'
FROM category
JOIN film_category ON (category.category_id = film_category.film_id)
JOIN inventory ON (film_category.film_id = inventory.inventory_id)
JOIN rental ON (inventory.inventory_id = rental.inventory_id) 
JOIN payment on (rental.rental_id = payment.rental_id) 
GROUP BY category.name
ORDER BY `Gross Revenue` 
LIMIT 5;

#8a ?????
CREATE VIEW 'Top 5' AS SELECT 'Top 5 Genres' FROM 'Top 5 Genres';

#8b ??

DROP VIEW

