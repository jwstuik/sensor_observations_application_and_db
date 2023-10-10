from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Experiment(Base):
    __tablename__ = 'experiments'

    id = Column(Integer, primary_key=True)
    researcher = Column(String)
    upper_threshold = Column(Float)
    lower_threshold = Column(Float)

    sensors = relationship("Sensor", back_populates="experiment")
    measurements = relationship("Measurement", back_populates="experiment")

class Sensor(Base):
    __tablename__ = 'sensors'

    id = Column(Integer, primary_key=True)
    experiment_id = Column(Integer, ForeignKey('experiments.id'))
    sensor_id = Column(String)

    experiment = relationship("Experiment", back_populates="sensors")

class Measurement(Base):
    __tablename__ = 'measurements'

    id = Column(Integer, primary_key=True)
    experiment_id = Column(Integer, ForeignKey('experiments.id'))
    timestamp = Column(Float)
    temperature = Column(Float)

    experiment = relationship("Experiment", back_populates="measurements")

engine = create_engine('postgresql://postgres:password@localhost/experiment_db')

Base.metadata.create_all(engine)
