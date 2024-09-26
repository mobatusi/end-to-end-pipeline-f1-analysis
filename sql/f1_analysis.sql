-- f1_analysis.sql: Transformation logic
DROP TABLE IF EXISTS f1_analysis.f1_result;

CREATE TABLE IF NOT EXISTS f1_analysis.f1_result (
    result_id INTEGER,
    race_id INTEGER,
    race_name STRING,
    race_year INTEGER,
    race_date DATE,
    driver_id INTEGER,
    driver_forename STRING,
    driver_surname STRING,
    constructor_id INTEGER,
    constructor_name STRING,
    circuit_id INTEGER,
    circuit_name STRING,
    circuit_location STRING,
    points FLOAT64
);

MERGE INTO f1_analysis.f1_result AS dst
USING (
select 
    resultId              as result_id
    , results.raceId      as race_id
    , races.name          as race_name
    , races.year          as race_year
    , races.date          as race_date
    , results.driverId    as driver_id
    , drivers.forename    as driver_forename
    , drivers.surname     as driver_surname
    , results.constructorId  as constructor_id
    , constructors.name      as constructor_name
    , circuits.circuitId     as circuit_id
    , circuits.name          as circuit_name
    , circuits.location      as circuit_location
    , results.points         as points

    from f1_analysis.results
    left join f1_analysis.races using (raceId)
    left join f1_analysis.drivers using (driverId)
    left join f1_analysis.constructors using (constructorId)
    left join f1_analysis.circuits using (circuitId)
) AS src
ON dst.result_id = src.result_id
WHEN MATCHED THEN DELETE
WHEN NOT MATCHED THEN
    INSERT (result_id, race_id, race_name, race_year, race_date, driver_id, driver_forename, driver_surname, constructor_id, constructor_name, circuit_id, circuit_name, circuit_location, points)
    VALUES (result_id, race_id, race_name, race_year, race_date, driver_id, driver_forename, driver_surname, constructor_id, constructor_name, circuit_id, circuit_name, circuit_location, points)