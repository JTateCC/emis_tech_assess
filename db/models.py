from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Patient(Base):
    __tablename__ = 'patient'

    id = Column(String, primary_key=True)
    meta = Column(String)
    text = Column(String)
    extension = Column(String)
    identifier = Column(String)
    name = Column(String)
    telecom = Column(String)
    gender = Column(String)
    birthDate = Column(String)
    deceasedDateTime = Column(String)
    address = Column(String)
    maritalStatus = Column(String)
    multipleBirthBoolean = Column(String)
    communication = Column(String)


    # encounters =relationship('Encounter', back_populates='patient')

class Encounter(Base):
    __tablename__ = 'encounter'

    id = Column(String, primary_key=True)
    meta = Column(String)
    identifier = Column(String)
    status = Column(String)
    _class = Column('class', String, key='_class')
    type = Column(String)
    subject = Column(String)
    participant = Column(String)
    period = Column(String)
    location = Column(String)
    serviceProvider = Column(String)
    reasonCode = Column(String)
    hospitalization = Column(String)

    # patient_id = Column(String, ForeignKey('patient.id'))
    # patient = relationship('Patient', back_populates='encounters')

class Condition(Base):
    __tablename__ = 'condition'  # Set the table name to the class name

    id = Column(String, primary_key=True)
    meta = Column(String)
    clinicalStatus = Column(String)
    verificationStatus = Column(String)
    category = Column(String)
    code = Column(String)
    subject = Column(String)
    encounter = Column(String)
    onsetDateTime = Column(String)
    recordedDate = Column(String)

class DiagnosticReport(Base):
    __tablename__ = 'diagnosticReport'

    id = Column(String, primary_key=True)
    meta = Column(String)
    status = Column(String)
    category = Column(String)
    code = Column(String)
    subject = Column(String)
    encounter = Column(String)
    effectiveDateTime = Column(String)
    issued = Column(String)
    performer = Column(String)
    presentedForm = Column(String)

class DocumentReference(Base):
    __tablename__ = 'documentReference'

    id = Column(String, primary_key=True)
    meta = Column(String)
    identifier = Column(String)
    status = Column(String)
    type = Column(String)
    category = Column(String)
    subject = Column(String)
    date = Column(String)
    author = Column(String)
    custodian = Column(String)
    content = Column(String)
    context = Column(String)

class Claim(Base):
    __tablename__ = 'claim'

    id = Column(String, primary_key=True)
    status = Column(String)
    type = Column(String)
    use = Column(String)
    patient = Column(String)
    billablePeriod = Column(String)
    created = Column(String)
    provider = Column(String)
    priority = Column(String)
    facility = Column(String)
    diagnosis = Column(String)
    insurance = Column(String)
    item = Column(String)
    total = Column(String)


class ExplanationOfBenefit(Base):
    __tablename__ = 'explanationOfBenefit'

    id = Column(String, primary_key=True)
    contained = Column(String)
    identifier = Column(String)
    status = Column(String)
    type = Column(String)
    use = Column(String)
    patient = Column(String)
    billablePeriod = Column(String)
    created = Column(String)
    insurer = Column(String)
    provider = Column(String)
    referral = Column(String)
    facility = Column(String)
    claim = Column(String)
    outcome = Column(String)
    careTeam = Column(String)
    diagnosis = Column(String)
    insurance = Column(String)
    item = Column(String)
    total = Column(String)
    payment = Column(String)

class Observation(Base):
    __tablename__ = 'observation'

    id = Column(String, primary_key=True)
    meta = Column(String)
    status = Column(String)
    category = Column(String)
    code = Column(String)
    subject = Column(String)
    encounter = Column(String)
    effectiveDateTime = Column(String)
    issued = Column(String)
    valueQuantity = Column(String)

class Procedure(Base):
    __tablename__ = 'procedure'

    id = Column(String, primary_key=True)
    meta = Column(String)
    status = Column(String)
    code = Column(String)
    subject = Column(String)
    encounter = Column(String)
    performedPeriod = Column(String)
    location = Column(String)

class Immunization(Base):
    __tablename__ = 'immunization'

    id = Column(String, primary_key=True)
    meta = Column(String)
    status = Column(String)
    vaccineCode = Column(String)
    patient = Column(String)
    encounter = Column(String)
    occurrenceDateTime = Column(String)
    primarySource = Column(String)
    location = Column(String)

class MedicationRequest(Base):
    __tablename__ = 'medicationRequest'

    id = Column(String, primary_key=True)
    meta = Column(String)
    status = Column(String)
    intent = Column(String)
    medicationCodeableConcept = Column(String)
    subject = Column(String)
    encounter = Column(String)
    authoredOn = Column(String)
    requester = Column(String)
    reasonReference = Column(String)
    dosageInstruction = Column(String)

class CareTeam(Base):
    __tablename__ = 'careTeam'

    id = Column(String, primary_key=True)
    meta = Column(String)
    status = Column(String)
    subject = Column(String)
    encounter = Column(String)
    period = Column(String)
    participant = Column(String)
    reasonCode = Column(String)
    managingOrganization = Column(String)

class CarePlan(Base):
    __tablename__ = 'carePlan'

    id = Column(String, primary_key=True)
    meta = Column(String)
    text = Column(String)
    status = Column(String)
    intent = Column(String)
    category = Column(String)
    subject = Column(String)
    encounter = Column(String)
    period = Column(String)
    careTeam = Column(String)
    addresses = Column(String)
    activity = Column(String)

class ImagingStudy(Base):
    __tablename__ = 'imagingStudy'

    id = Column(String, primary_key=True)
    identifier = Column(String)
    status = Column(String)
    subject = Column(String)
    encounter = Column(String)
    started = Column(String)
    numberOfSeries = Column(String)
    numberOfInstances = Column(String)
    procedureCode = Column(String)
    location = Column(String)
    series = Column(String)

class Medication(Base):
    __tablename__ = 'medication'

    id = Column(String, primary_key=True)
    meta = Column(String)
    code = Column(String)
    status = Column(String)

class MedicationAdministration(Base):
    __tablename__ = 'medicationAdministration'

    id = Column(String, primary_key=True)
    status = Column(String)
    medicationCodeableConcept = Column(String)
    subject = Column(String)
    context = Column(String)
    effectiveDateTime = Column(String)
    reasonReference = Column(String)

class Provenance(Base):
    __tablename__ = 'provenance'

    id = Column(String, primary_key=True)
    meta = Column(String)
    target = Column(String)
    recorded = Column(String)
    agent = Column(String)

class AllergyIntolerance(Base):
    __tablename__ = 'allergyIntolerance'

    id = Column(String, primary_key=True)
    meta = Column(String)
    clinicalStatus = Column(String)
    verificationStatus = Column(String)
    type = Column(String)
    category = Column(String)
    criticality = Column(String)
    code = Column(String)
    patient = Column(String)
    recordedDate = Column(String)

class Device(Base):
    __tablename__ = 'device'

    id = Column(String, primary_key=True)
    meta = Column(String)
    udiCarrier = Column(String)
    status = Column(String)
    distinctIdentifier = Column(String)
    manufactureDate = Column(String)
    expirationDate = Column(String)
    lotNumber = Column(String)
    serialNumber = Column(String)
    deviceName = Column(String)
    type = Column(String)
    patient = Column(String)

class SupplyDelivery(Base):
    __tablename__ = 'supplyDelivery'

    id = Column(String, primary_key=True)
    status = Column(String)
    patient = Column(String)
    type = Column(String)
    suppliedItem = Column(String)
    occurrenceDateTime = Column(String)
