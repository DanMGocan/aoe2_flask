/* Delete this in production */
DROP TABLE IF EXISTS units, civilizations, buildings, technologies;

CREATE TABLE units(
    name TEXT NOT NULL,
    civilization TEXT NOT NULL
);


CREATE TABLE civilizations();
CREATE TABLE buildings();
CREATE TABLE technologies();