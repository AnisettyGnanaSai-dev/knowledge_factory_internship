// =====================================
// CONSTRAINTS
// =====================================

CREATE CONSTRAINT employee_id IF NOT EXISTS
FOR (e:Employee)
REQUIRE e.id IS UNIQUE;

CREATE CONSTRAINT document_id IF NOT EXISTS
FOR (d:Document)
REQUIRE d.id IS UNIQUE;

CREATE CONSTRAINT project_id IF NOT EXISTS
FOR (p:Project)
REQUIRE p.id IS UNIQUE;

CREATE CONSTRAINT technology_id IF NOT EXISTS
FOR (t:Technology)
REQUIRE t.id IS UNIQUE;

CREATE CONSTRAINT policy_id IF NOT EXISTS
FOR (p:Policy)
REQUIRE p.id IS UNIQUE;

CREATE CONSTRAINT service_id IF NOT EXISTS
FOR (s:Service)
REQUIRE s.id IS UNIQUE;


// =====================================
// INDEXES
// =====================================

CREATE INDEX employee_role IF NOT EXISTS
FOR (e:Employee)
ON (e.role);

CREATE INDEX document_sensitivity IF NOT EXISTS
FOR (d:Document)
ON (d.sensitivity_level);

CREATE INDEX document_title IF NOT EXISTS
FOR (d:Document)
ON (d.title);

CREATE INDEX project_name IF NOT EXISTS
FOR (p:Project)
ON (p.name);

CREATE INDEX technology_name IF NOT EXISTS
FOR (t:Technology)
ON (t.name);

CREATE INDEX policy_title IF NOT EXISTS
FOR (p:Policy)
ON (p.title);

CREATE INDEX service_name IF NOT EXISTS
FOR (s:Service)
ON (s.name);