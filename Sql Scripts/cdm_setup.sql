INSERT INTO ohdsi.source (source_id, source_name, source_key, source_connection, source_dialect) 
SELECT nextval('ohdsi.source_sequence'), 'Hadassha CDM', 'omop_demo', 'jdbc:postgresql://132.72.65.168:5432/Hadassah?user=ayalonaz&password=ayalonA3', 'postgresql';

INSERT INTO ohdsi.source_daimon (source_daimon_id, source_id, daimon_type, table_qualifier, priority) 
SELECT nextval('ohdsi.source_daimon_sequence'), source_id, 0, 'cdm', 0
FROM ohdsi.source
WHERE source_key = 'omop_demo'
;

INSERT INTO ohdsi.source_daimon (source_daimon_id, source_id, daimon_type, table_qualifier, priority) 
SELECT nextval('ohdsi.source_daimon_sequence'), source_id, 1, 'vocab', 1
FROM ohdsi.source
WHERE source_key = 'omop_demo'
;

INSERT INTO ohdsi.source_daimon (source_daimon_id, source_id, daimon_type, table_qualifier, priority) 
SELECT nextval('ohdsi.source_daimon_sequence'), source_id, 2, 'results', 1
FROM ohdsi.source
WHERE source_key = 'omop_demo'
;

INSERT INTO ohdsi.source_daimon (source_daimon_id, source_id, daimon_type, table_qualifier, priority) 
SELECT nextval('ohdsi.source_daimon_sequence'), source_id, 5, 'temp', 0
FROM ohdsi.source
WHERE source_key = 'omop_demo'
;