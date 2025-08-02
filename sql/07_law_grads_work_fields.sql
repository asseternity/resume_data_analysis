SELECT
    edu.person_id,
    edu.program,
    exp.title,
    CASE
    -- Legal (first to avoid misclassification as Software or Other)
    WHEN exp.title LIKE '%lawye%'
      OR exp.title LIKE '%attorne%'
      OR exp.title LIKE '%legal%'
      OR exp.title LIKE '%paralega%'
      OR exp.title LIKE '%solicito%'
      OR exp.title LIKE '%barriste%'
      OR exp.title LIKE '%counsel%'
      OR exp.title LIKE '%juris%'
      OR exp.title LIKE '%llm%'
      OR exp.title LIKE '%llb%'
      OR exp.title LIKE '%jd%'
      OR exp.title LIKE '%regulatory%'
      OR exp.title LIKE '%compliance%'
      OR exp.title LIKE '%ethics%'
      OR exp.title LIKE '%policy advis%'
      OR exp.title LIKE '%public policy%'
      OR exp.title LIKE '%general counsel%' THEN 'Legal'

    -- Business & Consulting
    WHEN exp.title LIKE '%business analys%'
      OR exp.title LIKE '%strategy%'
      OR exp.title LIKE '%consultan%'
      OR exp.title LIKE '%business development%' THEN 'Business & Consulting'

    -- Management
    WHEN exp.title LIKE '%manager%'
      OR exp.title LIKE '%project lead%'
      OR exp.title LIKE '%product manager%'
      OR exp.title LIKE '%executive%'
      OR exp.title LIKE '%director%'
      OR exp.title LIKE '%vp of%'
      OR exp.title LIKE '%supervisor%'
      OR exp.title LIKE '%scrum master%'
      OR exp.title LIKE '%head of%' THEN 'Management'

    -- Human Resources
    WHEN exp.title LIKE '%recruite%'
      OR exp.title LIKE '%talent%'
      OR exp.title LIKE '%human resources%'
      OR exp.title LIKE '%hr%' THEN 'Human Resources'

    -- Accounting & Finance
    WHEN exp.title LIKE '%accountan%'
      OR exp.title LIKE '%finance%'
      OR exp.title LIKE '%financial%'
      OR exp.title LIKE '%audito%'
      OR exp.title LIKE '%controlle%' THEN 'Accounting & Finance'

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
      OR exp.title LIKE '%front end%'
      OR exp.title LIKE '%back-end%'
      OR exp.title LIKE '%back end%'
      OR exp.title LIKE '%full-stack%'
      OR exp.title LIKE '%programme%'
      OR exp.title LIKE '%devops%'
      OR exp.title LIKE '%qa enginee%'
      OR exp.title LIKE '%it security%'
      OR exp.title LIKE '%it specialis%'
      OR exp.title LIKE '%cloud%'
      OR exp.title LIKE '%cyber%'
      OR exp.title LIKE '%systems analys%'
      OR exp.title LIKE '%technical suppor%'
      OR exp.title LIKE '%information security analys%'
      OR exp.title LIKE '%it analys%'
      OR exp.title LIKE '%network engine%'
      OR exp.title LIKE '%web develope%'
      OR exp.title LIKE '%it suppor%'
      OR exp.title LIKE '%system admin%' THEN 'Software & IT'

    -- Marketing & Communications
    WHEN exp.title LIKE '%marketing%'
      OR exp.title LIKE '%communications%'
      OR exp.title LIKE '%social media%'
      OR exp.title LIKE '%pr%'
      OR exp.title LIKE '%brand%' THEN 'Marketing & Communications'

    -- Sales
    WHEN exp.title LIKE '%sales%'
      OR exp.title LIKE '%account executive%'
      OR exp.title LIKE '%business development%' THEN 'Sales'

    -- Education & Volunteering
    WHEN exp.title LIKE '%teache%'
      OR exp.title LIKE '%educato%'
      OR exp.title LIKE '%lecture%'
      OR exp.title LIKE '%professo%'
      OR exp.title LIKE '%voluntee%'
      OR exp.title LIKE '%tuto%' THEN 'Education & Volunteering'

    -- Administrative
    WHEN exp.title LIKE '%admin%'
      OR exp.title LIKE '%assistant%'
      OR exp.title LIKE '%office manage%'
      OR exp.title LIKE '%secretar%' THEN 'Administrative'

    -- Design and UX/UI
    WHEN exp.title LIKE '%ux%'
      OR exp.title LIKE '%ui designe%'
      OR exp.title LIKE '%product designe%'
      OR exp.title LIKE '%graphic designe%'
      OR exp.title LIKE '%visual designe%' THEN 'Design & UX/UI'

    -- Armed Security
    WHEN exp.title LIKE '%armed%'
      OR exp.title LIKE '%enforcemen%'
      OR exp.title LIKE '%security guard%' THEN 'Armed Security'

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
