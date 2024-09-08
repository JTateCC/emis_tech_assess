import pytest
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Base, Patient, Identifier
@pytest.fixture
def create_in_memory_db():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()

def test_patient_created(create_in_memory_db):
    session = create_in_memory_db
    new_patient = Patient(id='13944033030',
                          us_birth_gender='M',
                          birth_date=datetime.date(1980,1,1),
                          family_name='Doe',
                          given_name='John',
                          prefix='Mr',
                          contact='07929292920',
                          )
    session.add(new_patient)
    session.commit()

    patient = session.query(Patient).filter_by(id='13944033030').first()

    assert patient is not None
    assert patient.id == '13944033030'
    assert patient.family_name == 'Doe'
    assert patient.us_birth_gender == 'M'
    assert str(patient.birth_date) == '1980-01-01'

def test_identifier_created(create_in_memory_db):
    session = create_in_memory_db
    ssn_identifier = Identifier(name='SSN')

    # Step 2: Add and commit the identifier to the session
    session.add(ssn_identifier)
    session.commit()

    identifier = session.query(Identifier).filter_by(name='SSN').first()

    assert identifier is not None
    assert identifier.name == 'SSN'

def test_duplicate_handled(create_in_memory_db):
    session = create_in_memory_db
    ssn_identifier = Identifier(name='SSN')

    # Step 2: Add and commit the identifier to the session
    session.add(ssn_identifier)
    session.commit()

    ssn_identifier_duplicate = Identifier(name='SSN')
    session.add(ssn_identifier_duplicate)
    session.commit()





