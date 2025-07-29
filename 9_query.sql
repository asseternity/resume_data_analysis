SELECT
    edu.person_id,
    edu.program,
    exp.title,
    CASE
        -- Data Science and AI
        WHEN exp.title LIKE '%data scientis%'
          OR exp.title LIKE '%data science%'
          OR exp.title LIKE '%data analys%'
          OR exp.title LIKE '%data analysi%'
          OR exp.title LIKE '%data enginee%'
          OR exp.title LIKE '%machine learning%'
          OR exp.title LIKE '%ml enginee%'
          OR exp.title LIKE '%ai enginee%'
          OR exp.title LIKE '%artificial intelli%' THEN 'Data Science & AI'

        -- Software and IT
        WHEN exp.title LIKE '%software%'
          OR exp.title LIKE '%frontend%'
          OR exp.title LIKE '%backend%'
          OR exp.title LIKE '%fullstack%'
          OR exp.title LIKE '%front-end%'
          OR exp.title LIKE '%back-end%'
          OR exp.title LIKE '%full-stack%'
          OR exp.title LIKE '%programme%'
          OR exp.title LIKE '%devops%'
          OR exp.title LIKE '%qa enginee%'
          OR exp.title LIKE '%cloud%'
          OR exp.title LIKE '%cyber%'
          OR exp.title LIKE '%web develope%'
          OR exp.title LIKE '%system admin%' THEN 'Software & IT'

        -- Legal
        WHEN exp.title LIKE '%lawye%'
          OR exp.title LIKE '%attorne%'
          OR exp.title LIKE '%legal%'
          OR exp.title LIKE '%paralega%'
          OR exp.title LIKE '%solicito%'
          OR exp.title LIKE '%barriste%' THEN 'Legal'

        -- Business & Consulting
        WHEN exp.title LIKE '%business analys%'
          OR exp.title LIKE '%strategy%'
          OR exp.title LIKE '%consultant%'
          OR exp.title LIKE '%business development%' THEN 'Business & Consulting'

        -- Management
        WHEN exp.title LIKE '%manager%'
          OR exp.title LIKE '%project lead%'
          OR exp.title LIKE '%product manager%'
          OR exp.title LIKE '%executive%'
          OR exp.title LIKE '%director%'
          OR exp.title LIKE '%head of%' THEN 'Management'

        -- Administrative
        WHEN exp.title LIKE '%admin%'
          OR exp.title LIKE '%assistant%'
          OR exp.title LIKE '%office manage%'
          OR exp.title LIKE '%secretar%' THEN 'Administrative'

        -- Education
        WHEN exp.title LIKE '%teache%'
          OR exp.title LIKE '%educato%'
          OR exp.title LIKE '%lecture%'
          OR exp.title LIKE '%professo%'
          OR exp.title LIKE '%tuto%' THEN 'Education'

        -- Accounting & Finance
        WHEN exp.title LIKE '%accountan%'
          OR exp.title LIKE '%finance%'
          OR exp.title LIKE '%financial%'
          OR exp.title LIKE '%audito%'
          OR exp.title LIKE '%controlle%' THEN 'Accounting & Finance'

        -- Marketing & Communications
        WHEN exp.title LIKE '%marketing%'
          OR exp.title LIKE '%communications%'
          OR exp.title LIKE '%social media%'
          OR exp.title LIKE '%pr%'
          OR exp.title LIKE '%brand%' THEN 'Marketing & Communications'

        -- Human Resources
        WHEN exp.title LIKE '%recruite%'
          OR exp.title LIKE '%talent%'
          OR exp.title LIKE '%human resources%'
          OR exp.title LIKE '%hr%' THEN 'Human Resources'

        -- Design and UX/UI
        WHEN exp.title LIKE '%ux%'
          OR exp.title LIKE '%ui designe%'
          OR exp.title LIKE '%product designe%'
          OR exp.title LIKE '%graphic designe%'
          OR exp.title LIKE '%visual designe%' THEN 'Design & UX/UI'

        -- Sales
        WHEN exp.title LIKE '%sales%'
          OR exp.title LIKE '%account executive%'
          OR exp.title LIKE '%business development%' THEN 'Sales'

        -- Unknown or not provided
        WHEN exp.title IS NULL 
          OR exp.title = 'unknown' THEN 'Unknown'

        -- Everything else
        ELSE 'Other'
    END AS 'field'
FROM
    education_table_clean AS edu
    JOIN experience_table_clean AS exp ON edu.person_id = exp.person_id
WHERE
    edu.program LIKE '%law%'
    OR edu.program LIKE '%legal%'
    OR edu.program LIKE '%juris%'
    OR edu.program LIKE '%llb'
    OR edu.program LIKE '%crimin%'
    OR edu.program LIKE '%justic%'
    OR edu.program LIKE '%llm'
    OR edu.program LIKE '%jd'
