# Hello, lexicom

docker-compose build 
docker-compose up -d

UPDATE full_names
-- SET status = short_names.status
-- FROM 
-- WHERE full_names.name LIKE short_names.name || '%';

SELECT full_names.name, short_names.status
FROM full_names
left JOIN short_names ON full_names.name like short_names.name || '%';