SELECT
    exp.person_id,
    exp.title,
    edu.program,
    CASE
        WHEN edu.program LIKE '%computer science%' THEN 'Computer Science'
        WHEN edu.program LIKE '%law%'
        OR edu.program LIKE '%legal%'
        OR edu.program LIKE '%jurisprudence%' THEN 'Law'
        WHEN edu.program IS NULL
        OR edu.program = 'Unknown' THEN 'Unknown'
        ELSE 'Other'
    END AS 'degree'
FROM
    experience_table_clean AS exp
    JOIN education_table_clean AS edu ON exp.person_id = edu.person_id
WHERE
    exp.title LIKE '%developer'
    OR exp.title LIKE '%software%'
    OR exp.title LIKE '%programmer%'
    OR exp.title LIKE '%devops%'