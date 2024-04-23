# SQL

### Section One: MCQ

1. B
2. B
3. D
4. B
5. A

### Section Two:
1.
SELECT patient_id, COUNT(*) AS admission_count
FROM admissions
WHERE department_id = (SELECT department_id FROM departments WHERE department_name = "Cardiology")
AND admission_date >= '2015-01-01'
GROUP BY patient_id
ORDER BY admission_count DESC
LIMIT 1;

The code should not include a reference to blank department_name entries as this will return any department IDs that don't have a name.  Although this should not happen in a well managed database, where department_id would be the primary key of the table it would be sensible to remove this reference:

2.
To improve the code:
- The department table should be included in the query as a join rather than a subquery as this would make the code easier to read and would also be more efficient as the database would not have to run the subquery first.
- The patient name should also be included in the query in order to make the output more useful to the people using it.  This may also need other data to be included, such as their address or their consultant.
- The query is currently only limited to the patient with the highest number of admissions.  To get a better understanding of the data for 8500 patients it should be expanded to more patients, such as the top 100.  This would enable trends in the data to be seen.

