from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from lib.database import Base

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=True)

    cars = relationship("Car", back_populates="owner", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Customer(id={self.id}, name={self.name}, phone={self.phone}, email={self.email})>"

class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True)
    model = Column(String, nullable=False)
    year = Column(String, nullable=False)
    owner_id = Column(Integer, ForeignKey("customers.id"))

    owner = relationship("Customer", back_populates="cars")
    services = relationship("Service", back_populates="car", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Car(id={self.id}, model={self.model}, year={self.year}, owner_id={self.owner_id})>"

class Service(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True)
    service_type = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    status = Column(String, default="upcoming")
    car_id = Column(Integer, ForeignKey("cars.id"))

    car = relationship("Car", back_populates="services")

    def __repr__(self):
        return f"<Service(id={self.id}, type={self.service_type}, date={self.date}, status={self.status}, car_id={self.car_id})>"
