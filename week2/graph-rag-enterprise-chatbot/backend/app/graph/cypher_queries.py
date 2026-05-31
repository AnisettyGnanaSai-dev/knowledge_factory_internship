ADMIN_QUERY = """
MATCH (n)
RETURN n
LIMIT 25
"""


DEVELOPER_QUERY = """
MATCH (d:Document)
WHERE 'developer' IN d.allowed_roles

RETURN
d.title AS title,
d.content AS content,
d.sensitivity_level AS sensitivity
LIMIT 25
"""


INTERN_QUERY = """
MATCH (d:Document)
WHERE 'intern' IN d.allowed_roles

RETURN
d.title AS title,
d.content AS content,
d.sensitivity_level AS sensitivity
LIMIT 25
"""


CLIENT_QUERY = """
MATCH (d:Document)
WHERE 'client' IN d.allowed_roles

RETURN
d.title AS title,
d.content AS content,
d.sensitivity_level AS sensitivity
LIMIT 25
"""