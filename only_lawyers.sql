SELECT
    exp.person_id,
    exp.title,
    edu.program,
    CASE 
        WHEN exp.title LIKE "%web%"
        OR exp.title LIKE "%front%"
        OR exp.title LIKE "%ui developer%"
        OR exp.title LIKE "%ux/ui%" THEN "Web development and Front-End"
        WHEN exp.title LIKE "%security%"
        OR exp.title LIKE "%forensic%"
        OR exp.title LIKE "%intelligence%"  
        OR exp.title LIKE "%protect%" THEN "Cyber Security"
        WHEN exp.title LIKE "%fullstack%"
        OR exp.title LIKE "%full-stack%" THEN "Full-Stack"
        WHEN exp.title LIKE "%back-end%"
        OR exp.title LIKE "%backend%" 
        OR exp.title LIKE "%java %" 
        OR exp.title LIKE "%.net%" THEN "Back-End"
        WHEN exp.title LIKE "%data%" 
        OR exp.title LIKE "%sql%"  
        OR exp.title LIKE "%dba%" THEN "Data & Databases"
        WHEN exp.title LIKE "%artifici%" 
        OR exp.title LIKE "ai%" THEN "AI"
        WHEN exp.title LIKE "%devops%" THEN "DevOps"
        WHEN exp.title LIKE "%qa%" THEN "QA"
        WHEN exp.title LIKE "%mobile%" THEN "Mobile developer"
        WHEN exp.title LIKE "%cloud%" 
        OR exp.title LIKE "%aws%" THEN "Cloud"
        WHEN exp.title LIKE "%manager%" 
        OR exp.title LIKE "%business analyst%"  
        OR exp.title LIKE "%owner%" THEN "Product Manager & Business Analyst"
        ELSE "Other"
    END AS 'field'
FROM
    experience_table_clean as exp
    JOIN education_table_clean as edu ON exp.person_id = edu.person_id
WHERE
    (
        exp.title LIKE '%developer%'
        OR exp.title LIKE '%software%'
        OR exp.title LIKE '%frontend%'
        OR exp.title LIKE '%backend%'
        OR exp.title LIKE '%fullstack%'
        OR exp.title LIKE '%front-end%'
        OR exp.title LIKE '%back-end%'
        OR exp.title LIKE '%full-stack%'
        OR exp.title LIKE '%programmer%'
        OR exp.title LIKE '%devops%'
        OR exp.title LIKE '%data engineer%'
        OR exp.title LIKE '%QA%'
        OR exp.title LIKE '%UX/UI%'
        OR exp.title LIKE '%data scien%'
        OR exp.title LIKE '%data anal%'
        OR exp.title LIKE '%cloud%'
        OR exp.title LIKE '%cyber%'
    ) AND (
        edu.program LIKE '%law%'
        OR edu.program LIKE '%legal%'
        OR edu.program LIKE '%juris%'
        OR edu.program LIKE '%attorney%'
        OR edu.program LIKE '%llb%'
        OR edu.program LIKE '%bllb%'
        OR edu.program LIKE '%jd%'
    )
