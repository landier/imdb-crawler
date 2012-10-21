CREATE VIEW Node AS
(
  SELECT
    CONCAT("p", p.Id) AS Id,
    p.Name AS Label
  FROM Person p
  ORDER BY p.Id
)
UNION
(
  SELECT
    CONCAT("m", m.Id),
    m.Title
  FROM Movie m
  ORDER BY m.Id
)

CREATE VIEW Edge AS
(
  SELECT
    CONCAT("p", d.Person_id, "m", d.Movie_id) AS Id,
    "Director" AS Label,
    2*m.Rating AS Weight,
    CONCAT("p", d.Person_id) AS Source,
    CONCAT("m", d.Movie_id) AS Target
  FROM Director d
  INNER JOIN Movie m ON m.Id = d.Movie_id
  ORDER BY d.Id
)
UNION
(
    SELECT
    CONCAT("p", a.Person_id, "m", a.Movie_id) AS Id,
    "Actor" AS Label,
    m.Rating AS Weight,
    CONCAT("p", a.Person_id) AS Source,
    CONCAT("m", a.Movie_id) AS Target
  FROM Actor a
  INNER JOIN Movie m ON m.Id = a.Movie_id
  ORDER BY a.Id
)

CREATE View Casting AS
SELECT
  m.Title,
  p.Name,
  a.CharacterName
FROM Actor a
INNER JOIN Person p ON p.Id = a.Person_id
INNER JOIN Movie m ON m.Id = a.Movie_id;