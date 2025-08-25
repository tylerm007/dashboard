# coding: utf-8
from sqlalchemy.dialects.mysql import *
from sqlalchemy import Boolean, Column, Computed, DECIMAL, Date, Float, ForeignKey, Index, Integer, LargeBinary, NCHAR, String, Table, Unicode, Uuid, text
from sqlalchemy.dialects.mssql import DATETIME2
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  August 25, 2025 14:57:08
# Database: mssql+pyodbc://apilogic:2Rtrzc8iLovpU!Hv8gG*@kash-sql-st.nyc.ou.org/dashboard?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=no&Encrypt=no
# Dialect:  mssql
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX, TestBase
from flask_login import UserMixin
import safrs, flask_sqlalchemy, os
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.mssql import *

if os.getenv('APILOGICPROJECT_NO_FLASK') is None or os.getenv('APILOGICPROJECT_NO_FLASK') == 'None':
    Base = SAFRSBaseX   # enables rules to be used outside of Flask, e.g., test data loading
else:
    Base = TestBase     # ensure proper types, so rules work for data loading
    print('*** Models.py Using TestBase ***')



class ProcessDefinition(Base):  # type: ignore
    __tablename__ = 'ProcessDefinitions'
    _s_collection_name = 'ProcessDefinition'  # type: ignore

    ProcessId = Column(Uuid, server_default=text("newid()"), primary_key=True)
    ProcessName = Column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    ProcessVersion = Column(Unicode(10, 'SQL_Latin1_General_CP1_CI_AS'), server_default=text("1.0"), nullable=False)
    Description = Column(Unicode(500, 'SQL_Latin1_General_CP1_CI_AS'))
    IsActive = Column(Boolean, server_default=text("1"), nullable=False)
    CreatedDate = Column(DATETIME2, server_default=text("(getutcdate())"), nullable=False)
    CreatedBy = Column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    ModifiedDate = Column(DATETIME2)
    ModifiedBy = Column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    allow_client_generated_ids = True

    # parent relationships (access parent)

    # child relationships (access children)
    LaneDefinitionList : Mapped[List["LaneDefinition"]] = relationship(back_populates="Process")
    TaskDefinitionList : Mapped[List["TaskDefinition"]] = relationship(back_populates="Process")
    ProcessInstanceList : Mapped[List["ProcessInstance"]] = relationship(back_populates="Process")



t_ProcessOverview = Table(
    'ProcessOverview', metadata,
    Column('ProcessId', Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('ProcessName', Unicode(255, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('IsExecutable', Boolean, nullable=False),
    Column('LaneCount', Integer),
    Column('NodeCount', Integer),
    Column('FlowCount', Integer)
)


class ValidationRule(Base):  # type: ignore
    __tablename__ = 'ValidationRules'
    _s_collection_name = 'ValidationRule'  # type: ignore

    ValidationId = Column(Uuid, server_default=text("newid()"), primary_key=True)
    ValidationName = Column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    Category = Column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    RuleType = Column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    ValidationQuery = Column(Unicode(collation='SQL_Latin1_General_CP1_CI_AS'))
    ErrorMessage = Column(Unicode(500, 'SQL_Latin1_General_CP1_CI_AS'))
    IsActive = Column(Boolean, server_default=text("1"), nullable=False)
    CreatedDate = Column(DATETIME2, server_default=text("(getutcdate())"), nullable=False)
    allow_client_generated_ids = True

    # parent relationships (access parent)

    # child relationships (access children)
    ValidationResultList : Mapped[List["ValidationResult"]] = relationship(back_populates="Validation")



class WFActivityStatus(Base):  # type: ignore
    __tablename__ = 'WF_ActivityStatus'
    _s_collection_name = 'WFActivityStatus'  # type: ignore

    StatusCode = Column(Unicode(5, 'SQL_Latin1_General_CP1_CI_AS'), primary_key=True)
    StatusDesc = Column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'))
    allow_client_generated_ids = True

    # parent relationships (access parent)

    # child relationships (access children)
    WFActivityLogList : Mapped[List["WFActivityLog"]] = relationship(back_populates="WF_ActivityStatu")



class WFApplicationStatus(Base):  # type: ignore
    __tablename__ = 'WF_ApplicationStatus'
    _s_collection_name = 'WFApplicationStatus'  # type: ignore

    StatusCode = Column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'), primary_key=True)
    StatusDescription = Column(Unicode(255, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    allow_client_generated_ids = True

    # parent relationships (access parent)

    # child relationships (access children)
    WFApplicationList : Mapped[List["WFApplication"]] = relationship(back_populates="WF_ApplicationStatu")



class WFDashboard(Base):  # type: ignore
    __tablename__ = 'WF_Dashboard'
    _s_collection_name = 'WFDashboard'  # type: ignore

    ID = Column(Integer, server_default=text("0"), primary_key=True)
    count_new = Column(Integer, server_default=text("0"))
    count_in_progress = Column(Integer, server_default=text("0"))
    count_withdrawn = Column(Integer, server_default=text("0"))
    count_completed = Column(Integer, server_default=text("0"))
    count_overdue = Column(Integer, server_default=text("0"))
    total_count = Column(Integer, server_default=text("0"))

    # parent relationships (access parent)

    # child relationships (access children)
    WFApplicationList : Mapped[List["WFApplication"]] = relationship(back_populates="WFDashboard")



class WFFileType(Base):  # type: ignore
    __tablename__ = 'WF_FileTypes'
    _s_collection_name = 'WFFileType'  # type: ignore

    FileType = Column(Unicode(5, 'SQL_Latin1_General_CP1_CI_AS'), primary_key=True)
    FileTypeName = Column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    allow_client_generated_ids = True

    # parent relationships (access parent)

    # child relationships (access children)
    WFFileList : Mapped[List["WFFile"]] = relationship(back_populates="WF_FileType")



class WFPriority(Base):  # type: ignore
    __tablename__ = 'WF_Priorities'
    _s_collection_name = 'WFPriority'  # type: ignore

    PriorityCode = Column(Unicode(20, 'SQL_Latin1_General_CP1_CI_AS'), primary_key=True)
    PriorityDescription = Column(Unicode(255, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    allow_client_generated_ids = True

    # parent relationships (access parent)

    # child relationships (access children)
    WFApplicationList : Mapped[List["WFApplication"]] = relationship(back_populates="WF_Priority")



class WFProcessPriority(Base):  # type: ignore
    __tablename__ = 'WF_ProcessPriorities'
    _s_collection_name = 'WFProcessPriority'  # type: ignore

    PriorityCode = Column(Unicode(10, 'SQL_Latin1_General_CP1_CI_AS'), primary_key=True)
    PriorityDescription = Column(Unicode(255, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    allow_client_generated_ids = True

    # parent relationships (access parent)

    # child relationships (access children)
    ProcessInstanceList : Mapped[List["ProcessInstance"]] = relationship(back_populates="WF_ProcessPriority")



class WFProcessStatus(Base):  # type: ignore
    __tablename__ = 'WF_ProcessStatus'
    _s_collection_name = 'WFProcessStatus'  # type: ignore

    StatusCode = Column(Unicode(10, 'SQL_Latin1_General_CP1_CI_AS'), primary_key=True)
    StatusDescription = Column(Unicode(255, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    allow_client_generated_ids = True

    # parent relationships (access parent)

    # child relationships (access children)
    ProcessInstanceList : Mapped[List["ProcessInstance"]] = relationship(back_populates="WF_ProcessStatus")



class WFQuoteStatus(Base):  # type: ignore
    __tablename__ = 'WF_QuoteStatus'
    _s_collection_name = 'WFQuoteStatus'  # type: ignore

    StatusCode = Column(Unicode(10, 'SQL_Latin1_General_CP1_CI_AS'), primary_key=True)
    StatusDesc = Column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'))
    allow_client_generated_ids = True

    # parent relationships (access parent)

    # child relationships (access children)
    WFQuoteList : Mapped[List["WFQuote"]] = relationship(back_populates="WF_QuoteStatu")



class WFRole(Base):  # type: ignore
    __tablename__ = 'WF_Roles'
    _s_collection_name = 'WFRole'  # type: ignore

    UserRole = Column(Unicode(10, 'SQL_Latin1_General_CP1_CI_AS'), primary_key=True)
    Role = Column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    CreatedDate = Column(DATETIME2, server_default=text("getdate()"), nullable=False)
    allow_client_generated_ids = True

    # parent relationships (access parent)

    # child relationships (access children)
    WFUserList : Mapped[List["WFUser"]] = relationship(back_populates="WF_Role")



class Sysdiagram(Base):  # type: ignore
    __tablename__ = 'sysdiagrams'
    _s_collection_name = 'Sysdiagram'  # type: ignore
    __table_args__ = (
        Index('UK_principal_name', 'principal_id', 'name', unique=True),
    )

    name = Column(NullType, nullable=False)
    principal_id = Column(Integer, nullable=False)
    diagram_id = Column(Integer, server_default=text("0"), primary_key=True)
    version = Column(Integer)
    definition = Column(LargeBinary)

    # parent relationships (access parent)

    # child relationships (access children)



t_vw_ActiveWorkflows = Table(
    'vw_ActiveWorkflows', metadata,
    Column('InstanceId', Uuid, nullable=False),
    Column('ApplicationId', Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('ProcessName', Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('Status', Unicode(10, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('CurrentTask', Unicode(100, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('StartedDate', DATETIME2, nullable=False),
    Column('StartedBy', Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('Priority', Unicode(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('HoursActive', Integer)
)


t_vw_TaskPerformance = Table(
    'vw_TaskPerformance', metadata,
    Column('TaskName', Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('TaskType', Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('TaskCategory', Unicode(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('TotalExecutions', Integer),
    Column('AvgDurationMinutes', Float(53)),
    Column('EstimatedDurationMinutes', Integer),
    Column('CompletedTasks', Integer),
    Column('FailedTasks', Integer),
    Column('SuccessRate', Float(53))
)


t_vw_ValidationStatus = Table(
    'vw_ValidationStatus', metadata,
    Column('InstanceId', Uuid, nullable=False),
    Column('ApplicationId', Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('TotalValidations', Integer),
    Column('PassedValidations', Integer),
    Column('FailedValidations', Integer),
    Column('ValidationStatus', String(12, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
)


t_vw_WorkflowDashboard = Table(
    'vw_WorkflowDashboard', metadata,
    Column('Metric', String(25, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('Value', Float(53)),
    Column('Unit', String(5, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
)


class LaneDefinition(Base):  # type: ignore
    __tablename__ = 'LaneDefinitions'
    _s_collection_name = 'LaneDefinition'  # type: ignore

    LaneId = Column(Uuid, server_default=text("newid()"), primary_key=True)
    ProcessId = Column(ForeignKey('ProcessDefinitions.ProcessId'), nullable=False)
    LaneName = Column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    LaneDescription = Column(Unicode(500, 'SQL_Latin1_General_CP1_CI_AS'))
    EstimatedDurationDays = Column(Integer)
    CreatedDate = Column(DATETIME2, server_default=text("(getutcdate())"), nullable=False)
    CreatedBy = Column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'), server_default=text("system"), nullable=False)
    allow_client_generated_ids = True

    # parent relationships (access parent)
    Process : Mapped["ProcessDefinition"] = relationship(back_populates=("LaneDefinitionList"))

    # child relationships (access children)
    TaskDefinitionList : Mapped[List["TaskDefinition"]] = relationship(back_populates="Lane")
    StageInstanceList : Mapped[List["StageInstance"]] = relationship(back_populates="Lane")



class WFApplication(Base):  # type: ignore
    __tablename__ = 'WF_Applications'
    _s_collection_name = 'WFApplication'  # type: ignore

    ApplicationID = Column(Integer, server_default=text("0"), primary_key=True, index=True)
    ApplicationNumber = Column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False, unique=True)
    CompanyID = Column(Integer, nullable=False, index=True)
    PlantID = Column(Integer)
    SubmissionDate = Column(Date, nullable=False)
    Status = Column(ForeignKey('WF_ApplicationStatus.StatusCode'), server_default=text("NEW"), nullable=False, index=True)
    Priority = Column(ForeignKey('WF_Priorities.PriorityCode'), server_default=text("NORMAL"))
    PrimaryContactName = Column(Unicode(200, 'SQL_Latin1_General_CP1_CI_AS'))
    Version = Column(Unicode(20, 'SQL_Latin1_General_CP1_CI_AS'), server_default=text("1.0.0"), nullable=False)
    CreatedDate = Column(DATETIME2, server_default=text("getdate()"), nullable=False)
    LastUpdatedDate = Column(DATETIME2, server_default=text("getdate()"), nullable=False)
    LastStatusChangeDate = Column(DATETIME2, server_default=text("getdate()"), nullable=False)
    LastStatusChangedBy = Column(Unicode(200, 'SQL_Latin1_General_CP1_CI_AS'))
    WFDashboardID = Column(ForeignKey('WF_Dashboard.ID'), server_default=text("1"))

    # parent relationships (access parent)
    WF_Priority : Mapped["WFPriority"] = relationship(back_populates=("WFApplicationList"))
    WF_ApplicationStatu : Mapped["WFApplicationStatus"] = relationship(back_populates=("WFApplicationList"))
    WFDashboard : Mapped["WFDashboard"] = relationship(back_populates=("WFApplicationList"))

    # child relationships (access children)
    CompanyList : Mapped[List["Company"]] = relationship(back_populates="Application")
    ContactList : Mapped[List["Contact"]] = relationship(back_populates="Application")
    IngredientList : Mapped[List["Ingredient"]] = relationship(back_populates="Application")
    PlantList : Mapped[List["Plant"]] = relationship(back_populates="Application")
    ProductList : Mapped[List["Product"]] = relationship(back_populates="Application")
    ValidationCheckList : Mapped[List["ValidationCheck"]] = relationship(back_populates="Application")
    WFActivityLogList : Mapped[List["WFActivityLog"]] = relationship(back_populates="Application")
    WFCommentList : Mapped[List["WFComment"]] = relationship(back_populates="Application")
    WFFileList : Mapped[List["WFFile"]] = relationship(back_populates="Application")
    WFMessageList : Mapped[List["WFMessage"]] = relationship(back_populates="Application")
    WFQuoteList : Mapped[List["WFQuote"]] = relationship(back_populates="Application")



class WFUser(Base):  # type: ignore
    __tablename__ = 'WF_Users'
    _s_collection_name = 'WFUser'  # type: ignore

    UserID = Column(Integer, server_default=text("0"), primary_key=True)
    Username = Column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False, unique=True)
    FullName = Column(Unicode(200, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    Email = Column(Unicode(255, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False, unique=True)
    Role = Column(ForeignKey('WF_Roles.UserRole'), server_default=text("ADMIN"), nullable=False)
    IsActive = Column(Boolean, server_default=text("1"), nullable=False)
    CreatedDate = Column(DATETIME2, server_default=text("getdate()"), nullable=False)
    LastLoginDate = Column(DATETIME2)

    # parent relationships (access parent)
    WF_Role : Mapped["WFRole"] = relationship(back_populates=("WFUserList"))

    # child relationships (access children)



class Company(Base):  # type: ignore
    __tablename__ = 'Companies'
    _s_collection_name = 'Company'  # type: ignore

    CompanyID = Column(Integer, server_default=text("0"), primary_key=True)
    ApplicationID = Column(ForeignKey('WF_Applications.ApplicationID'), nullable=False)
    KashrusCompanyID = Column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    CompanyName = Column(Unicode(500, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    Category = Column(Unicode(200, 'SQL_Latin1_General_CP1_CI_AS'))
    CurrentlyCertified = Column(Boolean, server_default=text("0"), nullable=False)
    EverCertified = Column(Boolean, server_default=text("0"), nullable=False)
    StreetAddress = Column(Unicode(500, 'SQL_Latin1_General_CP1_CI_AS'))
    AddressLine2 = Column(Unicode(500, 'SQL_Latin1_General_CP1_CI_AS'))
    City = Column(Unicode(200, 'SQL_Latin1_General_CP1_CI_AS'))
    State = Column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    Country = Column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    ZipCode = Column(Unicode(20, 'SQL_Latin1_General_CP1_CI_AS'))
    Website = Column(Unicode(500, 'SQL_Latin1_General_CP1_CI_AS'))
    OwnBrand = Column(Boolean, server_default=text("0"), nullable=False)
    CopackerDirectory = Column(Boolean, server_default=text("0"), nullable=False)
    VeganCertification = Column(Boolean, server_default=text("0"), nullable=False)
    PlantCount = Column(Integer, server_default=text("0"), nullable=False)
    CreatedDate = Column(DATETIME2, server_default=text("getdate()"), nullable=False)
    LastUpdatedDate = Column(DATETIME2, server_default=text("getdate()"), nullable=False)

    # parent relationships (access parent)
    Application : Mapped["WFApplication"] = relationship(back_populates=("CompanyList"))

    # child relationships (access children)



class Contact(Base):  # type: ignore
    __tablename__ = 'Contacts'
    _s_collection_name = 'Contact'  # type: ignore

    ContactID = Column(Integer, server_default=text("0"), primary_key=True)
    ApplicationID = Column(ForeignKey('WF_Applications.ApplicationID'), nullable=False)
    ContactType = Column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    FullName = Column(Unicode(200, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    JobTitle = Column(Unicode(200, 'SQL_Latin1_General_CP1_CI_AS'))
    Phone = Column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'))
    Email = Column(Unicode(255, 'SQL_Latin1_General_CP1_CI_AS'))
    IsPrimary = Column(Boolean, server_default=text("0"), nullable=False)
    Role = Column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    CreatedDate = Column(DATETIME2, server_default=text("getdate()"), nullable=False)

    # parent relationships (access parent)
    Application : Mapped["WFApplication"] = relationship(back_populates=("ContactList"))

    # child relationships (access children)



class Ingredient(Base):  # type: ignore
    __tablename__ = 'Ingredients'
    _s_collection_name = 'Ingredient'  # type: ignore

    IngredientID = Column(Integer, server_default=text("0"), primary_key=True)
    ApplicationID = Column(ForeignKey('WF_Applications.ApplicationID'), nullable=False, index=True)
    NCRCIngredientID = Column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False, index=True)
    Source = Column(Unicode(200, 'SQL_Latin1_General_CP1_CI_AS'))
    UKDID = Column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    RMC = Column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    IngredientName = Column(Unicode(500, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    Manufacturer = Column(Unicode(500, 'SQL_Latin1_General_CP1_CI_AS'))
    Brand = Column(Unicode(500, 'SQL_Latin1_General_CP1_CI_AS'))
    Packaging = Column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    CertificationAgency = Column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'))
    AddedDate = Column(Date, nullable=False)
    AddedBy = Column(Unicode(200, 'SQL_Latin1_General_CP1_CI_AS'))
    Status = Column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'), server_default=text("Original"), nullable=False)
    CreatedDate = Column(DATETIME2, server_default=text("getdate()"), nullable=False)

    # parent relationships (access parent)
    Application : Mapped["WFApplication"] = relationship(back_populates=("IngredientList"))

    # child relationships (access children)



class Plant(Base):  # type: ignore
    __tablename__ = 'Plants'
    _s_collection_name = 'Plant'  # type: ignore

    PlantID = Column(Integer, server_default=text("0"), primary_key=True)
    ApplicationID = Column(ForeignKey('WF_Applications.ApplicationID'), nullable=False, index=True)
    PlantNumber = Column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    PlantName = Column(Unicode(500, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    StreetAddress = Column(Unicode(500, 'SQL_Latin1_General_CP1_CI_AS'))
    AddressLine2 = Column(Unicode(500, 'SQL_Latin1_General_CP1_CI_AS'))
    City = Column(Unicode(200, 'SQL_Latin1_General_CP1_CI_AS'))
    State = Column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    Country = Column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    Province = Column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    Region = Column(Unicode(200, 'SQL_Latin1_General_CP1_CI_AS'))
    ZipCode = Column(Unicode(20, 'SQL_Latin1_General_CP1_CI_AS'))
    ContactName = Column(Unicode(200, 'SQL_Latin1_General_CP1_CI_AS'))
    ContactTitle = Column(Unicode(200, 'SQL_Latin1_General_CP1_CI_AS'))
    ContactPhone = Column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'))
    ContactEmail = Column(Unicode(255, 'SQL_Latin1_General_CP1_CI_AS'))
    ManufacturingProcess = Column(Unicode(collation='SQL_Latin1_General_CP1_CI_AS'))
    ClosestMajorCity = Column(Unicode(200, 'SQL_Latin1_General_CP1_CI_AS'))
    HasOtherProducts = Column(Boolean, server_default=text("0"), nullable=False)
    OtherProductsList = Column(Unicode(1000, 'SQL_Latin1_General_CP1_CI_AS'))
    HasOtherPlants = Column(Boolean, server_default=text("0"), nullable=False)
    OtherPlantsLocation = Column(Unicode(1000, 'SQL_Latin1_General_CP1_CI_AS'))
    OperationalStatus = Column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'), server_default=text("Active"), nullable=False)
    LastInspection = Column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    ComplianceStatus = Column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    CreatedDate = Column(DATETIME2, server_default=text("getdate()"), nullable=False)

    # parent relationships (access parent)
    Application : Mapped["WFApplication"] = relationship(back_populates=("PlantList"))

    # child relationships (access children)



class Product(Base):  # type: ignore
    __tablename__ = 'Products'
    _s_collection_name = 'Product'  # type: ignore

    ProductID = Column(Integer, server_default=text("0"), primary_key=True)
    ApplicationID = Column(ForeignKey('WF_Applications.ApplicationID'), nullable=False, index=True)
    Source = Column(Unicode(200, 'SQL_Latin1_General_CP1_CI_AS'))
    LabelName = Column(Unicode(500, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    BrandName = Column(Unicode(500, 'SQL_Latin1_General_CP1_CI_AS'))
    LabelCompany = Column(Unicode(500, 'SQL_Latin1_General_CP1_CI_AS'))
    ConsumerIndustrial = Column(NCHAR(1, 'SQL_Latin1_General_CP1_CI_AS'))
    BulkShipped = Column(NCHAR(1, 'SQL_Latin1_General_CP1_CI_AS'))
    CertificationSymbol = Column(Unicode(20, 'SQL_Latin1_General_CP1_CI_AS'))
    Status = Column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'), server_default=text("submitted"), nullable=False)
    Category = Column(Unicode(200, 'SQL_Latin1_General_CP1_CI_AS'))
    CreatedDate = Column(DATETIME2, server_default=text("getdate()"), nullable=False)

    # parent relationships (access parent)
    Application : Mapped["WFApplication"] = relationship(back_populates=("ProductList"))

    # child relationships (access children)



class TaskDefinition(Base):  # type: ignore
    __tablename__ = 'TaskDefinitions'
    _s_collection_name = 'TaskDefinition'  # type: ignore

    TaskId = Column(Uuid, server_default=text("newid()"), primary_key=True)
    ProcessId = Column(ForeignKey('ProcessDefinitions.ProcessId'), nullable=False)
    TaskName = Column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    TaskType = Column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    TaskCategory = Column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'))
    Sequence = Column(Integer, nullable=False)
    IsParallel = Column(Boolean, server_default=text("0"), nullable=False)
    AssigneeRole = Column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'))
    EstimatedDurationMinutes = Column(Integer)
    IsRequired = Column(Boolean, server_default=text("1"), nullable=False)
    AutoComplete = Column(Boolean, server_default=text("0"), nullable=False)
    Description = Column(Unicode(500, 'SQL_Latin1_General_CP1_CI_AS'))
    ConfigurationJson = Column(Unicode(collation='SQL_Latin1_General_CP1_CI_AS'))
    LaneId = Column(ForeignKey('LaneDefinitions.LaneId'))
    allow_client_generated_ids = True

    # parent relationships (access parent)
    Lane : Mapped["LaneDefinition"] = relationship(back_populates=("TaskDefinitionList"))
    Process : Mapped["ProcessDefinition"] = relationship(back_populates=("TaskDefinitionList"))

    # child relationships (access children)
    ProcessInstanceList : Mapped[List["ProcessInstance"]] = relationship(back_populates="CurrentTask")
    TaskFlowList : Mapped[List["TaskFlow"]] = relationship(foreign_keys='[TaskFlow.FromTaskId]', back_populates="FromTask")
    ToTaskTaskFlowList : Mapped[List["TaskFlow"]] = relationship(foreign_keys='[TaskFlow.ToTaskId]', back_populates="ToTask")
    TaskInstanceList : Mapped[List["TaskInstance"]] = relationship(back_populates="Task")



class ValidationCheck(Base):  # type: ignore
    __tablename__ = 'ValidationChecks'
    _s_collection_name = 'ValidationCheck'  # type: ignore
    __table_args__ = (
        Index('UQ__Validati__E2DAF7F574543B14', 'ApplicationID', 'CheckType', unique=True),
    )

    ValidationID = Column(Integer, server_default=text("0"), primary_key=True)
    ApplicationID = Column(ForeignKey('WF_Applications.ApplicationID'), nullable=False)
    CheckType = Column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    IsValid = Column(Boolean, server_default=text("0"), nullable=False)
    ValidationMessage = Column(Unicode(1000, 'SQL_Latin1_General_CP1_CI_AS'))
    LastCheckedDate = Column(DATETIME2, server_default=text("getdate()"), nullable=False)

    # parent relationships (access parent)
    Application : Mapped["WFApplication"] = relationship(back_populates=("ValidationCheckList"))

    # child relationships (access children)



class WFActivityLog(Base):  # type: ignore
    __tablename__ = 'WF_ActivityLog'
    _s_collection_name = 'WFActivityLog'  # type: ignore

    ActivityID = Column(Integer, server_default=text("0"), primary_key=True)
    ApplicationID = Column(ForeignKey('WF_Applications.ApplicationID'), nullable=False, index=True)
    ActionType = Column(Unicode(200, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    ActionDetails = Column(Unicode(collation='SQL_Latin1_General_CP1_CI_AS'))
    UserName = Column(Unicode(200, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    ActivityType = Column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    Status = Column(ForeignKey('WF_ActivityStatus.StatusCode'), server_default=text("APP"), nullable=False)
    Category = Column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    ActivityDate = Column(DATETIME2, server_default=text("getdate()"), nullable=False, index=True)

    # parent relationships (access parent)
    Application : Mapped["WFApplication"] = relationship(back_populates=("WFActivityLogList"))
    WF_ActivityStatu : Mapped["WFActivityStatus"] = relationship(back_populates=("WFActivityLogList"))

    # child relationships (access children)



class WFComment(Base):  # type: ignore
    __tablename__ = 'WF_Comments'
    _s_collection_name = 'WFComment'  # type: ignore

    CommentID = Column(Integer, server_default=text("0"), primary_key=True)
    ApplicationID = Column(ForeignKey('WF_Applications.ApplicationID'), nullable=False, index=True)
    Author = Column(Unicode(200, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    CommentText = Column(Unicode(collation='SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    CommentType = Column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'), server_default=text("internal"), nullable=False)
    Category = Column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    CreatedDate = Column(DATETIME2, server_default=text("getdate()"), nullable=False)

    # parent relationships (access parent)
    Application : Mapped["WFApplication"] = relationship(back_populates=("WFCommentList"))

    # child relationships (access children)



class WFFile(Base):  # type: ignore
    __tablename__ = 'WF_Files'
    _s_collection_name = 'WFFile'  # type: ignore

    FileID = Column(Integer, server_default=text("0"), primary_key=True)
    ApplicationID = Column(ForeignKey('WF_Applications.ApplicationID'), nullable=False, index=True)
    FileName = Column(Unicode(500, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    FileType = Column(ForeignKey('WF_FileTypes.FileType'), nullable=False)
    FileSize = Column(Unicode(20, 'SQL_Latin1_General_CP1_CI_AS'))
    UploadedDate = Column(Date, nullable=False)
    Tag = Column(Unicode(200, 'SQL_Latin1_General_CP1_CI_AS'))
    IsProcessed = Column(Boolean, server_default=text("0"), nullable=False)
    RecordCount = Column(Integer)
    FilePath = Column(Unicode(1000, 'SQL_Latin1_General_CP1_CI_AS'))
    CreatedDate = Column(DATETIME2, server_default=text("getdate()"), nullable=False)

    # parent relationships (access parent)
    Application : Mapped["WFApplication"] = relationship(back_populates=("WFFileList"))
    WF_FileType : Mapped["WFFileType"] = relationship(back_populates=("WFFileList"))

    # child relationships (access children)



class WFMessage(Base):  # type: ignore
    __tablename__ = 'WF_Messages'
    _s_collection_name = 'WFMessage'  # type: ignore

    MessageID = Column(Integer, server_default=text("0"), primary_key=True)
    ApplicationID = Column(ForeignKey('WF_Applications.ApplicationID'), nullable=False, index=True)
    FromUser = Column(Unicode(200, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    ToUser = Column(Unicode(200, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    MessageText = Column(Unicode(collation='SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    MessageType = Column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'), server_default=text("outgoing"), nullable=False)
    Priority = Column(Unicode(20, 'SQL_Latin1_General_CP1_CI_AS'), server_default=text("normal"), nullable=False)
    SentDate = Column(DATETIME2, server_default=text("getdate()"), nullable=False)

    # parent relationships (access parent)
    Application : Mapped["WFApplication"] = relationship(back_populates=("WFMessageList"))

    # child relationships (access children)



class WFQuote(Base):  # type: ignore
    __tablename__ = 'WF_Quotes'
    _s_collection_name = 'WFQuote'  # type: ignore

    QuoteID = Column(Integer, server_default=text("0"), primary_key=True)
    ApplicationID = Column(ForeignKey('WF_Applications.ApplicationID'), nullable=False, index=True)
    QuoteNumber = Column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False, unique=True)
    TotalAmount : DECIMAL = Column(DECIMAL(10, 2), nullable=False)
    ValidUntil = Column(Date, nullable=False)
    Status = Column(ForeignKey('WF_QuoteStatus.StatusCode'), server_default=text("PEND"), nullable=False)
    LastUpdatedDate = Column(Date, nullable=False)
    CreatedDate = Column(DATETIME2, server_default=text("getdate()"), nullable=False)

    # parent relationships (access parent)
    Application : Mapped["WFApplication"] = relationship(back_populates=("WFQuoteList"))
    WF_QuoteStatu : Mapped["WFQuoteStatus"] = relationship(back_populates=("WFQuoteList"))

    # child relationships (access children)
    WFQuoteItemList : Mapped[List["WFQuoteItem"]] = relationship(back_populates="Quote")



class ProcessInstance(Base):  # type: ignore
    __tablename__ = 'ProcessInstances'
    _s_collection_name = 'ProcessInstance'  # type: ignore

    InstanceId = Column(Uuid, server_default=text("newid()"), primary_key=True)
    ProcessId = Column(ForeignKey('ProcessDefinitions.ProcessId'), nullable=False)
    ApplicationId = Column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False, index=True)
    Status = Column(ForeignKey('WF_ProcessStatus.StatusCode'), server_default=text("NEW"), nullable=False, index=True)
    CurrentTaskId = Column(ForeignKey('TaskDefinitions.TaskId'))
    StartedDate = Column(DATETIME2, server_default=text("(getutcdate())"), nullable=False, index=True)
    StartedBy = Column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    CompletedDate = Column(DATETIME2)
    CompletedBy = Column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    Priority = Column(ForeignKey('WF_ProcessPriorities.PriorityCode'), server_default=text("NORMAL"))
    ContextData = Column(Unicode(collation='SQL_Latin1_General_CP1_CI_AS'))
    allow_client_generated_ids = True

    # parent relationships (access parent)
    CurrentTask : Mapped["TaskDefinition"] = relationship(back_populates=("ProcessInstanceList"))
    WF_ProcessPriority : Mapped["WFProcessPriority"] = relationship(back_populates=("ProcessInstanceList"))
    Process : Mapped["ProcessDefinition"] = relationship(back_populates=("ProcessInstanceList"))
    WF_ProcessStatus : Mapped["WFProcessStatus"] = relationship(back_populates=("ProcessInstanceList"))

    # child relationships (access children)
    MessageList : Mapped[List["Message"]] = relationship(back_populates="Instance")
    StageInstanceList : Mapped[List["StageInstance"]] = relationship(back_populates="ProcessInstance")
    TaskInstanceList : Mapped[List["TaskInstance"]] = relationship(back_populates="Instance")
    CommentList : Mapped[List["Comment"]] = relationship(back_populates="Instance")
    ValidationResultList : Mapped[List["ValidationResult"]] = relationship(back_populates="Instance")
    WorkflowHistoryList : Mapped[List["WorkflowHistory"]] = relationship(back_populates="Instance")



class TaskFlow(Base):  # type: ignore
    __tablename__ = 'TaskFlow'
    _s_collection_name = 'TaskFlow'  # type: ignore

    FlowId = Column(Uuid, server_default=text("newid()"), primary_key=True)
    FromTaskId = Column(ForeignKey('TaskDefinitions.TaskId'))
    ToTaskId = Column(ForeignKey('TaskDefinitions.TaskId'), nullable=False)
    Condition = Column(Unicode(500, 'SQL_Latin1_General_CP1_CI_AS'))
    IsDefault = Column(Boolean, server_default=text("0"), nullable=False)
    allow_client_generated_ids = True

    # parent relationships (access parent)
    FromTask : Mapped["TaskDefinition"] = relationship(foreign_keys='[TaskFlow.FromTaskId]', back_populates=("TaskFlowList"))
    ToTask : Mapped["TaskDefinition"] = relationship(foreign_keys='[TaskFlow.ToTaskId]', back_populates=("ToTaskTaskFlowList"))

    # child relationships (access children)



class WFQuoteItem(Base):  # type: ignore
    __tablename__ = 'WF_QuoteItems'
    _s_collection_name = 'WFQuoteItem'  # type: ignore

    QuoteItemID = Column(Integer, server_default=text("0"), primary_key=True)
    QuoteID = Column(ForeignKey('WF_Quotes.QuoteID'), nullable=False)
    Description = Column(Unicode(500, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    Amount : DECIMAL = Column(DECIMAL(10, 2), nullable=False)
    SortOrder = Column(Integer, server_default=text("1"), nullable=False)

    # parent relationships (access parent)
    Quote : Mapped["WFQuote"] = relationship(back_populates=("WFQuoteItemList"))

    # child relationships (access children)



class Message(Base):  # type: ignore
    __tablename__ = 'Messages'
    _s_collection_name = 'Message'  # type: ignore

    MessageId = Column(Uuid, server_default=text("newid()"), primary_key=True)
    InstanceId = Column(ForeignKey('ProcessInstances.InstanceId'), nullable=False)
    FromUser = Column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    ToUser = Column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'), index=True)
    ToRole = Column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'))
    MessageType = Column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'), server_default=text("Standard"))
    Subject = Column(Unicode(200, 'SQL_Latin1_General_CP1_CI_AS'))
    MessageBody = Column(Unicode(collation='SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    SentDate = Column(DATETIME2, server_default=text("(getutcdate())"), nullable=False)
    ReadDate = Column(DATETIME2)
    IsRead = Column(Boolean, server_default=text("0"), nullable=False, index=True)
    allow_client_generated_ids = True

    # parent relationships (access parent)
    Instance : Mapped["ProcessInstance"] = relationship(back_populates=("MessageList"))

    # child relationships (access children)



class StageInstance(Base):  # type: ignore
    __tablename__ = 'StageInstance'
    _s_collection_name = 'StageInstance'  # type: ignore

    StageInstanceId = Column(Uuid, server_default=text("newid()"), primary_key=True)
    ProcessInstanceId = Column(ForeignKey('ProcessInstances.InstanceId'), nullable=False)
    LaneId = Column(ForeignKey('LaneDefinitions.LaneId'), nullable=False)
    Status = Column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'), server_default=text("Pending"), nullable=False)
    StartedDate = Column(DATETIME2)
    CompletedDate = Column(DATETIME2)
    DurationMinutes = Column(Integer, Computed('(datediff(minute,[StartedDate],[CompletedDate]))', persisted=False))
    RetryCount = Column(Integer, server_default=text("0"))
    CompletedCount = Column(Integer, server_default=text("0"))
    TotalCount = Column(Integer, server_default=text("0"))
    allow_client_generated_ids = True

    # parent relationships (access parent)
    Lane : Mapped["LaneDefinition"] = relationship(back_populates=("StageInstanceList"))
    ProcessInstance : Mapped["ProcessInstance"] = relationship(back_populates=("StageInstanceList"))

    # child relationships (access children)
    TaskInstanceList : Mapped[List["TaskInstance"]] = relationship(back_populates="Stage")



class TaskInstance(Base):  # type: ignore
    __tablename__ = 'TaskInstances'
    _s_collection_name = 'TaskInstance'  # type: ignore

    TaskInstanceId = Column(Uuid, server_default=text("newid()"), primary_key=True)
    InstanceId = Column(ForeignKey('ProcessInstances.InstanceId'), nullable=False)
    TaskId = Column(ForeignKey('TaskDefinitions.TaskId'), nullable=False)
    Status = Column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'), server_default=text("Pending"), nullable=False, index=True)
    AssignedTo = Column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'), index=True)
    StartedDate = Column(DATETIME2, index=True)
    CompletedDate = Column(DATETIME2)
    DurationMinutes = Column(Integer, Computed('(datediff(minute,[StartedDate],[CompletedDate]))', persisted=False))
    Result = Column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'))
    ResultData = Column(Unicode(collation='SQL_Latin1_General_CP1_CI_AS'))
    ErrorMessage = Column(Unicode(1000, 'SQL_Latin1_General_CP1_CI_AS'))
    RetryCount = Column(Integer, server_default=text("0"))
    StageId = Column(ForeignKey('StageInstance.StageInstanceId'))
    allow_client_generated_ids = True

    # parent relationships (access parent)
    Instance : Mapped["ProcessInstance"] = relationship(back_populates=("TaskInstanceList"))
    Stage : Mapped["StageInstance"] = relationship(back_populates=("TaskInstanceList"))
    Task : Mapped["TaskDefinition"] = relationship(back_populates=("TaskInstanceList"))

    # child relationships (access children)
    CommentList : Mapped[List["Comment"]] = relationship(back_populates="TaskInstance")
    ValidationResultList : Mapped[List["ValidationResult"]] = relationship(back_populates="TaskInstance")
    WorkflowHistoryList : Mapped[List["WorkflowHistory"]] = relationship(back_populates="TaskInstance")



class Comment(Base):  # type: ignore
    __tablename__ = 'Comments'
    _s_collection_name = 'Comment'  # type: ignore

    CommentId = Column(Uuid, server_default=text("newid()"), primary_key=True)
    InstanceId = Column(ForeignKey('ProcessInstances.InstanceId'), nullable=False)
    TaskInstanceId = Column(ForeignKey('TaskInstances.TaskInstanceId'))
    CommentType = Column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'), server_default=text("Internal"))
    CommentText = Column(Unicode(collation='SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    Author = Column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    CreatedDate = Column(DATETIME2, server_default=text("(getutcdate())"), nullable=False)
    IsVisible = Column(Boolean, server_default=text("1"), nullable=False)
    allow_client_generated_ids = True

    # parent relationships (access parent)
    Instance : Mapped["ProcessInstance"] = relationship(back_populates=("CommentList"))
    TaskInstance : Mapped["TaskInstance"] = relationship(back_populates=("CommentList"))

    # child relationships (access children)



class ValidationResult(Base):  # type: ignore
    __tablename__ = 'ValidationResults'
    _s_collection_name = 'ValidationResult'  # type: ignore

    ValidationResultId = Column(Uuid, server_default=text("newid()"), primary_key=True)
    InstanceId = Column(ForeignKey('ProcessInstances.InstanceId'), nullable=False, index=True)
    ValidationId = Column(ForeignKey('ValidationRules.ValidationId'), nullable=False)
    TaskInstanceId = Column(ForeignKey('TaskInstances.TaskInstanceId'))
    IsValid = Column(Boolean, nullable=False, index=True)
    ValidationMessage = Column(Unicode(500, 'SQL_Latin1_General_CP1_CI_AS'))
    ValidationDate = Column(DATETIME2, server_default=text("(getutcdate())"), nullable=False)
    ValidatedBy = Column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'))
    allow_client_generated_ids = True

    # parent relationships (access parent)
    Instance : Mapped["ProcessInstance"] = relationship(back_populates=("ValidationResultList"))
    TaskInstance : Mapped["TaskInstance"] = relationship(back_populates=("ValidationResultList"))
    Validation : Mapped["ValidationRule"] = relationship(back_populates=("ValidationResultList"))

    # child relationships (access children)



class WorkflowHistory(Base):  # type: ignore
    __tablename__ = 'WorkflowHistory'
    _s_collection_name = 'WorkflowHistory'  # type: ignore

    HistoryId = Column(Uuid, server_default=text("newid()"), primary_key=True)
    InstanceId = Column(ForeignKey('ProcessInstances.InstanceId'), nullable=False, index=True)
    TaskInstanceId = Column(ForeignKey('TaskInstances.TaskInstanceId'))
    Action = Column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    PreviousStatus = Column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'))
    NewStatus = Column(Unicode(50, 'SQL_Latin1_General_CP1_CI_AS'))
    ActionBy = Column(Unicode(100, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    ActionDate = Column(DATETIME2, server_default=text("(getutcdate())"), nullable=False, index=True)
    ActionReason = Column(Unicode(500, 'SQL_Latin1_General_CP1_CI_AS'))
    Details = Column(Unicode(collation='SQL_Latin1_General_CP1_CI_AS'))
    allow_client_generated_ids = True

    # parent relationships (access parent)
    Instance : Mapped["ProcessInstance"] = relationship(back_populates=("WorkflowHistoryList"))
    TaskInstance : Mapped["TaskInstance"] = relationship(back_populates=("WorkflowHistoryList"))

    # child relationships (access children)
