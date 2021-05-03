create_airportCodes = """
CREATE TABLE IF NOT EXISTS airportCodes (
    ident        VARCHAR,
    name         VARCHAR,
    type         VARCHAR,
    local_code   VARCHAR,
    coordinates  VARCHAR,
    elevation_ft FLOAT,
    iso_country  VARCHAR,
    iso_region   VARCHAR,
    municipality VARCHAR,
    gps_code     VARCHAR,
    PRIMARY KEY (ident)
    
);
"""

drop_airportCodes = "DROP TABLE IF EXISTS airportCodes;"

airportCodes_insert = """
INSERT INTO airportCodes (ident, name, type, local_code, coordinates, elevation_ft,\
iso_country, iso_region, municipality, gps_code) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

create_demographic = """
CREATE TABLE IF NOT EXISTS demographics (
    city                   VARCHAR,
    state                  VARCHAR,
    media_age              FLOAT,
    male_population        FLOAT,
    female_population      FLOAT,
    total_population       FLOAT,
    num_veterans           FLOAT,
    foreign_born           FLOAT,
    average_household_size FLOAT,
    state_code             VARCHAR(2),
    race                   VARCHAR,
    count                  FLOAT
);
"""

drop_demographic = "DROP TABLE IF EXISTS demographics;"

demographic_insert = """
INSERT INTO demographics VALUES (%s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s)"""

create_immigration = """
CREATE TABLE IF NOT EXISTS immigration (
    cicid    FLOAT PRIMARY KEY,
    year     FLOAT,
    month    FLOAT,
    cit      FLOAT,
    res      FLOAT,
    port     VARCHAR(45),
    arrdate  FLOAT,
    mode     FLOAT,
    addr     VARCHAR,
    depdate  FLOAT,
    bir      FLOAT,
    count    FLOAT,
    dtadfile VARCHAR,
    entdepa  VARCHAR,
    entdepd  VARCHAR,
    matflag  VARCHAR,
    biryear  FLOAT,
    dtaddto  VARCHAR,
    gender   VARCHAR,
    airline  VARCHAR,
    admnum   FLOAT,
    fltno    VARCHAR,
    visatype VARCHAR
);
"""

drop_immigration = "DROP TABLE IF EXISTS immigration;"

immigration_insert = ("""
INSERT INTO immigration (cicid, year, month, cit, res, port, arrdate, mode, addr, depdate, bir,count, dtadfile, \
entdepa, entdepd, matflag, biryear, dtaddto, gender, airline, admnum, fltno, visatype) \
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)""")

create_temperature = """
CREATE TABLE IF NOT EXISTS temperature (
    timestamp                      DATE,
    average_temperature            FLOAT,
    average_temperature_uncertainty FLOAT,
    city                           VARCHAR,
    country                        VARCHAR,
    latitude                       VARCHAR,
    longitude                      VARCHAR
);
"""

temperature_insert = ("""
INSERT INTO temperature  VALUES (%s, %s, %s, %s, %s, %s, %s)""")

drop_temperature = "DROP TABLE IF EXISTS temperature;"


create_table_queries = [create_airportCodes, create_demographic, create_immigration, create_temperature]
drop_table_queries = [drop_airportCodes, drop_demographic, drop_immigration, drop_temperature]
