create database universe;
\c universe;
CREATE TABLE galaxy (
galaxy_id SERIAL PRIMARY KEY,
name VARCHAR(255) UNIQUE NOT NULL,
description TEXT,
galaxy_types VARCHAR(100) NOT NULL,
age_in_millions_of_years INT NOT NULL,
has_life BOOLEAN
);
CREATE TABLE star (
    star_id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL,
    description TEXT,
    star_type VARCHAR(100) NOT NULL,
    age_in_millions_of_years INT NOT NULL,
    is_spherical BOOLEAN,
    galaxy_id INT REFERENCES galaxy(galaxy_id)
);

CREATE TABLE planet (
    planet_id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL,
    description TEXT,
    planet_types VARCHAR(100) NOT NULL,
    distance_from_earth NUMERIC NOT NULL,
    has_life BOOLEAN,
    star_id INT REFERENCES star(star_id)
);
CREATE TABLE moon (
    moon_id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL,
    description TEXT,
    is_spherical BOOLEAN,
    age_in_millions_of_years INT NOT NULL,
    planet_id INT REFERENCES planet(planet_id)
);
CREATE TABLE asteroid (
    asteroid_id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL,
    description TEXT,
    distance_from_earth NUMERIC NOT NULL,
    has_life BOOLEAN
);
INSERT INTO galaxy (name, description, galaxy_types, age_in_millions_of_years, has_life)
VALUES
    ('Milky Way', 'Spiral galaxy', 'Spiral', 13600, TRUE),
    ('Andromeda', 'Spiral galaxy', 'Spiral', 10100, TRUE),
    ('Triangulum', 'Spiral galaxy', 'Spiral', 12000, FALSE),
    ('Whirlpool', 'Spiral galaxy', 'Spiral', 8000, FALSE),
    ('Sombrero', 'Elliptical galaxy', 'Elliptical', 11000, FALSE),
    ('Pinwheel', 'Spiral galaxy', 'Spiral', 13000, TRUE);
	
INSERT INTO star (name, description, star_type, age_in_millions_of_years, is_spherical, galaxy_id)
VALUES
    ('Sun', 'Main-sequence star', 'G-Type', 4600, TRUE, 1),
    ('Betelgeuse', 'Red supergiant star', 'M-Type', 8000, TRUE, 2),
    ('Sirius', 'Binary star system', 'A-Type', 300, TRUE, 1),
    ('Vega', 'Main-sequence star', 'A-Type', 455, TRUE, 1),
    ('Rigel', 'Blue supergiant star', 'B-Type', 860, TRUE, 2),
    ('Aldebaran', 'Red giant star', 'K-Type', 6500, TRUE, 3);

INSERT INTO planet (name, description, planet_types, distance_from_earth, has_life, star_id)
VALUES
    ('Earth', 'Terrestrial planet', 'Terrestrial', 0, TRUE, 1),
    ('Mars', 'Terrestrial planet', 'Terrestrial', 0.0000158, FALSE, 1),
    ('Jupiter', 'Gas giant', 'Gas giant', 0.0000823, FALSE, 1),
    ('Saturn', 'Gas giant', 'Gas giant', 0.000152, FALSE, 1),
    ('Venus', 'Terrestrial planet', 'Terrestrial', 0.0000121, FALSE, 1),
    ('Mercury', 'Terrestrial planet', 'Terrestrial', 0.00004, FALSE, 1),
	('Pluto', 'Cold Planet', 'Terrestrial', 169, FALSE, 1),
    ('Proxima b', 'Exoplanet', 'Terrestrial', 4.24, FALSE, 3),
    ('Kepler-186f', 'Exoplanet', 'Terrestrial', 500, True, 3),
    ('TOI 700 d', 'Exoplanet', 'Terrestrial', 101.4, FALSE, 5),
    ('Trappist-1e', 'Exoplanet', 'Terrestrial', 39.6, FALSE, 2),
    ('GJ 1214 b', 'Exoplanet', 'Super-Earth', 42.3, FALSE, 4),
    ('HD 209458 b', 'Exoplanet', 'Gas giant', 150, FALSE, 5);

INSERT INTO moon (name, description, is_spherical, age_in_millions_of_years, planet_id)
VALUES
    ('Moon', 'Moon of Earth', TRUE, 4500, 1),
    ('Europa', 'Moon of Jupiter', TRUE, 4500, 3),
    ('Ganymede', 'Moon of Jupiter', TRUE, 4500, 3),
    ('Callisto', 'Moon of Jupiter', TRUE, 4500, 3),
    ('Io', 'Moon of Jupiter', TRUE, 4500, 3),
    ('Titan', 'Moon of Saturn', TRUE, 4500, 4),
    ('Enceladus', 'Moon of Saturn', TRUE, 4500, 4),
    ('Mimas', 'Moon of Saturn', TRUE, 4500, 4),
    ('Phobos', 'Moon of Mars', TRUE, 4500, 2),
    ('Deimos', 'Moon of Mars', TRUE, 4500, 2),
    ('Triton', 'Moon of Neptune', TRUE, 4500, 6),
    ('Oberon', 'Moon of Uranus', TRUE, 4500, 6),
    ('Umbriel', 'Moon of Uranus', TRUE, 4500, 6),
    ('Ariel', 'Moon of Uranus', TRUE, 4500, 6),
    ('Miranda', 'Moon of Uranus', TRUE, 4500, 6),
    ('Charon', 'Moon of Pluto', TRUE, 4500, 12),
    ('Hydra', 'Moon of Pluto', TRUE, 4500, 12),
    ('Nix', 'Moon of Pluto', TRUE, 4500, 12),
    ('Kerberos', 'Moon of Pluto', TRUE, 4500, 12),
    ('Styx', 'Moon of Pluto', TRUE, 4500, 12);

INSERT INTO asteroid (name, description, distance_from_earth, has_life)
VALUES
    ('Ceres', 'Dwarf planet in asteroid belt', 2.77, FALSE),
    ('Pallas', 'Asteroid in asteroid belt', 2.77, FALSE),
    ('Vesta', 'Asteroid in asteroid belt', 2.36, FALSE);
