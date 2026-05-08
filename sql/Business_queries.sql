SELECT SUM(weekly_sales) AS total_revenue
FROM retail_sales;


/* top 10 stories */

SELECT 
    store,
    SUM(weekly_sales) AS total_sales
FROM retail_sales
GROUP BY store
ORDER BY total_sales DESC
LIMIT 10;

/* Holiday sales impact */

SELECT 
    isholiday,
    AVG(weekly_sales) AS avg_sales
FROM retail_sales
GROUP BY isholiday;

/*Monthly sales trends */

SELECT 
    month,
    SUM(weekly_sales) AS monthly_sales
FROM retail_sales
GROUP BY month
ORDER BY month;