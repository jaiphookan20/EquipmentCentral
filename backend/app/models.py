from datetime import datetime
from enum import Enum
from typing import List
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum as SQLEnum, Boolean, Float, Text
from sqlalchemy.orm import relationship
from app import db

# Use SQLAlchemy's declarative base
Base = db.Model

class ProjectType(str, Enum):
    MINING = "mining"
    RENEWABLE = "renewable"
    COMMERCIAL = "commercial"
    INDUSTRIAL = "industrial"
    RESIDENTIAL = "residential"

class VoltageLevel(str, Enum):
    LOW = "low_voltage"  # Up to 1000V
    MEDIUM = "medium_voltage"  # 1kV to 33kV
    HIGH = "high_voltage"  # Above 33kV

class ProjectRole(str, Enum):
    LEAD = "lead_electrician"
    SUPERVISOR = "supervisor"
    TECHNICIAN = "technician"
    APPRENTICE = "apprentice"

class SpecialtyArea(str, Enum):
    INDUSTRIAL_AUTOMATION = "industrial_automation"
    POWER_DISTRIBUTION = "power_distribution"
    RENEWABLE_ENERGY = "renewable_energy"
    MINING_OPERATIONS = "mining_operations"
    COMMERCIAL_INSTALLATION = "commercial_installation"
    MAINTENANCE = "maintenance"

class LicenseType(str, Enum):
    ELECTRICAL_CONTRACTOR = "electrical_contractor"  # Business license
    QUALIFIED_SUPERVISOR = "qualified_supervisor"    # Supervisory license
    ELECTRICAL_WORKER = "electrical_worker"         # Individual license (A-Grade)

class QualificationType(str, Enum):
    CERT_III_ELECTROTECHNOLOGY = "cert_iii_electrotechnology"  # UEE30811
    CERT_IV_INDUSTRIAL_ELECTRONICS = "cert_iv_industrial_electronics"
    DIPLOMA_ELECTRICAL = "diploma_electrical"
    ADVANCED_DIPLOMA_ELECTRICAL = "advanced_diploma_electrical"

class CertificationType(str, Enum):
    # High-Risk Work
    WORKING_AT_HEIGHTS = "working_at_heights"
    CONFINED_SPACE = "confined_space"
    EWP = "elevated_work_platform"
    WHITE_CARD = "construction_induction"
    
    # Technical Specializations
    HV_SWITCHING = "high_voltage_switching"
    HAZARDOUS_AREA = "hazardous_area"
    TEST_AND_TAG = "test_and_tag"
    SOLAR_GRID_CONNECT = "solar_grid_connect"
    BATTERY_STORAGE = "battery_storage"
    UNDERGROUND_CABLES = "underground_cables"
    
    # Mining Specific
    MINE_SITE_INDUCTION = "mine_site_induction"
    SURFACE_MINING = "surface_mining"
    UNDERGROUND_MINING = "underground_mining"
    GAS_TESTING = "gas_testing"
    EXPLOSION_PROTECTION = "explosion_protection"
    
    # Safety & Compliance
    FIRST_AID = "first_aid"
    CPR = "cpr"
    ASBESTOS_AWARENESS = "asbestos_awareness"
    LOTO = "lockout_tagout"

class AustralianState(str, Enum):
    NSW = "new_south_wales"
    VIC = "victoria"
    QLD = "queensland"
    WA = "western_australia"
    SA = "south_australia"
    TAS = "tasmania"
    NT = "northern_territory"
    ACT = "australian_capital_territory"

class License(Base):
    __tablename__ = "licenses"
    
    id = Column(Integer, primary_key=True)
    electrician_id = Column(Integer, ForeignKey("electricians.id"))
    license_type = Column(SQLEnum(LicenseType))
    license_number = Column(String, unique=True, nullable=False)
    issuing_state = Column(SQLEnum(AustralianState))
    issue_date = Column(DateTime, nullable=False)
    expiry_date = Column(DateTime, nullable=False)
    status = Column(String)  # Active, Suspended, Expired
    restrictions = Column(String)  # Any conditions or restrictions
    
    electrician = relationship("Electrician", back_populates="licenses")

class Qualification(Base):
    __tablename__ = "qualifications"
    
    id = Column(Integer, primary_key=True)
    electrician_id = Column(Integer, ForeignKey("electricians.id"))
    qualification_type = Column(SQLEnum(QualificationType))
    institution = Column(String, nullable=False)
    completion_date = Column(DateTime, nullable=False)
    certificate_number = Column(String)
    
    electrician = relationship("Electrician", back_populates="qualifications")

class Certification(Base):
    __tablename__ = "certifications"
    
    id = Column(Integer, primary_key=True)
    electrician_id = Column(Integer, ForeignKey("electricians.id"))
    certification_type = Column(SQLEnum(CertificationType))
    issuing_body = Column(String, nullable=False)
    issue_date = Column(DateTime, nullable=False)
    expiry_date = Column(DateTime)
    certificate_number = Column(String)
    status = Column(String)  # Active, Expired, Pending Renewal
    
    electrician = relationship("Electrician", back_populates="certifications")

class Electrician(Base):
    __tablename__ = "electricians"
    
    id = Column(Integer, primary_key=True)
    full_name = Column(String, nullable=False)
    years_experience = Column(Integer)
    hourly_rate = Column(Integer)
    available_from = Column(DateTime)
    preferred_locations = Column(String)  # JSON array of AustralianState
    
    # Compliance and Verification
    primary_license_state = Column(SQLEnum(AustralianState), nullable=False)
    insurance_status = Column(Boolean, default=False)
    insurance_expiry = Column(DateTime)
    insurance_policy_number = Column(String)
    verified_status = Column(Boolean, default=False)
    profile_completion = Column(Integer)  # Percentage of profile completed
    
    # Relationships
    licenses = relationship("License", back_populates="electrician")
    qualifications = relationship("Qualification", back_populates="electrician")
    certifications = relationship("Certification", back_populates="electrician")
    projects = relationship("Project", back_populates="electrician")
    skills = relationship("Skill", back_populates="electrician")

class Project(Base):
    __tablename__ = "projects"
    
    id = Column(Integer, primary_key=True)
    electrician_id = Column(Integer, ForeignKey("electricians.id"))
    project_type = Column(SQLEnum(ProjectType))
    project_value = Column(Integer)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    description = Column(String)
    tools_used = Column(String)  # JSON string of tools
    role_description = Column(String)
    
    # New fields for standardized experience tracking
    voltage_levels = Column(String)  # JSON array of VoltageLevel
    role = Column(SQLEnum(ProjectRole))
    specialties = Column(String)  # JSON array of SpecialtyArea
    team_size = Column(Integer)
    safety_incidents = Column(Integer, default=0)
    compliance_standards = Column(String)  # JSON array of compliance standards met
    key_achievements = Column(String)  # JSON array of standardized achievements
    
    electrician = relationship("Electrician", back_populates="projects")

class Skill(Base):
    __tablename__ = "skills"
    
    id = Column(Integer, primary_key=True)
    electrician_id = Column(Integer, ForeignKey("electricians.id"))
    specialty = Column(SQLEnum(SpecialtyArea))
    years_experience = Column(Integer)
    proficiency_level = Column(Integer)  # 1-5 scale
    last_used_date = Column(DateTime)
    
    electrician = relationship("Electrician", back_populates="skills")

class UserRole(str, Enum):
    HIRER = "hirer"
    OPERATOR = "operator"
    ADMIN = "admin"

class RFQStatus(str, Enum):
    PENDING = "pending"
    ACCEPTED = "accepted"
    DECLINED = "declined"
    EXPIRED = "expired"

class ModerationStatus(str, Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    role = Column(SQLEnum(UserRole), nullable=False)
    full_name = Column(String(255), nullable=False)
    phone = Column(String(20))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted_at = Column(DateTime)
    
    # Relationship
    operator = relationship("Operator", back_populates="user", uselist=False)

class Operator(Base):
    __tablename__ = 'operators'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    business_name = Column(String(255), nullable=False, unique=True)
    abn = Column(String(11))
    description = Column(Text)
    
    # Replace PostGIS Geography with simple lat/long
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    
    service_radius = Column(Integer, nullable=False)  # in meters
    operating_hours = Column(String)  # JSON string
    website = Column(String(255))
    address_line1 = Column(String(255), nullable=False)
    address_line2 = Column(String(255))
    suburb = Column(String(100), nullable=False)
    state = Column(String(50), nullable=False)
    postcode = Column(String(10), nullable=False)
    moderation_status = Column(SQLEnum(ModerationStatus), nullable=False, default=ModerationStatus.PENDING)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted_at = Column(DateTime)

    # Relationship
    user = relationship("User", back_populates="operator")
    equipment = relationship("Equipment", back_populates="operator")

class EquipmentCategory(Base):
    __tablename__ = 'equipment_categories'
    
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('equipment_categories.id'))
    name = Column(String(100), nullable=False, unique=True)
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Self-referential relationship
    parent = relationship("EquipmentCategory", remote_side=[id], backref="subcategories")
    equipment = relationship("Equipment", back_populates="category")

class Equipment(Base):
    __tablename__ = 'equipment'
    
    id = Column(Integer, primary_key=True)
    operator_id = Column(Integer, ForeignKey('operators.id'), nullable=False)
    category_id = Column(Integer, ForeignKey('equipment_categories.id'), nullable=False)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    specifications = Column(String)  # JSON string
    daily_rate = Column(Float)
    weekly_rate = Column(Float)
    monthly_rate = Column(Float)
    availability_status = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    operator = relationship("Operator", back_populates="equipment")
    category = relationship("EquipmentCategory", back_populates="equipment")
