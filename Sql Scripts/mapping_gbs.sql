
-- Creating a sequence for manual observation id

create sequence omop_demo.observation_observation_id_seq
   owned by  omop_demo.observation.observation_id;
   
select setval(pg_get_serial_sequence('omop_demo.observation', 'observation_id'), max(observation_id))
from  omop_demo.observation;

--  Insert positive gbs results

insert into omop_demo.observation (	observation_id,
				person_id,
				observation_concept_id,
				observation_date,
				observation_datetime,
				observation_type_concept_id,
				value_as_string,
				value_as_concept_id,
				visit_occurrence_id)
select 
	nextval('omop_demo.observation_observation_id_seq'),
	id_baznat,
	4304821,
	record_date::date,
	record_date::timestamp,
	32817,
	'Positive',
	9191,
	event_baznat
from
	(select 
		*
	from
		temp.csv45
	where
		gbs_vagina = 'חיובי'
		or
		gbs_in_urine='חיובי') pos

-- Insert negative gbs results

insert into omop_demo.observation (	observation_id,
				person_id,
				observation_concept_id,
				observation_date,
				observation_datetime,
				observation_type_concept_id,
				value_as_string,
				value_as_concept_id,
				visit_occurrence_id)
select 
	nextval('omop_demo.observation_observation_id_seq'),
	id_baznat,
	4304821,
	record_date::date,
	record_date::timestamp,
	32817,
	'Negative',
	9189,
	event_baznat
from
	(select 
		*
	from
		temp.csv45
	where
		gbs_vagina = 'שלילי'
		or
		gbs_in_urine='שלילי') neg


-- Adding patients body temprature as a measurment

insert into omop_demo.measurement (	measurement_id,
				person_id,
				measurement_concept_id,
				measurement_date,
				measurement_datetime,
				measurement_type_concept_id,
				value_as_number,
				visit_occurrence_id)

select
	nextval('omop_demo.measurement_measurement_id_seq'),
	id_baznat,
	4302666,
	execution_date::date,
	execution_date::timestamp,
	32817,
	חום::double precision,
	event_baznat
from
	temp.csvsheet4
where
	(חום is not null);

