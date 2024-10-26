

def get_construction_industry_specifics():
    return """Introduction to the Construction Industry: The construction industry encompasses a wide range of activities related to building infrastructure, residential and commercial properties, and public works. It involves complex contractual relationships between various parties, such as clients and vendors. A crucial aspect of these contracts is the specification of insurance requirements that vendors must meet to protect against potential risks and liabilities associated with construction projects.
Key Terms:-
    Client: The entity that owns the project and contracts vendors to perform specific tasks. For example, a property developer hiring a construction company to build an office complex.
    Vendor: The entity that performs work or provides services for the client. Vendors can be construction companies, subcontractors, or other service providers who must meet specific insurance requirements set by the client.
    Certificate of Insurance (COI): A document issued by an insurance company or broker that provides evidence of the insurance coverage held by a vendor. It includes details such as the types of insurance, coverage limits, and policy effective dates. Clients use COIs to verify that vendors meet the required insurance specifications before allowing them to work on-site.
    Conditional Coverage: This term indicates whether special conditions or additional requirements are applied to the coverage. For example, a clause may require that certain insurance coverages only apply under specific circumstances, such as if the vendor is working above a certain height or handling hazardous materials.
    Additional Insured: A person or entity added to a vendor’s insurance policy at the client’s request, providing them with coverage under the vendor's insurance. This protects the client from claims arising from the vendor's work.
    Insurance Requirements in the Construction Industry: Insurance requirements are outlined in contracts to ensure that vendors have adequate coverage to mitigate risks associated with their work. These clauses typically specify the types of insurance required, such as General Liability, Workers' Compensation, Automobile Liability, and Professional Liability, along with minimum coverage limits and additional conditions."""

def get_insurance_mapping_fields():
    return """1. General Liability Insurance
    Coverage Required (GeneralLiability_Required): Indicates if General Liability coverage is mandatory.
    Each Occurrence Limit (GeneralLiability_EachOccurrence): The amount covered per incident.
    Aggregate Limit (GeneralLiability_Aggregate): The total amount covered during the policy period.
    Conditional Coverage (GeneralLiability_Conditional): Specifies if special conditions are applied to this coverage.
2. Automobile Liability Insurance
    Coverage Required (AutomobileLiability_Required): Indicates if Automobile Liability coverage is mandatory.
    Each Occurrence Limit (AutomobileLiability_EachOccurrence): The amount covered per incident for vehicle-related accidents.
    Aggregate Limit (AutomobileLiability_Aggregate): The total amount covered for all vehicle-related incidents during the policy period.
    Conditional Coverage (AutomobileLiability_Conditional): Specifies if special conditions are applied to this coverage.
3. Workers' Compensation Insurance
    Coverage Required (WorkersCompensation_Required): Indicates if Workers' Compensation coverage is mandatory.
    Each Occurrence Limit (WorkersCompensation_EachOccurrence): The amount covered per worker's injury incident.
    Aggregate Limit (WorkersCompensation_Aggregate): The total amount covered for all worker's injury incidents during the policy period.
    Conditional Coverage (WorkersCompensation_Conditional): Specifies if special conditions are applied to this coverage.
4. Professional Liability Insurance
    Coverage Required (ProfessionalLiability_Required): Indicates if Professional Liability coverage is mandatory.
    Each Occurrence Limit (ProfessionalLiability_EachOccurrence): The amount covered per claim related to professional services.
    Aggregate Limit (ProfessionalLiability_Aggregate): The total amount covered for all claims during the policy period.
    Conditional Coverage (ProfessionalLiability_Conditional): Specifies if special conditions are applied to this coverage.
5. Additional Insured
    Entity Name (AdditionalInsured_Name): The name of the entity added as an additional insured.
    Type of Coverage (AdditionalInsured_TypeOfCoverage): Specifies the type of coverage the additional insured is associated with, such as General Liability or Automobile Liability."""

def get_contruction_insurance_examples():
    return """{
    "insurance_requirements": {
        "general_liability": {
            "coverage_required": true or false,
            "each_occurrence_limit":<integer> or null,
            "aggregate_limit": <integer> or null,
            "conditional_coverage": true or false
        },
        "automobile_liability": {
            "coverage_required": true or false,
            "each_occurrence_limit": <integer> or null,
            "aggregate_limit": <integer> or null,
            "conditional_coverage": true or false
        },
        "workers_compensation": {
            "coverage_required": true or false,
            "each_occurrence_limit": <integer> or null,
            "aggregate_limit": <integer> or null,
            "conditional_coverage": true or false
        },
        "professional_liability": {
            "coverage_required": true or false,
            "each_occurrence_limit": <integer> or null,
            "aggregate_limit": <integer> or null,
            "conditional_coverage": true or false
        }
    },
    "additional_insured": [{
        "entity_name": <string> or null,
        "type_of_coverage": <string> or null
    }]
    }"""

def get_contruction_insurance_agent():
    return """You are a text processing agent working with Insurance agreement document."""