# GP-FD-ONTOLOGY-AMEDEO-001-SPEC-A: AMEDEO Ontology Specification

**(🚨 GenAI Proposal Status Disclaimer: This document outlines the specification for a core system component based on prior inputs, many AI-generated. It requires rigorous review, technical validation, formal definition by ontology experts, and approval by authorized GAIA AIR personnel before implementation. Content is conceptual and subject to change.)**

**Document ID:** GP-FD-ONTOLOGY-AMEDEO-001-SPEC-A
**Part:** GP-FD (Program Foundations)
**Chapter:** ONTOLOGY-AMEDEO (AMEDEO Foundational Ontology)
**Subject:** 001 - Core Specification
**InfoCode:** SPEC
**Version:** 0.8 (Draft)
**Status:** Draft
**Classification:** Internal Use Only / Core Architectural Component
**Date:** 2023-10-26
**Author:** GAIA AIR Ontology Working Group (Synthesized by GenAI Assistant)

---

**Table of Contents**

1.  Introduction & Purpose
2.  Scope
3.  Definitions
4.  Core Ontological Concepts & Principles
5.  Structure & Representation Language
6.  Key Ontological Domains (Illustrative Examples)
    6.1. Ethics, Governance & Intent (CFSI Integration)
    6.2. System Structure & Function (AGIS/FFI Integration)
    6.3. Human Factors & Adaptation
    6.4. Operations, Resources & Regeneration (AGAD Integration)
    6.5. Data, Knowledge & Context (COAFI/Data Tectonics Integration)
7.  Relationship to Other GAIA AIR Systems
    7.1. COAFI
    7.2. AMPEL
    7.3. QAO & AI Core (i-Aher0)
    7.4. CFSI
    7.5. AGIS & FFI
8.  Governance & Maintenance
9.  Appendices
    9.1. Formal Representation Files (Placeholder)
    9.2. Visualization (Placeholder)

---

## 1. Introduction & Purpose

This document specifies the **AMEDEO (Active Meta-Ethical Dynamic Execution Ontology)**, the master semantic framework and shared conceptual model for the entire GAIA AIR ecosystem. AMEDEO serves as the program's "soul," providing a formal, machine-interpretable representation of core entities, relationships, rules, constraints, and ethical principles.

Its primary purposes are to:

*   Establish a **common, unambiguous understanding** of GAIA AIR concepts for both human stakeholders and autonomous systems (AI, QAO, AMPEL).
*   Provide the **semantic foundation** for structuring knowledge within COAFI.
*   Define the **operational semantics** used by runtime components like QAO and the AMPEL Runtime.
*   Codify and make operational the **ethical principles** derived from the CFSI.
*   Enable **advanced reasoning, context awareness, and dynamic adaptation** across the federated system.
*   Serve as the **stable semantic baseline** for navigating Data Tectonics.

AMEDEO is not merely a static data model; it is **Active** (used at runtime), **Meta-Ethical** (represents ethical rules), **Dynamic** (evolvable under governance), and directly informs **Execution**.

---

## 2. Scope

**In Scope:**

*   Formal definition of core GAIA AIR classes (concepts, entities).
*   Formal definition of properties (relationships, attributes) between classes.
*   Key axioms (logical statements) defining constraints and characteristics of classes and properties.
*   Formal representation of foundational ethical rules and principles derived from CFSI.
*   Core operational rules and semantics necessary for system-wide understanding and orchestration.
*   High-level structure for domain-specific ontological extensions (Air, Space, Robotics, Finance, etc.).
*   The controlled vocabulary and taxonomy used across GAIA AIR systems and documentation.

**Out of Scope:**

*   **Instance Data:** The detailed data about specific components, missions, users, etc. (This data *conforms* to AMEDEO's structure but resides within COAFI operational databases or knowledge graphs).
*   **Specific Implementation Details:** How systems like QAO or AMPEL *internally implement* the logic derived from AMEDEO (covered in their respective SDDs).
*   **The complete COAFI data storage schema** (AMEDEO defines the *meaning*, COAFI schemas define the *storage structure*).
*   **Detailed domain-specific ontologies** (These will be separate SPEC documents extending AMEDEO, e.g., `GP-AM-ONTOLOGY-AERO-001-SPEC-A`).

---

## 3. Definitions

*   **Ontology:** A formal, explicit specification of a shared conceptualization. Defines concepts, categories, properties, and relations for a domain.
*   **Class:** A category or type of entity (e.g., `Mission`, `Operator`, `EthicalConstraint`). Corresponds to TBox in Description Logics.
*   **Property:** A binary relation specifying attributes of classes or relationships between classes (e.g., `hasStatus`, `requiresSkill`, `isGovernedBy`). Corresponds to RBox.
    *   **Object Property:** Links instances of classes (e.g., `Operator performs Task`).
    *   **Data Property:** Links instances to literal values (e.g., `Component hasMassValue "10.5"`).
*   **Individual / Instance:** A specific object or entity belonging to a class (e.g., `Mission_Lunar_Cargo_Run_003` is an instance of `Mission`). Corresponds to ABox (though instance data largely lives outside this core spec).
*   **Axiom:** A logical statement assumed to be true within the ontology, defining constraints or deriving knowledge (e.g., "Every `SafetyCriticalFunction` must have an associated `VerificationProcedure`").
*   **Rule:** A logical implication (often IF-THEN) used for reasoning and deriving new information or triggering actions (e.g., using SWRL - Semantic Web Rule Language).
*   **Semantic Web Technologies:** Standards used for representing and reasoning with ontologies, potentially including:
    *   **RDF (Resource Description Framework):** Data model for representing information as triples (Subject-Predicate-Object).
    *   **OWL 2 (Web Ontology Language):** Rich language for defining complex classes, properties, and axioms, enabling automated reasoning.
    *   **SPARQL:** Query language for RDF data / knowledge graphs.
*   **Meta-Ethical:** Relating to the nature and definition of ethical concepts and principles themselves. AMEDEO represents these concepts formally.
*   **Dynamic:** Capable of evolving or changing over time (under strict governance).
*   **Execution Ontology:** An ontology specifically designed to be used by systems during runtime operation to inform decisions and actions.

---

## 4. Core Ontological Concepts & Principles

AMEDEO is built upon the following core concepts reflecting GAIA AIR's nature:

*   **Active & Runtime-Relevant:** Concepts and rules are designed to be directly queryable and usable by QAO, AMPEL Runtime, and AI Core during operations.
*   **Meta-Ethical Representation:** Formally models CFSI principles (`DignityOfIntent`, `EntanglementOfResponsibility`), ethical rules, consent states, and allows reasoning about ethical compliance.
*   **Dynamic Evolution:** While foundational, the ontology anticipates controlled evolution as GAIA AIR learns and adapts. Versioning and governance are critical.
*   **Human-Centricity:** Includes rich representations of `UserContext`, `OperatorProfile` (including `SkillLevel`, `Certification`, `Preferences`), `WellbeingState`, and `PTIMConfiguration` to enable adaptive interfaces and interactions.
*   **Federation & Agency:** Models `FederatedNode`, `Agent` (human/AI/robotic), `ConsensusProtocol`, `SharedResource`, `JurisdictionContext` (for Data Tectonics).
*   **Intentionality & Purpose:** Represents `Mission`, `Goal`, `Task`, `DeclaredIntent`, linking actions back to purpose (CFSI's Dignity of Intent).
*   **Regeneration & Sustainability (AGAD):** Models `AGADAxis`, `Resource`, `EnergyFlow`, `LifecyclePhase`, `EnvironmentalImpactMetric`, `RegenerativeProcess`.
*   **System Representation:** Integrates `GAIAComponent` (linked to AGIS), `SystemFunction` (linked to FFI), `InterfaceDefinition` (linked to ICDs), `OperationalMode`, `SystemState`.
*   **Knowledge & Provenance:** Models `COAFIDocument`, `DataSource`, `ConfidenceLevel`, `InformationLifecycle`, `VerificationStatus`, potentially linking to BITT hashes for critical data provenance.

---

## 5. Structure & Representation Language

*   **Formal Language:** AMEDEO shall be primarily represented using **OWL 2 DL (Web Ontology Language 2, Description Logic profile)**. This provides significant expressive power while retaining computational tractability for reasoning.
*   **Underlying Model:** RDF (Resource Description Framework) serves as the underlying data model.
*   **Query Language:** SPARQL shall be the standard language for querying AMEDEO-conformant knowledge graphs.
*   **Rules:** Where necessary, operational or inferential rules beyond OWL 2 DL's expressivity may be represented using **SWRL (Semantic Web Rule Language)** or similar compatible rule languages.
*   **Modularity:** AMEDEO is designed as a modular ontology:
    *   **AMEDEO-Core:** Defines the absolute foundational concepts, upper-level classes, core properties, and cross-domain relationships (this specification).
    *   **Domain Ontologies:** Separate, dependent ontologies extending AMEDEO-Core for specific GAIA AIR parts (e.g., `AMEDEO-Aero` for GP-AM, `AMEDEO-Space` for GP-SM, `AMEDEO-Robotics` for GP-RS, `AMEDEO-Finance` for AGAD/MOD-FIN). These are specified in separate documents.
*   **Key Structural Components:**
    *   **Classes (TBox):** A hierarchy of concepts representing entities in the GAIA AIR universe (e.g., `PhysicalObject`, `Agent`, `Process`, `InformationEntity`, `AbstractConcept`).
    *   **Properties (RBox):** Defines relationships (e.g., `partOf`, `implementsFunction`, `hasEthicalConstraint`, `requiresInputData`, `generatesOutput`) and attributes (e.g., `hasMass`, `hasStatus`, `hasTimestamp`). Properties will have defined domains and ranges.
    *   **Axioms:** Defines necessary and sufficient conditions for class membership, property characteristics (transitive, symmetric), constraints (cardinality), and logical relationships (disjointness).
    *   **(Implicit) Individuals (ABox):** While the core spec focuses on TBox/RBox, it defines the *types* of individuals expected in operational knowledge graphs.

---

## 6. Key Ontological Domains (Illustrative Examples)

This section illustrates how core GAIA AIR concepts are modeled within AMEDEO. (Note: These are simplified examples).

### 6.1. Ethics, Governance & Intent (CFSI Integration)

*   **Classes:** `CFSIPrinciple`, `EthicalRule`, `ConsentRecord`, `AgentIntent`, `ResponsibilityAssignment`, `DataJurisdiction`.
*   **Properties:** `governedBy` (linking `Action` to `EthicalRule`), `requiresConsentFrom` (linking `Action` to `Agent`), `intentOf` (linking `AgentIntent` to `Action`), `assignedResponsibility` (linking `Agent` to `Task`).
*   **Axioms/Rules:** "An `Action` requiring consent cannot proceed if `ConsentRecord.status` is 'Denied'." "Every `FederatedAction` must have an associated `ResponsibilityAssignment`."

### 6.2. System Structure & Function (AGIS/FFI Integration)

*   **Classes:** `GAIAComponent`, `SystemFunction`, `Interface`, `Requirement`, `OperationalMode`, `SystemState`.
*   **Properties:** `hasAGIS_ID` (linking `GAIAComponent` to Literal), `implementsFunction` (linking `GAIAComponent` to `SystemFunction`), `hasInterface` (linking `GAIAComponent` to `Interface`), `satisfiesRequirement` (linking `SystemFunction` or `GAIAComponent` to `Requirement`).
*   **Axioms/Rules:** Linking FFI Tiers, ensuring function allocation consistency.

### 6.3. Human Factors & Adaptation

*   **Classes:** `HumanAgent`, `OperatorProfile`, `Skill`, `Certification`, `WellbeingIndicator`, `PTIM`.
*   **Properties:** `hasSkillLevel` (linking `OperatorProfile` to `Skill`), `monitorsWellbeing` (linking `Sensor` to `HumanAgent`), `adaptsTo` (linking `PTIM` to `OperatorProfile`).
*   **Axioms/Rules:** "A `Task` requiring `Skill X Level 3` cannot be assigned to `OperatorProfile` lacking it." "If `WellbeingIndicator` crosses `Threshold Y`, trigger `Alert Z`."

### 6.4. Operations, Resources & Regeneration (AGAD Integration)

*   **Classes:** `OperationalTask`, `Resource`, `EnergySource`, `AGAD_Metric`, `LifecyclePhase`, `MOD_Instance`.
*   **Properties:** `consumesResource`, `producesResource`, `monitoredByMetric`, `operatesAccordingToAxis` (linking `Process` to `AGADAxis`).
*   **Axioms/Rules:** Defining resource flow constraints, triggering regenerative processes based on AGAD metrics.

### 6.5. Data, Knowledge & Context (COAFI/Data Tectonics Integration)

*   **Classes:** `COAFIDocument`, `DataSource`, `InformationAsset`, `SemanticTag`, `DataHandlingPolicy`, `GeopoliticalContext`.
*   **Properties:** `referencesDocument` (linking `SystemState` to `COAFIDocument`), `hasProvenance` (linking `InformationAsset` to `DataSource`), `subjectToPolicy` (linking `InformationAsset` to `DataHandlingPolicy`), `appliesInContext` (linking `DataHandlingPolicy` to `GeopoliticalContext`).
*   **Axioms/Rules:** Defining data access based on context and policy, associating COAFI metadata tags with formal ontology concepts.

### 6.6. APU Maintenance Safety and Ethics (AMEDEO-APU Integration)

*   **Classes:** `APUComponent`, `OperationalState`, `MaintenanceProcedure`, `SafetyCriticalComponent`, `CertificationRecord`, `Technician`.
*   **Properties:** `requiresCertification` (linking `MaintenanceProcedure` to `CertificationRecord`), `targetsComponent` (linking `MaintenanceProcedure` to `APUComponent`), `hasOperationalState` (linking `APUComponent` to `OperationalState`), `qualifiedTechnician` (linking `MaintenanceProcedure` to `Technician`).
*   **Axioms/Rules:** "A `MaintenanceProcedure` targeting a `SafetyCriticalComponent` must have an `Approved` `CertificationRecord`." "A `Technician` must be qualified for the `MaintenanceProcedure` they perform."

---

## 7. Relationship to Other GAIA AIR Systems

AMEDEO is deeply integrated and provides the semantic glue:

*   **7.1. COAFI:** AMEDEO defines the meaning and structure of concepts documented in COAFI. COAFI metadata (semantic tags) directly reference AMEDEO classes and properties, enabling semantic search and AI understanding of documentation.
*   **7.2. AMPEL:**
    *   **Semantic Validation:** Uses AMEDEO to understand the meaning of nouns, verbs, intentions in AMPEL code.
    *   **Ethical Core:** Evaluates AMPEL actions against ethical rules formalized in AMEDEO.
    *   **AMPIDE Agent:** Uses AMEDEO for contextual understanding and providing meaningful guidance.
    *   **AMEDEO Runtime:** Executes AMPEL commands within the rich semantic context maintained by the ontology.
*   **7.3. QAO & AI Core (i-Aher0):** Use AMEDEO extensively for:
    *   **Context Understanding:** Interpreting sensor data, mission goals, user states.
    *   **Problem Formulation:** Structuring complex problems (e.g., optimization) based on ontological relationships.
    *   **Decision Making:** Applying operational and ethical rules from AMEDEO.
    *   **Explainability (XAI):** Grounding explanations in shared ontological concepts.
*   **7.4. CFSI:** AMEDEO serves as the formal, operational representation of the abstract principles defined in the CFSI.
*   **7.5. AGIS & FFI:** AMEDEO provides the semantic layer connecting physical/logical components (AGIS IDs) with their intended functions (FIDs), constraints, and operational context.

---

## 8. Governance & Maintenance

*   **Stewardship:** Governed by the GAIA AIR Ontology Working Group (OWG), reporting to the GAIA AIR Architecture Board.
*   **Change Management:** Changes follow a rigorous process: Proposal -> Review by OWG -> Impact Analysis (potentially involving simulation via GACMS) -> Approval by Architecture Board -> Version Increment -> Deployment. Changes must maintain logical consistency and alignment with CFSI.
*   **Versioning:** AMEDEO uses semantic versioning. Systems consuming the ontology must declare compatibility with specific versions.
*   **Tooling:** Development and maintenance likely utilize tools like Protégé, enterprise graph databases (e.g., Neo4j, Stardog), OWL reasoners (e.g., Pellet, HermiT), and version control systems (Git).

---

## 9. Appendices

### 9.1. Formal Representation Files (Placeholder)

*   Link to AMEDEO-Core OWL/RDF file(s) in COAFI/Version Control System.

```owl
@prefix : <http://gaiaair.org/ontology/amedeo#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

<http://gaiaair.org/ontology/ameodeo>
    a owl:Ontology ;
    rdfs:label "AMEDEO Core Ontology v0.8" ;
    owl:versionInfo "v0.8" ;
    owl:imports <http://www.w3.org/2002/07/owl> .

### 🎯 Clases Ontológicas Principales

:Agente a owl:Class ;
    rdfs:label "Agente" ;
    rdfs:comment "Entidad capaz de tomar decisiones en el ecosistema GAIA AIR." .

:Intención a owl:Class ;
    rdfs:label "Intención" ;
    rdfs:comment "Proyección teleológica asociada al propósito de una acción." .

:Contexto a owl:Class ;
    rdfs:label "Contexto" ;
    rdfs:comment "Estado situacional que influye sobre la interpretación ética." .

:Ética a owl:Class ;
    rdfs:label "Ética" ;
    rdfs:comment "Marco normativo vinculado a intenciones, acciones y consecuencias." .

:Función a owl:Class ;
    rdfs:label "Función" ;
    rdfs:comment "Acción realizada por el sistema, trazable vía FFI y AGIS." .

:Responsabilidad a owl:Class ;
    rdfs:label "Responsabilidad" ;
    rdfs:comment "Grado de imputabilidad o rendición ética exigida a un agente." .

### 🔗 Propiedades de Objeto

:tieneIntención a owl:ObjectProperty ;
    rdfs:domain :Agente ;
    rdfs:range :Intención ;
    rdfs:label "tieneIntención" .

:operaEnContexto a owl:ObjectProperty ;
    rdfs:domain :Función ;
    rdfs:range :Contexto ;
    rdfs:label "operaEnContexto" .

:seRigePor a owl:ObjectProperty ;
    rdfs:domain :Función ;
    rdfs:range :Ética ;
    rdfs:label "seRigePor" .

:asume a owl:ObjectProperty ;
    rdfs:domain :Agente ;
    rdfs:range :Responsabilidad ;
    rdfs:label "asume" .

### 📊 Propiedades de Datos

:prioridadÉtica a owl:DatatypeProperty ;
    rdfs:domain :Intención ;
    rdfs:range xsd:decimal ;
    rdfs:label "prioridadÉtica" .

:nivelConfianza a owl:DatatypeProperty ;
    rdfs:domain :Función ;
    rdfs:range xsd:decimal ;
    rdfs:label "nivelConfianza" .

### ⚖️ Axiomas Ético-Funcionales (Ejemplo)

[ a owl:Restriction ;
  owl:onProperty :seRigePor ;
  owl:someValuesFrom :Ética ] .

[ a owl:Class ;
  owl:intersectionOf (
    :Función
    [ a owl:Restriction ; owl:onProperty :nivelConfianza ; owl:someValuesFrom xsd:decimal ]
  ) ;
  rdfs:label "Función éticamente validable" ] 

### AMEDEO-APU Ontology Extension

:APUComponent a owl:Class ;
    rdfs:label "APU Component" ;
    rdfs:comment "Components of the Auxiliary Power Unit (APU)." .

:OperationalState a owl:Class ;
    rdfs:label "Operational State" ;
    rdfs:comment "Operational states of the APU." .

:MaintenanceProcedure a owl:Class ;
    rdfs:label "Maintenance Procedure" ;
    rdfs:comment "Procedures for maintaining the APU." .

:SafetyCriticalComponent a owl:Class ;
    rdfs:label "Safety Critical Component" ;
    rdfs:comment "Components of the APU that are critical for safety." .

:CertificationRecord a owl:Class ;
    rdfs:label "Certification Record" ;
    rdfs:comment "Records of certifications for maintenance procedures." .

:Technician a owl:Class ;
    rdfs:label "Technician" ;
    rdfs:comment "Technicians qualified to perform maintenance procedures." .

:requiresCertification a owl:ObjectProperty ;
    rdfs:domain :MaintenanceProcedure ;
    rdfs:range :CertificationRecord ;
    rdfs:label "requires Certification" .

:targetsComponent a owl:ObjectProperty ;
    rdfs:domain :MaintenanceProcedure ;
    rdfs:range :APUComponent ;
    rdfs:label "targets Component" .

:hasOperationalState a owl:ObjectProperty ;
    rdfs:domain :APUComponent ;
    rdfs:range :OperationalState ;
    rdfs:label "has Operational State" .

:qualifiedTechnician a owl:ObjectProperty ;
    rdfs:domain :MaintenanceProcedure ;
    rdfs:range :Technician ;
    rdfs:label "qualified Technician" .

### SWRL Rules for AMEDEO-APU

[ a swrl:Imp ;
  swrl:body (
    [ a swrl:ClassAtom ;
      swrl:classPredicate :MaintenanceProcedure ;
      swrl:argument1 ?procedure
    ]
    [ a swrl:ClassAtom ;
      swrl:classPredicate :SafetyCriticalComponent ;
      swrl:argument1 ?component
    ]
    [ a swrl:PropertyAtom ;
      swrl:propertyPredicate :targetsComponent ;
      swrl:argument1 ?procedure ;
      swrl:argument2 ?component
    ]
    [ a swrl:PropertyAtom ;
      swrl:propertyPredicate :requiresCertification ;
      swrl:argument1 ?procedure ;
      swrl:argument2 ?cert
    ]
    [ a swrl:ClassAtom ;
      swrl:classPredicate :CertificationRecord ;
      swrl:argument1 ?cert
    ]
    [ a swrl:DataPropertyAtom ;
      swrl:propertyPredicate :status ;
      swrl:argument1 ?cert ;
      swrl:argument2 "Approved"
    ]
  ) ;
  swrl:head (
    [ a swrl:ClassAtom ;
      swrl:classPredicate :ValidProcedure ;
      swrl:argument1 ?procedure
    ]
  )
] .

[ a swrl:Imp ;
  swrl:body (
    [ a swrl:ClassAtom ;
      swrl:classPredicate :MaintenanceProcedure ;
      swrl:argument1 ?procedure
    ]
    [ a swrl:ClassAtom ;
      swrl:classPredicate :Technician ;
      swrl:argument1 ?technician
    ]
    [ a swrl:PropertyAtom ;
      swrl:propertyPredicate :qualifiedTechnician ;
      swrl:argument1 ?procedure ;
      swrl:argument2 ?technician
    ]
  ) ;
  swrl:head (
    [ a swrl:ClassAtom ;
      swrl:classPredicate :QualifiedProcedure ;
      swrl:argument1 ?procedure
    ]
  )
] .

```

*   Links to primary domain ontology files (as they are developed).

### 9.2. Visualization (Placeholder)

*   Conceptual diagrams illustrating key parts of the class hierarchy and property relationships. (Generated from ontology tools).

  ```python
from graphviz import Digraph

# Crear un grafo dirigido
dot = Digraph(comment='AMEDEO Ontology - Conceptual Diagram')

# Clases principales
classes = [
    "Agente", "Intención", "Contexto", "Ética", "Función", "Responsabilidad"
]

# Propiedades de objeto
object_properties = {
    "tieneIntención": ("Agente", "Intención"),
    "operaEnContexto": ("Función", "Contexto"),
    "seRigePor": ("Función", "Ética"),
    "asume": ("Agente", "Responsabilidad")
}

# Propiedades de datos (como etiquetas dentro de las clases destino)
data_properties = {
    "prioridadÉtica": "Intención",
    "nivelConfianza": "Función"
}

# Añadir nodos de clase
for cls in classes:
    dot.node(cls, cls, shape='box', style='filled', color='lightgrey')

# Añadir aristas de propiedades de objeto
for prop, (domain, range_) in object_properties.items():
    dot.edge(domain, range_, label=prop)

# Añadir nodos de propiedades de datos
for prop, domain in data_properties.items():
    dp_node = f"{prop} : xsd:decimal"
    dot.node(dp_node, dp_node, shape='note', color='lightblue')
    dot.edge(domain, dp_node, style='dashed')

# Renderizar el grafo
dot.render('/mnt/data/amedeo_ontology_diagram', format='png', cleanup=False)

# Mostrar imagen renderizada
'/mnt/data/amedeo_ontology_diagram.png'

---
<?xml version="1.0"?>
<rdf:RDF xmlns="http://gaiaair.org/ontology/amedeo-apu#"
     xml:base="http://gaiaair.org/ontology/amedeo-apu"
     xmlns:owl="http://www.w3.org/2002/07/owl#"
     xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
     xmlns:xml="http://www.w3.org/XML/1998/namespace"
     xmlns:xsd="http://www.w3.org/2001/XMLSchema#"
     xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
     xmlns:amedeo="http://gaiaair.org/ontology/amedeo#"
     xmlns:apu="http://gaiaair.org/ontology/amedeo-apu#">
    
    <owl:Ontology rdf:about="http://gaiaair.org/ontology/amedeo-apu">
        <owl:versionIRI rdf:resource="http://gaiaair.org/ontology/amedeo-apu/1.0"/>
        <owl:imports rdf:resource="http://gaiaair.org/ontology/amedeo"/>
        <rdfs:label>AMEDEO APU Extension</rdfs:label>
        <rdfs:comment>Extension of the AMEDEO core ontology for Auxiliary Power Unit (APU) maintenance, certification, and ethical safety enforcement</rdfs:comment>
        <owl:versionInfo>1.0</owl:versionInfo>
    </owl:Ontology>
    
    <!-- 
    ///////////////////////////////////////////////////////////////////////////////////////
    //
    // Classes
    //
    ///////////////////////////////////////////////////////////////////////////////////////
     -->
    
    <!-- http://gaiaair.org/ontology/amedeo-apu#APU -->
    <owl:Class rdf:about="http://gaiaair.org/ontology/amedeo-apu#APU">
        <rdfs:subClassOf rdf:resource="http://gaiaair.org/ontology/amedeo#GAIAComponent"/>
        <rdfs:label>APU</rdfs:label>
        <rdfs:comment>Auxiliary Power Unit - provides electrical power and compressed air to aircraft systems when main engines are not operating</rdfs:comment>
    </owl:Class>
    
    <!-- http://gaiaair.org/ontology/amedeo-apu#LRU -->
    <owl:Class rdf:about="http://gaiaair.org/ontology/amedeo-apu#LRU">
        <rdfs:subClassOf rdf:resource="http://gaiaair.org/ontology/amedeo#GAIAComponent"/>
        <rdfs:label>Line Replaceable Unit</rdfs:label>
        <rdfs:comment>A modular component designed to be replaced quickly at the operational level</rdfs:comment>
    </owl:Class>
    
    <!-- http://gaiaair.org/ontology/amedeo-apu#SafetyCriticalComponent -->
    <owl:Class rdf:about="http://gaiaair.org/ontology/amedeo-apu#SafetyCriticalComponent">
        <rdfs:subClassOf rdf:resource="http://gaiaair.org/ontology/amedeo#GAIAComponent"/>
        <rdfs:label>Safety Critical Component</rdfs:label>
        <rdfs:comment>A component whose failure could lead to hazardous or catastrophic conditions</rdfs:comment>
    </owl:Class>
    
    <!-- http://gaiaair.org/ontology/amedeo-apu#BleedAirControlValve -->
    <owl:Class rdf:about="http://gaiaair.org/ontology/amedeo-apu#BleedAirControlValve">
        <rdfs:subClassOf rdf:resource="http://gaiaair.org/ontology/amedeo-apu#LRU"/>
        <rdfs:subClassOf rdf:resource="http://gaiaair.org/ontology/amedeo-apu#SafetyCriticalComponent"/>
        <rdfs:label>Bleed Air Control Valve</rdfs:label>
        <rdfs:comment>Controls the flow of compressed air from the APU to aircraft systems</rdfs:comment>
    </owl:Class>
    
    <!-- http://gaiaair.org/ontology/amedeo-apu#GeneratorControlUnit -->
    <owl:Class rdf:about="http://gaiaair.org/ontology/amedeo-apu#GeneratorControlUnit">
        <rdfs:subClassOf rdf:resource="http://gaiaair.org/ontology/amedeo-apu#LRU"/>
        <rdfs:label>Generator Control Unit</rdfs:label>
        <rdfs:comment>Controls and regulates the electrical output from the APU generator</rdfs:comment>
    </owl:Class>
    
    <!-- http://gaiaair.org/ontology/amedeo-apu#FuelControlUnit -->
    <owl:Class rdf:about="http://gaiaair.org/ontology/amedeo-apu#FuelControlUnit">
        <rdfs:subClassOf rdf:resource="http://gaiaair.org/ontology/amedeo-apu#LRU"/>
        <rdfs:subClassOf rdf:resource="http://gaiaair.org/ontology/amedeo-apu#SafetyCriticalComponent"/>
        <rdfs:label>Fuel Control Unit</rdfs:label>
        <rdfs:comment>Regulates fuel flow to the APU combustion chamber</rdfs:comment>
    </owl:Class>
    
    <!-- http://gaiaair.org/ontology/amedeo-apu#APUOperationalState -->
    <owl:Class rdf:about="http://gaiaair.org/ontology/amedeo-apu#APUOperationalState">
        <rdfs:subClassOf rdf:resource="http://gaiaair.org/ontology/amedeo#SystemState"/>
        <rdfs:label>APU Operational State</rdfs:label>
        <rdfs:comment>Represents the current operational state of an APU</rdfs:comment>
    </owl:Class>
    
    <!-- http://gaiaair.org/ontology/amedeo-apu#Running -->
    <owl:Class rdf:about="http://gaiaair.org/ontology/amedeo-apu#Running">
        <rdfs:subClassOf rdf:resource="http://gaiaair.org/ontology/amedeo-apu#APUOperationalState"/>
        <rdfs:label>Running</rdfs:label>
        <rdfs:comment>APU is currently operating</rdfs:comment>
    </owl:Class>
    
    <!-- http://gaiaair.org/ontology/amedeo-apu#Shutdown -->
    <owl:Class rdf:about="http://gaiaair.org/ontology/amedeo-apu#Shutdown">
        <rdfs:subClassOf rdf:resource="http://gaiaair.org/ontology/amedeo-apu#APUOperationalState"/>
        <rdfs:label>Shutdown</rdfs:label>
        <rdfs:comment>APU is currently not operating</rdfs:comment>
    </owl:Class>
    
    <!-- http://gaiaair.org/ontology/amedeo-apu#FaultCode -->
    <owl:Class rdf:about="http://gaiaair.org/ontology/amedeo-apu#FaultCode">
        <rdfs:subClassOf rdf:resource="http://gaiaair.org/ontology/amedeo#InformationAsset"/>
        <rdfs:label>Fault Code</rdfs:label>
        <rdfs:comment>A diagnostic code indicating a specific fault condition in the APU</rdfs:comment>
    </owl:Class>
    
    <!-- http://gaiaair.org/ontology/amedeo-apu#MaintenanceProcedure -->
    <owl:Class rdf:about="http://gaiaair.org/ontology/amedeo-apu#MaintenanceProcedure">
        <rdfs:subClassOf rdf:resource="http://gaiaair.org/ontology/amedeo#OperationalTask"/>
        <rdfs:label>Maintenance Procedure</rdfs:label>
        <rdfs:comment>A defined sequence of actions to maintain, repair, or inspect an APU component</rdfs:comment>
    </owl:Class>
    
    <!-- http://gaiaair.org/ontology/amedeo-apu#FuelLineDisconnect -->
    <owl:Class rdf:about="http://gaiaair.org/ontology/amedeo-apu#FuelLineDisconnect">
        <rdfs:subClassOf rdf:resource="http://gaiaair.org/ontology/amedeo-apu#MaintenanceProcedure"/>
        <rdfs:label>Fuel Line Disconnect</rdfs:label>
        <rdfs:comment>Procedure to disconnect the fuel line from the APU</rdfs:comment>
    </owl:Class>
    
    <!-- http://gaiaair.org/ontology/amedeo-apu#CertificationRecord -->
    <owl:Class rdf:about="http://gaiaair.org/ontology/amedeo-apu#CertificationRecord">
        <rdfs:subClassOf rdf:resource="http://gaiaair.org/ontology/amedeo#InformationAsset"/>
        <rdfs:label>Certification Record</rdfs:label>
        <rdfs:comment>Documentation of certification status for a component or procedure</rdfs:comment>
    </owl:Class>
    
    <!-- http://gaiaair.org/ontology/amedeo-apu#CertifiedProcedureForSafetyCriticalComponent -->
    <owl:Class rdf:about="http://gaiaair.org/ontology/amedeo-apu#CertifiedProcedureForSafetyCriticalComponent">
        <owl:equivalentClass>
            <owl:Class>
                <owl:intersectionOf rdf:parseType="Collection">
                    <rdf:Description rdf:about="http://gaiaair.org/ontology/amedeo-apu#MaintenanceProcedure"/>
                    <owl:Restriction>
                        <owl:onProperty rdf:resource="http://gaiaair.org/ontology/amedeo-apu#targetsComponent"/>
                        <owl:someValuesFrom rdf:resource="http://gaiaair.org/ontology/amedeo-apu#SafetyCriticalComponent"/>
                    </owl:Restriction>
                    <owl:Restriction>
                        <owl:onProperty rdf:resource="http://gaiaair.org/ontology/amedeo-apu#hasCertificationRecord"/>
                        <owl:someValuesFrom>
                            <owl:Class>
                                <owl:intersectionOf rdf:parseType="Collection">
                                    <rdf:Description rdf:about="http://gaiaair.org/ontology/amedeo-apu#CertificationRecord"/>
                                    <owl:Restriction>
                                        <owl:onProperty rdf:resource="http://gaiaair.org/ontology/amedeo-apu#status"/>
                                        <owl:hasValue>Approved</owl:hasValue>
                                    </owl:Restriction>
                                </owl:intersectionOf>
                            </owl:Class>
                        </owl:someValuesFrom>
                    </owl:Restriction>
                </owl:intersectionOf>
            </owl:Class>
        </owl:equivalentClass>
        <rdfs:label>Certified Procedure For Safety Critical Component</rdfs:label>
        <rdfs:comment>A maintenance procedure that targets a safety-critical component and has an approved certification record</rdfs:comment>
    </owl:Class>
    
    <!-- http://gaiaair.org/ontology/amedeo-apu#PermissibleAPUStateForProcedure -->
    <owl:Class rdf:about="http://gaiaair.org/ontology/amedeo-apu#PermissibleAPUStateForProcedure">
        <rdfs:label>Permissible APU State For Procedure</rdfs:label>
        <rdfs:comment>Represents valid combinations of APU states and maintenance procedures</rdfs:comment>
    </owl:Class>
    
    <!-- http://gaiaair.org/ontology/amedeo-apu#InvalidProcedureWhileRunning -->
    <owl:Class rdf:about="http://gaiaair.org/ontology/amedeo-apu#InvalidProcedureWhileRunning">
        <owl:equivalentClass>
            <owl:Class>
                <owl:intersectionOf rdf:parseType="Collection">
                    <owl:Restriction>
                        <owl:onProperty rdf:resource="http://gaiaair.org/ontology/amedeo-apu#hasOperationalState"/>
                        <owl:hasValue rdf:resource="http://gaiaair.org/ontology/amedeo-apu#Running"/>
                    </owl:Restriction>
                    <owl:Restriction>
                        <owl:onProperty rdf:resource="http://gaiaair.org/ontology/amedeo-apu#requiresProcedure"/>
                        <owl:hasValue rdf:resource="http://gaiaair.org/ontology/amedeo-apu#FuelLineDisconnect"/>
                    </owl:Restriction>
                </owl:intersectionOf>
            </owl:Class>
        </owl:equivalentClass>
        <owl:disjointWith rdf:resource="http://gaiaair.org/ontology/amedeo-apu#PermissibleAPUStateForProcedure"/>
        <rdfs:label>Invalid Procedure While Running</rdfs:label>
        <rdfs:comment>Represents the invalid state of attempting a fuel line disconnect while the APU is running</rdfs:comment>
    </owl:Class>
    
    <!-- http://gaiaair.org/ontology/amedeo-apu#NonCompliantProcedure -->
    <owl:Class rdf:about="http://gaiaair.org/ontology/amedeo-apu#NonCompliantProcedure">
        <rdfs:subClassOf rdf:resource="http://gaiaair.org/ontology/amedeo-apu#MaintenanceProcedure"/>
        <rdfs:label>Non-Compliant Procedure</rdfs:label>
        <rdfs:comment>A maintenance procedure that violates safety or ethical constraints</rdfs:comment>
    </owl:Class>
    
    <!-- 
    ///////////////////////////////////////////////////////////////////////////////////////
    //
    // Object Properties
    //
    ///////////////////////////////////////////////////////////////////////////////////////
     -->
    
    <!-- http://gaiaair.org/ontology/amedeo-apu#hasOperationalState -->
    <owl:ObjectProperty rdf:about="http://gaiaair.org/ontology/amedeo-apu#hasOperationalState">
        <rdfs:domain rdf:resource="http://gaiaair.org/ontology/amedeo-apu#APU"/>
        <rdfs:range rdf:resource="http://gaiaair.org/ontology/amedeo-apu#APUOperationalState"/>
        <rdfs:label>has operational state</rdfs:label>
        <rdfs:comment>Relates an APU to its current operational state</rdfs:comment>
    </owl:ObjectProperty>
    
    <!-- http://gaiaair.org/ontology/amedeo-apu#targetsComponent -->
    <owl:ObjectProperty rdf:about="http://gaiaair.org/ontology/amedeo-apu#targetsComponent">
        <rdfs:domain rdf:resource="http://gaiaair.org/ontology/amedeo-apu#MaintenanceProcedure"/>
        <rdfs:range rdf:resource="http://gaiaair.org/ontology/amedeo#GAIAComponent"/>
        <rdfs:label>targets component</rdfs:label>
        <rdfs:comment>Relates a maintenance procedure to the component it targets</rdfs:comment>
    </owl:ObjectProperty>
    
    <!-- http://gaiaair.org/ontology/amedeo-apu#hasCertificationRecord -->
    <owl:ObjectProperty rdf:about="http://gaiaair.org/ontology/amedeo-apu#hasCertificationRecord">
        <rdfs:domain>
            <owl:Class>
                <owl:unionOf rdf:parseType="Collection">
                    <rdf:Description rdf:about="http://gaiaair.org/ontology/amedeo-apu#MaintenanceProcedure"/>
                    <rdf:Description rdf:about="http://gaiaair.org/ontology/amedeo#GAIAComponent"/>
                </owl:unionOf>
            </owl:Class>
        </rdfs:domain>
        <rdfs:range rdf:resource="http://gaiaair.org/ontology/amedeo-apu#CertificationRecord"/>
        <rdfs:label>has certification record</rdfs:label>
        <rdfs:comment>Relates a component or procedure to its certification record</rdfs:comment>
    </owl:ObjectProperty>
    
    <!-- http://gaiaair.org/ontology/amedeo-apu#requiresProcedure -->
    <owl:ObjectProperty rdf:about="http://gaiaair.org/ontology/amedeo-apu#requiresProcedure">
        <rdfs:domain rdf:resource="http://gaiaair.org/ontology/amedeo-apu#FaultCode"/>
        <rdfs:range rdf:resource="http://gaiaair.org/ontology/amedeo-apu#MaintenanceProcedure"/>
        <rdfs:label>requires procedure</rdfs:label>
        <rdfs:comment>Relates a fault code to the maintenance procedure required to address it</rdfs:comment>
    </owl:ObjectProperty>
    
    <!-- http://gaiaair.org/ontology/amedeo-apu#hasComponent -->
    <owl:ObjectProperty rdf:about="http://gaiaair.org/ontology/amedeo-apu#hasComponent">
        <rdfs:domain rdf:resource="http://gaiaair.org/ontology/amedeo-apu#APU"/>
        <rdfs:range rdf:resource="http://gaiaair.org/ontology/amedeo#GAIAComponent"/>
        <rdfs:label>has component</rdfs:label>
        <rdfs:comment>Relates an APU to its components</rdfs:comment>
    </owl:ObjectProperty>
    
    <!-- http://gaiaair.org/ontology/amedeo-apu#hasProvenance -->
    <owl:ObjectProperty rdf:about="http://gaiaair.org/ontology/amedeo-apu#hasProvenance">
        <rdfs:domain rdf:resource="http://gaiaair.org/ontology/amedeo#InformationAsset"/>
        <rdfs:range rdf:resource="http://gaiaair.org/ontology/amedeo#DataSource"/>
        <rdfs:label>has provenance</rdfs:label>
        <rdfs:comment>Relates an information asset to its provenance information</rdfs:comment>
    </owl:ObjectProperty>
    
    <!-- http://gaiaair.org/ontology/amedeo-apu#performedBy -->
    <owl:ObjectProperty rdf:about="http://gaiaair.org/ontology/amedeo-apu#performedBy">
        <rdfs:domain rdf:resource="http://gaiaair.org/ontology/amedeo-apu#MaintenanceProcedure"/>
        <rdfs:range rdf:resource="http://gaiaair.org/ontology/amedeo#HumanAgent"/>
        <rdfs:label>performed by</rdfs:label>
        <rdfs:comment>Relates a maintenance procedure to the human agent performing it</rdfs:comment>
    </owl:ObjectProperty>
    
    <!-- http://gaiaair.org/ontology/amedeo-apu#hasSkillLevel -->
    <owl:ObjectProperty rdf:about="http://gaiaair.org/ontology/amedeo-apu#hasSkillLevel">
        <rdfs:domain rdf:resource="http://gaiaair.org/ontology/amedeo#HumanAgent"/>
        <rdfs:range rdf:resource="http://gaiaair.org/ontology/amedeo#Skill"/>
        <rdfs:label>has skill level</rdfs:label>
        <rdfs:comment>Relates a human agent to their skill level</rdfs:comment>
    </owl:ObjectProperty>
    
    <!-- http://gaiaair.org/ontology/amedeo-apu#requiresSkillLevel -->
    <owl:ObjectProperty rdf:about="http://gaiaair.org/ontology/amedeo-apu#requiresSkillLevel">
        <rdfs:domain rdf:resource="http://gaiaair.org/ontology/amedeo-apu#MaintenanceProcedure"/>
        <rdfs:range rdf:resource="http://gaiaair.org/ontology/amedeo#Skill"/>
        <rdfs:label>requires skill level</rdfs:label>
        <rdfs:comment>Relates a maintenance procedure to the skill level required to perform it</rdfs:comment>
    </owl:ObjectProperty>
    
    <!-- 
    ///////////////////////////////////////////////////////////////////////////////////////
    //
    // Data Properties
    //
    ///////////////////////////////////////////////////////////////////////////////////////
     -->
    
    <!-- http://gaiaair.org/ontology/amedeo-apu#hasPartNumber -->
    <owl:DatatypeProperty rdf:about="http://gaiaair.org/ontology/amedeo-apu#hasPartNumber">
        <rdfs:domain rdf:resource="http://gaiaair.org/ontology/amedeo#GAIAComponent"/>
        <rdfs:range rdf:resource="http://www.w3.org/2001/XMLSchema#string"/>
        <rdfs:label>has part number</rdfs:label>
        <rdfs:comment>The manufacturer's part number for a component</rdfs:comment>
    </owl:DatatypeProperty>
    
    <!-- http://gaiaair.org/ontology/amedeo-apu#generatesPower -->
    <owl:DatatypeProperty rdf:about="http://gaiaair.org/ontology/amedeo-apu#generatesPower">
        <rdfs:domain rdf:resource="http://gaiaair.org/ontology/amedeo-apu#GeneratorControlUnit"/>
        <rdfs:range rdf:resource="http://www.w3.org/2001/XMLSchema#boolean"/>
        <rdfs:label>generates power</rdfs:label>
        <rdfs:comment>Indicates whether the generator control unit is currently generating power</rdfs:comment>
    </owl:DatatypeProperty>
    
    <!-- http://gaiaair.org/ontology/amedeo-apu#controlsAirflow -->
    <owl:DatatypeProperty rdf:about="http://gaiaair.org/ontology/amedeo-apu#controlsAirflow">
        <rdfs:domain rdf:resource="http://gaiaair.org/ontology/amedeo-apu#BleedAirControlValve"/>
        <rdfs:range rdf:resource="http://www.w3.org/2001/XMLSchema#boolean"/>
        <rdfs:label>controls airflow</rdfs:label>
        <rdfs:comment>Indicates whether the bleed air control valve is currently controlling airflow</rdfs:comment>
    </owl:DatatypeProperty>
    
    <!-- http://gaiaair.org/ontology/amedeo-apu#status -->
    <owl:DatatypeProperty rdf:about="http://gaiaair.org/ontology/amedeo-apu#status">
        <rdfs:domain rdf:resource="http://gaiaair.org/ontology/amedeo-apu#CertificationRecord"/>
        <rdfs:range rdf:resource="http://www.w3.org/2001/XMLSchema#string"/>
        <rdfs:label>status</rdfs:label>
        <rdfs:comment>The status of a certification record (e.g., "Approved", "Pending", "Rejected")</rdfs:comment>
    </owl:DatatypeProperty>
    
    <!-- http://gaiaair.org/ontology/amedeo-apu#tlsUtidsIdentifier -->
    <owl:DatatypeProperty rdf:about="http://gaiaair.org/ontology/amedeo-apu#tlsUtidsIdentifier">
        <rdfs:domain>
            <owl:Class>
                <owl:unionOf rdf:parseType="Collection">
                    <rdf:Description rdf:about="http://gaiaair.org/ontology/amedeo#GAIAComponent"/>
                    <rdf:Description rdf:about="http://gaiaair.org/ontology/amedeo-apu#MaintenanceProcedure"/>
                    <rdf:Description rdf:about="http://gaiaair.org/ontology/amedeo-apu#FaultCode"/>
                </owl:unionOf>
            </owl:Class>
        </rdfs:domain>
        <rdfs:range rdf:resource="http://www.w3.org/2001/XMLSchema#string"/>
        <rdfs:label>TLS-UTidS identifier</rdfs:label>
        <rdfs:comment>The TLS-UTidS identifier for a component, procedure, or fault code</rdfs:comment>
    </owl:DatatypeProperty>
    
    <!-- http://gaiaair.org/ontology/amedeo-apu#complianceStatus -->
    <owl:DatatypeProperty rdf:about="http://gaiaair.org/ontology/amedeo-apu#complianceStatus">
        <rdfs:domain rdf:resource="http://gaiaair.org/ontology/amedeo-apu#MaintenanceProcedure"/>
        <rdfs:range rdf:resource="http://www.w3.org/2001/XMLSchema#string"/>
        <rdfs:label>compliance status</rdfs:label>
        <rdfs:comment>The compliance status of a maintenance procedure (e.g., "PASS", "FAIL")</rdfs:comment>
    </owl:DatatypeProperty>
    
    <!-- http://gaiaair.org/ontology/amedeo-apu#reasoningExplanation -->
    <owl:DatatypeProperty rdf:about="http://gaiaair.org/ontology/amedeo-apu#reasoningExplanation">
        <rdfs:domain rdf:resource="http://gaiaair.org/ontology/amedeo-apu#MaintenanceProcedure"/>
        <rdfs:range rdf:resource="http://www.w3.org/2001/XMLSchema#string"/>
        <rdfs:label>reasoning explanation</rdfs:label>
        <rdfs:comment>Human-readable explanation of the reasoning behind a compliance decision</rdfs:comment>
    </owl:DatatypeProperty>
    
    <!-- http://gaiaair.org/ontology/amedeo-apu#suggestedFix -->
    <owl:DatatypeProperty rdf:about="http://gaiaair.org/ontology/amedeo-apu#suggestedFix">
        <rdfs:domain rdf:resource="http://gaiaair.org/ontology/amedeo-apu#MaintenanceProcedure"/>
        <rdfs:range rdf:resource="http://www.w3.org/2001/XMLSchema#string"/>
        <rdfs:label>suggested fix</rdfs:label>
        <rdfs:comment>Suggested action to fix a non-compliant procedure</rdfs:comment>
    </owl:DatatypeProperty>
    
    <!-- 
    ///////////////////////////////////////////////////////////////////////////////////////
    //
    // SWRL Rules
    //
    ///////////////////////////////////////////////////////////////////////////////////////
     -->
    
    <rdf:Description>
        <rdf:type rdf:resource="http://www.w3.org/2003/11/swrl#Imp"/>
        <swrl:body>
            <rdf:Description>
                <rdf:type rdf:resource="http://www.w3.org/2003/11/swrl#AtomList"/>
                <rdf:first>
                    <rdf:Description>
                        <rdf:type rdf:resource="http://www.w3.org/2003/11/swrl#ClassAtom"/>
                        <swrl:classPredicate rdf:resource="http://gaiaair.org/ontology/amedeo-apu#APU"/>
                        <swrl:argument1 rdf:resource="urn:swrl:var#a"/>
                    </rdf:Description>
                </rdf:first>
                <rdf:rest>
                    <rdf:Description>
                        <rdf:type rdf:resource="http://www.w3.org/2003/11/swrl#AtomList"/>
                        <rdf:first>
                            <rdf:Description>
                                <rdf:type rdf:resource="http://www.w3.org/2003/11/swrl#IndividualPropertyAtom"/>
                                <swrl:propertyPredicate rdf:resource="http://gaiaair.org/ontology/amedeo-apu#hasOperationalState"/>
                                <swrl:argument1 rdf:resource="urn:swrl:var#a"/>
                                <swrl:argument2 rdf:resource="http://gaiaair.org/ontology/amedeo-apu#Running"/>
                            </rdf:Description>
                        </rdf:first>
                        <rdf:rest>
                            <rdf:Description>
                                <rdf:type rdf:resource="http://www.w3.org/2003/11/swrl#AtomList"/>
                                <rdf:first>
                                    <rdf:Description>
                                        <rdf:type rdf:resource="http://www.w3.org/2003/11/swrl#ClassAtom"/>
                                        <swrl:classPredicate rdf:resource="http://gaiaair.org/ontology/amedeo-apu#MaintenanceProcedure"/>
                                        <swrl:argument1 rdf:resource="urn:swrl:var#p"/>
                                    </rdf:Description>
                                </rdf:first>
                                <rdf:rest>
                                    <rdf:Description>
                                        <rdf:type rdf:resource="http://www.w3.org/2003/11/swrl#AtomList"/>
                                        <rdf:first>
                                            <rdf:Description>
                                                <rdf:type rdf:resource="http://www.w3.org/2003/11/swrl#ClassAtom"/>
                                                <swrl:classPredicate rdf:resource="http://gaiaair.org/ontology/amedeo-apu#FuelLineDisconnect"/>
                                                <swrl:argument1 rdf:resource="urn:swrl:var#p"/>
                                            </rdf:Description>
                                        </rdf:first>
                                        <rdf:rest rdf:resource="http://www.w3.org/1999/02/22-rdf-syntax-ns#nil"/>
                                    </rdf:Description>
                                </rdf:rest>
                            </rdf:Description>
                        </rdf:rest>
                    </rdf:Description>
                </rdf:rest>
            </rdf:Description>
        </swrl:body>
        <swrl:head>
            <rdf:Description>
                <rdf:type rdf:resource="http://www.w3.org/2003/11/swrl#AtomList"/>
                <rdf:first>
                    <rdf:Description>
                        <rdf:type rdf:resource="http://www.w3.org/2003/11/swrl#ClassAtom"/>
                        <swrl:classPredicate rdf:resource="http://gaiaair.org/ontology/amedeo-apu#NonCompliantProcedure"/>
                        <swrl:argument1 rdf:resource="urn:swrl:var#p"/>
                    </rdf:Description>
                </rdf:first>
                <rdf:rest rdf:resource="http://www.w3.org/1999/02/22-rdf-syntax-ns#nil"/>
            </rdf:Description>
        </swrl:head>
    </rdf:Description>
    
    <!-- 
    ///////////////////////////////////////////////////////////////////////////////////////
    //
    // Individuals
    //
    ///////////////////////////////////////////////////////////////////////////////////////
     -->
    
    <!-- http://gaiaair.org/ontology/amedeo-apu#APU_001 -->
    <owl:NamedIndividual rdf:about="http://gaiaair.org/ontology/amedeo-apu#APU_001">
        <rdf:type rdf:resource="http://gaiaair.org/ontology/amedeo-apu#APU"/>
        <apu:hasOperationalState rdf:resource="http://gaiaair.org/ontology/amedeo-apu#Running"/>
        <apu:hasComponent rdf:resource="http://gaiaair.org/ontology/amedeo-apu#FuelControlUnit_4823AB12"/>
        <apu:hasPartNumber>GTCP331-350</apu:hasPartNumber>
        <apu:tlsUtidsIdentifier>[CMP:APU_001#live]</apu:tlsUtidsIdentifier>
    </owl:NamedIndividual>
    
    <!-- http://gaiaair.org/ontology/amedeo-apu#FuelControlUnit_4823AB12 -->
    <owl:NamedIndividual rdf:about="http://gaiaair.org/ontology/amedeo-apu#FuelControlUnit_4823AB12">
        <rdf:type rdf:resource="http://gaiaair.org/ontology/amedeo-apu#FuelControlUnit"/>
        <apu:hasCertificationRecord rdf:resource="http://gaiaair.org/ontology/amedeo-apu#Cert_00123"/>
        <apu:hasPartNumber>4823-AB12</apu:hasPartNumber>
        <apu:tlsUtidsIdentifier>[CMP:FCU_4823AB12#live]</apu:tlsUtidsIdentifier>
    </owl:NamedIndividual>
    
    <!-- http://gaiaair.org/ontology/amedeo-apu#Cert_00123 -->
    <owl:NamedIndividual rdf:about="http://gaiaair.org/ontology/amedeo-apu#Cert_00123">
        <rdf:type rdf:resource="http://gaiaair.org/ontology/amedeo-apu#CertificationRecord"/>
        <apu:hasProvenance rdf:resource="http://gaiaair.org/ontology/amedeo-apu#BITT_Hash_ABC123"/>
        <apu:status>Approved</apu:status>
        <apu:tlsUtidsIdentifier>[DOC:CERT_00123#auth]</apu:tlsUtidsIdentifier>
    </owl:NamedIndividual>
    
    <!-- http://gaiaair.org/ontology/amedeo-apu#BITT_Hash_ABC123 -->
    <owl:NamedIndividual rdf:about="http://gaiaair.org/ontology/amedeo-apu#BITT_Hash_ABC123">
        <rdf:type rdf:resource="http://gaiaair.org/ontology/amedeo#DataSource"/>
    </owl:NamedIndividual>
    
    <!-- http://gaiaair.org/ontology/amedeo-apu#FuelLineDisconnect_Procedure -->
    <owl:NamedIndividual rdf:about="http://gaiaair.org/ontology/amedeo-apu#FuelLineDisconnect_Procedure">
        <rdf:type rdf:resource="http://gaiaair.org/ontology/amedeo-apu#FuelLineDisconnect"/>
        <apu:targetsComponent rdf:resource="http://gaiaair.org/ontology/amedeo-apu#FuelControlUnit_4823AB12"/>
        <apu:hasCertificationRecord rdf:resource="http://gaiaair.org/ontology/amedeo-apu#Cert_00123"/>
        <apu:requiresSkillLevel rdf:resource="http://gaiaair.org/ontology/amedeo-apu#APU_Maintenance_L2"/>
        <apu:tlsUtidsIdentifier>[OP:FLD_PROC_001#maint]</apu:tlsUtidsIdentifier>
    </owl:NamedIndividual>
    
    <!-- http://gaiaair.org/ontology/amedeo-apu#APU_Maintenance_L2 -->
    <owl:NamedIndividual rdf:about="http://gaiaair.org/ontology/amedeo-apu#APU_Maintenance_L2">
        <rdf:type rdf:resource="http://gaiaair.org/ontology/amedeo#Skill"/>
    </owl:NamedIndividual>
    
    <!-- http://gaiaair.org/ontology/amedeo-apu#Technician_John -->
    <owl:NamedIndividual rdf:about="http://gaiaair.org/ontology/amedeo-apu#Technician_John">
        <rdf:type rdf:resource="http://gaiaair.org/ontology/amedeo#HumanAgent"/>
        <apu:hasSkillLevel rdf:resource="http://gaiaair.org/ontology/amedeo-apu#APU_Maintenance_L2"/>
        <apu:tlsUtidsIdentifier>[AGT:TECH_JOHN#resp]</apu:tlsUtidsIdentifier>
    </owl:NamedIndividual>
    
    <!-- http://gaiaair.org/ontology/amedeo-apu#FaultCode_FC001 -->
    <owl:NamedIndividual rdf:about="http://gaiaair.org/ontology/amedeo-apu#FaultCode_FC001">
        <rdf:type rdf:resource="http://gaiaair.org/ontology/amedeo-apu#FaultCode"/>
        <apu:requiresProcedure rdf:resource="http://gaiaair.org/ontology/amedeo-apu#FuelLineDisconnect_Procedure"/>
        <apu:tlsUtidsIdentifier>[ERR:FC001#diag]</apu:tlsUtidsIdentifier>
    </owl:NamedIndividual>
</rdf:RDF>
