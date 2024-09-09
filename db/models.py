from sqlalchemy import Column, String, Date, Integer, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

# class Patient(Base):
#     __tablename__ = 'patient'
#
#     id = Column(String, primary_key=True)
#
#
#     identifiers = relationship('PatientIdentifier', back_populates='patient')
#     encounters =relationship('Encounter', back_populates='patient')
#
# class Identifier(Base):
#     __tablename__ = 'identifier'
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#
#
# class PatientIdentifier(Base):
#     __tablename__ = 'patientidentifier'
#     id = Column(Integer, primary_key=True)
#     patient_id = Column(String, ForeignKey('patient.id'))
#
#     patient = relationship('Patient', back_populates='patientidentifier')

class Encounter(Base):
    __tablename__ = 'encounters'

    id = Column(String, primary_key=True)
    meta = Column(String)
    identifier = Column(String)
    status = Column(String)
    _class = Column(String)
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

db_url = 'postgresql+pg8000://admin:emistest!@postgres:5432/emis'
engine = create_engine(db_url)
Base.metadata.create_all(engine)