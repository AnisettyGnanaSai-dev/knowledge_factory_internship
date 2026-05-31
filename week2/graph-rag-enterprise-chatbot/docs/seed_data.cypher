seed_data.cypher// =====================================================
// EMPLOYEES
// =====================================================

CREATE
(admin:Employee {
    id:"emp001",
    name:"Admin User",
    role:"admin",
    email:"admin@coastal7.com",
    clearance_level:"confidential"
}),

(dev:Employee {
    id:"emp002",
    name:"Developer User",
    role:"developer",
    email:"developer@coastal7.com",
    clearance_level:"confidential"
}),

(intern:Employee {
    id:"emp003",
    name:"Intern User",
    role:"intern",
    email:"intern@coastal7.com",
    clearance_level:"public"
}),

(client:Employee {
    id:"emp004",
    name:"Client User",
    role:"client",
    email:"client@company.com",
    clearance_level:"public"
});


// =====================================================
// PROJECTS
// =====================================================

CREATE

(project1:Project {
    id:"proj001",
    name:"GraphRAG Enterprise",
    status:"active",
    description:"Role based GraphRAG chatbot system",
    sensitivity_level:"confidential"
}),

(project2:Project {
    id:"proj002",
    name:"Customer Service Portal",
    status:"active",
    description:"Client facing service platform",
    sensitivity_level:"public"
});


// =====================================================
// TECHNOLOGIES
// =====================================================

CREATE

(tech1:Technology {
    id:"tech001",
    name:"Neo4j",
    category:"Graph Database",
    description:"Knowledge Graph Storage"
}),

(tech2:Technology {
    id:"tech002",
    name:"FastAPI",
    category:"Backend",
    description:"Python API Framework"
}),

(tech3:Technology {
    id:"tech003",
    name:"Gemini",
    category:"LLM",
    description:"Google Generative AI"
});


// =====================================================
// DOCUMENTS
// =====================================================

CREATE

(doc1:Document {
    id:"doc001",
    title:"Enterprise Security Policy",
    content:"Internal security architecture and credentials handling.",
    file_type:"pdf",
    sensitivity_level:"confidential",
    allowed_roles:["developer"]
}),

(doc2:Document {
    id:"doc002",
    title:"Intern Learning Guide",
    content:"Neo4j and GraphRAG onboarding material.",
    file_type:"pdf",
    sensitivity_level:"public",
    allowed_roles:["intern"]
}),

(doc3:Document {
    id:"doc003",
    title:"Client Service Brochure",
    content:"Overview of services provided by Coastal 7.",
    file_type:"pdf",
    sensitivity_level:"public",
    allowed_roles:["client"]
});


// =====================================================
// POLICIES
// =====================================================

CREATE

(policy1:Policy {
    id:"pol001",
    title:"Confidential Data Policy",
    content:"Employees must not expose confidential information.",
    category:"security",
    sensitivity_level:"confidential"
}),

(policy2:Policy {
    id:"pol002",
    title:"Access Control Policy",
    content:"Role based access must be enforced.",
    category:"security",
    sensitivity_level:"confidential"
});


// =====================================================
// SERVICES
// =====================================================

CREATE

(service1:Service {
    id:"srv001",
    name:"AI Consulting",
    description:"Enterprise AI transformation services",
    pricing:"5000 USD",
    sensitivity_level:"public"
}),

(service2:Service {
    id:"srv002",
    name:"GraphRAG Development",
    description:"Graph powered RAG implementation",
    pricing:"10000 USD",
    sensitivity_level:"public"
});


// =====================================================
// EMPLOYEE -> PROJECT
// =====================================================

MATCH (admin:Employee {id:"emp001"})
MATCH (dev:Employee {id:"emp002"})
MATCH (intern:Employee {id:"emp003"})
MATCH (client:Employee {id:"emp004"})
MATCH (p1:Project {id:"proj001"})
MATCH (p2:Project {id:"proj002"})

CREATE
(admin)-[:PART_OF]->(p1),
(dev)-[:PART_OF]->(p1),
(intern)-[:PART_OF]->(p1),
(client)-[:PART_OF]->(p2);


// =====================================================
// MENTORSHIP
// =====================================================

MATCH (dev:Employee {id:"emp002"})
MATCH (intern:Employee {id:"emp003"})

CREATE
(intern)-[:MENTORED_BY]->(dev);


// =====================================================
// ACCESS RELATIONS
// =====================================================

MATCH (dev:Employee {id:"emp002"})
MATCH (intern:Employee {id:"emp003"})
MATCH (client:Employee {id:"emp004"})

MATCH (doc1:Document {id:"doc001"})
MATCH (doc2:Document {id:"doc002"})
MATCH (doc3:Document {id:"doc003"})

CREATE
(dev)-[:HAS_ACCESS_TO {level:"write"}]->(doc1),

(intern)-[:HAS_ACCESS_TO {level:"read"}]->(doc2),

(client)-[:HAS_ACCESS_TO {level:"read"}]->(doc3);


// =====================================================
// PROJECT -> TECHNOLOGY
// =====================================================

MATCH (p1:Project {id:"proj001"})
MATCH (p2:Project {id:"proj002"})

MATCH (neo4j:Technology {id:"tech001"})
MATCH (fastapi:Technology {id:"tech002"})
MATCH (gemini:Technology {id:"tech003"})

CREATE

(p1)-[:USES]->(neo4j),
(p1)-[:USES]->(fastapi),
(p1)-[:USES]->(gemini),

(p2)-[:USES]->(fastapi);


// =====================================================
// DOCUMENT -> PROJECT
// =====================================================

MATCH (doc1:Document {id:"doc001"})
MATCH (doc2:Document {id:"doc002"})
MATCH (doc3:Document {id:"doc003"})

MATCH (p1:Project {id:"proj001"})
MATCH (p2:Project {id:"proj002"})

CREATE

(doc1)-[:DESCRIBES]->(p1),
(doc2)-[:DESCRIBES]->(p1),
(doc3)-[:DESCRIBES]->(p2);


// =====================================================
// POLICY -> EMPLOYEE
// =====================================================

MATCH (policy1:Policy {id:"pol001"})
MATCH (policy2:Policy {id:"pol002"})

MATCH (dev:Employee {id:"emp002"})
MATCH (intern:Employee {id:"emp003"})

CREATE

(policy1)-[:APPLIES_TO]->(dev),
(policy2)-[:APPLIES_TO]->(intern);


// =====================================================
// SERVICE -> PROJECT
// =====================================================

MATCH (service1:Service {id:"srv001"})
MATCH (service2:Service {id:"srv002"})

MATCH (p2:Project {id:"proj002"})

CREATE

(service1)-[:OFFERED_BY]->(p2),
(service2)-[:OFFERED_BY]->(p2);