First inspection of Json files, revealed that resourceType would be the likely mapper for Database Tables
Ran script to get list of all resource types

Resource Type: Patient
Resource Type: Encounter
Resource Type: Condition
Resource Type: DiagnosticReport
Resource Type: DocumentReference
Resource Type: Claim
Resource Type: ExplanationOfBenefit
Resource Type: Observation
Resource Type: Procedure
Resource Type: Immunization
Resource Type: MedicationRequest
Resource Type: CareTeam
Resource Type: CarePlan
Resource Type: ImagingStudy
Resource Type: Medication
Resource Type: MedicationAdministration
Resource Type: Provenance
Resource Type: AllergyIntolerance
Resource Type: Device
Resource Type: SupplyDelivery

INspecting the key values of each entry to get ideas for column names
Resource Type: Procedure
id
meta
status
code
subject
encounter
performedPeriod
location

also led to the identificaton of foreign key relationships (e.g. encounter as the FK)


first step to extract json files into pandas dataframe for ease of use. 

debated automatically creating tables from dataframes or use of an ORM