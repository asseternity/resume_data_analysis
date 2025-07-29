SELECT
    exp.person_id,
    exp.title,
    edu.program,
    CASE
        WHEN edu.program LIKE "%law%"
        OR edu.program LIKE "%legal%"
        OR edu.program LIKE "%juris%"
        OR edu.program LIKE "%llb"
        OR edu.program LIKE '%crimin%'
        OR edu.program LIKE '%justic%'
        OR edu.program LIKE "%llb%"
        OR edu.program LIKE "llb"
        OR edu.program LIKE "llm"
        OR edu.program LIKE "llm%"
        OR edu.program LIKE "%llm"
        OR edu.program LIKE "%jd"
        OR edu.program LIKE "jd"
        OR edu.program LIKE "%jd%" THEN "Law"
        WHEN edu.program LIKE "%busines%"
        OR edu.program LIKE '%administrat%'
        OR edu.program LIKE "%economic%"
        OR edu.program LIKE '%account%'
        OR edu.program LIKE '%finan%'
        OR edu.program LIKE '%market%'
        OR edu.program LIKE '%commerce%'
        OR edu.program LIKE '%trade%'
        OR edu.program LIKE '%leadershi%'
        OR edu.program LIKE '%manage%'
        OR edu.program LIKE "%audi%" THEN "Business, Accounting and Audit"
        WHEN edu.program LIKE '%compute%'
        OR edu.program LIKE '%softwar%'
        OR edu.program LIKE '%cyber%'
        OR edu.program LIKE '%computing%'
        OR edu.program LIKE '%programmin%'
        OR edu.program LIKE '%developer%'
        OR edu.program LIKE '%information system%'
        OR edu.program LIKE '%information technolog%' THEN 'Computer Science and IT'
        WHEN edu.program LIKE '%data%' THEN 'Data and Databases'
        WHEN edu.program LIKE '%math%'
        OR edu.program LIKE '%physics%' THEN 'Math and Physics'
        WHEN edu.program LIKE '%religio%'
        OR edu.program LIKE '%theol%'
        OR edu.program LIKE '%psycholog%'
        OR edu.program LIKE '%cognitive%'
        OR edu.program LIKE '%philosoph%' THEN 'Psychology and Religion'
        WHEN edu.program LIKE '%health%'
        OR edu.program LIKE '%medic%'
        OR edu.program LIKE '%dentist%'
        OR edu.program LIKE '%nurs%'
        OR edu.program LIKE '%plant%'
        OR edu.program LIKE '%animal%'
        OR edu.program LIKE '%agricult%'
        OR edu.program LIKE '%chemistr%'
        OR edu.program LIKE '%biochem%'
        OR edu.program LIKE '%pharm%'
        OR edu.program LIKE '%bio%' THEN 'Chemistry, Biology, Bioengineering and Health'
        WHEN edu.program LIKE '%scien%' THEN 'Science'
        WHEN edu.program LIKE '%communicatio%' THEN 'Communications'
        WHEN edu.program LIKE '%architectur%'
        OR edu.program LIKE '%urban%'
        OR edu.program LIKE '%landscape%'
        OR edu.program LIKE '%interior%'
        OR edu.program LIKE '%civil%'
        OR edu.program LIKE '%constructio%'
        OR edu.program LIKE '%buildin%'
        OR edu.program LIKE '%mechani%'
        OR edu.program LIKE '%electr%' THEN 'Electrical & Construction Engineering'
        WHEN edu.program LIKE '%social%'
        OR edu.program LIKE '%journalis%'
        OR edu.program LIKE '%humanit%'
        OR edu.program LIKE '%political%'
        OR edu.program LIKE '%histor%'
        OR edu.program LIKE '%literatur%' THEN 'Political Science, History, Journalism and Literature'
        WHEN edu.program LIKE '%art%'
        OR edu.program LIKE '%music%'
        OR edu.program LIKE '%photograph%'
        OR edu.program LIKE '%theat%'
        OR edu.program LIKE '%desig%'
        OR edu.program LIKE '%film%' THEN 'Art, design, music and film'
        WHEN edu.program LIKE '%high schoo%'
        OR edu.program LIKE '%course%'
        OR edu.program LIKE '%certificat%' THEN 'High school, certificate or course'
        WHEN edu.program LIKE '%spanis%'
        OR edu.program LIKE '%englis%'
        OR edu.program LIKE '%languag%' THEN 'Languages'
        WHEN edu.program LIKE '%genera%' THEN 'General Studies'
        WHEN edu.program LIKE '%engineerin%' 
        OR edu.program LIKE '%aviatio%' THEN 'Other Engineering'
        WHEN edu.program IS NULL
        OR edu.program = 'unknown' THEN 'Unknown'
        ELSE "Other"
    END AS 'degree',
    CASE
        WHEN exp.title LIKE '%front-end%' 
        OR exp.title LIKE "%frontend%"  
        OR exp.title LIKE "%web develope%"  
        OR exp.title LIKE "%ux develope%"  
        OR exp.title LIKE "%ui develope%" THEN "Front-end"
        WHEN exp.title LIKE '%back-end%'   
        OR exp.title LIKE "%backend%"   
        OR exp.title LIKE "%.net%"   
        OR exp.title LIKE "%java %"   
        OR exp.title LIKE "%C++%" THEN "Back-end"
        WHEN exp.title LIKE '%full-stack develope%'    
        OR exp.title LIKE "%fullstack develope%" THEN "Full-stack"
        WHEN exp.title LIKE '%devops%' THEN "DevOps"
        WHEN  exp.title LIKE '%qa enginee%' THEN "QA"
        WHEN exp.title LIKE '%data enginee%'
        OR exp.title LIKE '%data scien%'
        OR exp.title LIKE '%data analy%' THEN "Data Science"
        WHEN exp.title LIKE '%cybersecurity%' THEN "Cyber Security"
        WHEN exp.title LIKE '%system admin%' THEN "System Administrator"
        WHEN exp.title LIKE '%machine learn%'
        OR exp.title LIKE '%artificial int%' THEN "AI & Machine Learning"
        WHEN exp.title IS NULL
        OR exp.title = 'unknown' THEN 'Unknown'
        ELSE "Other"
    END AS 'field'
FROM
    experience_table_clean AS exp
    JOIN education_table_clean AS edu ON exp.person_id = edu.person_id
WHERE
    exp.title LIKE '%developer'
    OR exp.title LIKE '%software%'
    OR exp.title LIKE '%frontend$'
    OR exp.title LIKE '%backend%'
    OR exp.title LIKE '%fullstack%'
    OR exp.title LIKE '%front-end%'
    OR exp.title LIKE '%back-end%'
    OR exp.title LIKE '%full-stack%'
    OR exp.title LIKE '%programme%'
    OR exp.title LIKE '%devops%'
    OR exp.title LIKE '%data enginee%'
    OR exp.title LIKE '%qa enginee%'
    OR exp.title LIKE '%ux/ui%'
    OR exp.title LIKE '%data scien%'
    OR exp.title LIKE '%data analy%'
    OR exp.title LIKE '%cloud%'
    OR exp.title LIKE '%cyber%'
    OR exp.title LIKE '%web develope%'
    OR exp.title LIKE '%system admin%'
    OR exp.title LIKE '%machine learn%'
    OR exp.title LIKE '%artificial int%'