use dashboard;
-- =============================================
-- Admin Completion Workflow - SQL Server DDL
-- BPMN-based Workflow Management System
-- =============================================

-- Create database schema
-- CREATE SCHEMA workflow;
-- GO

-- =============================================
-- Core Workflow Tables
-- =============================================
-- =============================================
-- Drop Tables (Child Tables First)
-- =============================================

-- Drop views first
IF OBJECT_ID('vw_ActiveWorkflows', 'V') IS NOT NULL DROP VIEW vw_ActiveWorkflows;
IF OBJECT_ID('vw_ValidationStatus', 'V') IS NOT NULL DROP VIEW vw_ValidationStatus;
IF OBJECT_ID('vw_TaskPerformance', 'V') IS NOT NULL DROP VIEW vw_TaskPerformance;
IF OBJECT_ID('vw_WorkflowDashboard', 'V') IS NOT NULL DROP VIEW vw_WorkflowDashboard;
IF OBJECT_ID('vw_BottleneckAnalysis', 'V') IS NOT NULL DROP VIEW vw_BottleneckAnalysis;

-- Drop triggers
IF OBJECT_ID('tr_TaskCompletion_AutoAdvance', 'TR') IS NOT NULL DROP TRIGGER tr_TaskCompletion_AutoAdvance;

-- Drop functions
IF OBJECT_ID('fn_AllValidationsPassed', 'FN') IS NOT NULL DROP FUNCTION fn_AllValidationsPassed;

-- Drop stored procedures
IF OBJECT_ID('sp_StartWorkflowInstance', 'P') IS NOT NULL DROP PROCEDURE sp_StartWorkflowInstance;
IF OBJECT_ID('sp_CompleteTask', 'P') IS NOT NULL DROP PROCEDURE sp_CompleteTask;
IF OBJECT_ID('sp_RunValidationCheck', 'P') IS NOT NULL DROP PROCEDURE sp_RunValidationCheck;
IF OBJECT_ID('sp_AddMessage', 'P') IS NOT NULL DROP PROCEDURE sp_AddMessage;
IF OBJECT_ID('sp_AddComment', 'P') IS NOT NULL DROP PROCEDURE sp_AddComment;
IF OBJECT_ID('sp_GetWorkflowStatus', 'P') IS NOT NULL DROP PROCEDURE sp_GetWorkflowStatus;


-- Drop child tables first (tables with foreign keys)
IF OBJECT_ID('WorkflowHistory', 'U') IS NOT NULL DROP TABLE WorkflowHistory;
IF OBJECT_ID('TaskComments', 'U') IS NOT NULL DROP TABLE TaskComments;
IF OBJECT_ID('ProcessMessages', 'U') IS NOT NULL DROP TABLE ProcessMessages;
IF OBJECT_ID('ValidationResults', 'U') IS NOT NULL DROP TABLE ValidationResults;
IF OBJECT_ID('StageInstance', 'U') IS NOT NULL DROP TABLE StageInstance;
IF OBJECT_ID('TaskInstances', 'U') IS NOT NULL DROP TABLE TaskInstances;
IF OBJECT_ID('ProcessInstances', 'U') IS NOT NULL DROP TABLE ProcessInstances;
IF OBJECT_ID('TaskFlow', 'U') IS NOT NULL DROP TABLE TaskFlow;
IF OBJECT_ID('TaskDefinitions', 'U') IS NOT NULL DROP TABLE TaskDefinitions;
IF OBJECT_ID('LaneDefinitions', 'U') IS NOT NULL DROP TABLE LaneDefinitions;

-- Drop parent tables (tables with primary keys referenced by others)
IF OBJECT_ID('StageStatus', 'U') IS NOT NULL DROP TABLE StageStatus;
IF OBJECT_ID('TaskCommentTypes', 'U') IS NOT NULL DROP TABLE TaskCommentTypes;
IF OBJECT_ID('ProcessMessageTypes', 'U') IS NOT NULL DROP TABLE ProcessMessageTypes;
IF OBJECT_ID('ValidationRules', 'U') IS NOT NULL DROP TABLE ValidationRules;
IF OBJECT_ID('ProcessDefinitions', 'U') IS NOT NULL DROP TABLE ProcessDefinitions;
IF OBJECT_ID('ProcessStatus', 'U') IS NOT NULL DROP TABLE ProcessStatus;
IF OBJECT_ID('ProcessPriorities', 'U') IS NOT NULL DROP TABLE IF EXISTS ProcessPriorities;

PRINT 'All tables, views, procedures, functions, and triggers dropped successfully.';
-- Workflow Process Definitions
CREATE TABLE ProcessDefinitions (
    ProcessId UNIQUEIDENTIFIER PRIMARY KEY DEFAULT NEWID(),
    ProcessName NVARCHAR(100) NOT NULL,
    ProcessVersion NVARCHAR(10) NOT NULL DEFAULT '1.0',
    Description NVARCHAR(500),
    IsActive BIT NOT NULL DEFAULT 1,
    CreatedDate DATETIME2 NOT NULL DEFAULT GETUTCDATE(),
    CreatedBy NVARCHAR(100) NOT NULL,
    ModifiedDate DATETIME2,
    ModifiedBy NVARCHAR(100)
);

CREATE TABLE LaneDefinitions(
	LaneId UNIQUEIDENTIFIER PRIMARY KEY DEFAULT NEWID(),
	ProcessId uniqueidentifier NOT NULL,
	LaneName nvarchar(100) NOT NULL,
	LaneDescription nvarchar(500) NULL,
	EstimatedDurationDays int NULL,
	CreatedDate datetime2(7) NOT NULL DEFAULT GETUTCDATE(),
	CreatedBy nvarchar(100) NOT NULL,
    ModifiedDate datetime2(7) NULL,
    ModifiedBy nvarchar(100) NULL,
    FOREIGN KEY (ProcessId) REFERENCES ProcessDefinitions(ProcessId)
);

-- Task Definitions within Processes
CREATE TABLE TaskDefinitions (
    TaskId UNIQUEIDENTIFIER PRIMARY KEY DEFAULT NEWID(),
    ProcessId UNIQUEIDENTIFIER NOT NULL,
    TaskName NVARCHAR(100) NOT NULL,
    TaskType NVARCHAR(50) NOT NULL, -- 'UserTask', 'ServiceTask', 'ScriptTask', 'Gateway', 'Event'
    TaskCategory NVARCHAR(50), -- 'Validation', 'Action', 'Decision', 'Notification'
    Sequence INT NOT NULL,
    IsParallel BIT NOT NULL DEFAULT 0,
    AssigneeRole NVARCHAR(50),
    EstimatedDurationMinutes INT,
    IsRequired BIT NOT NULL DEFAULT 1,
    AutoComplete BIT NOT NULL DEFAULT 0,
    Description NVARCHAR(500),
    ConfigurationJson NVARCHAR(MAX), -- JSON configuration for task-specific settings
    FOREIGN KEY (ProcessId) REFERENCES ProcessDefinitions(ProcessId)
);

-- Task Dependencies and Flow
CREATE TABLE TaskFlow (
    FlowId UNIQUEIDENTIFIER PRIMARY KEY DEFAULT NEWID(),
    FromTaskId UNIQUEIDENTIFIER,
    ToTaskId UNIQUEIDENTIFIER NOT NULL,
    Condition NVARCHAR(500), -- Conditional logic for flow
    IsDefault BIT NOT NULL DEFAULT 0,
    FOREIGN KEY (FromTaskId) REFERENCES TaskDefinitions(TaskId),
    FOREIGN KEY (ToTaskId) REFERENCES TaskDefinitions(TaskId)
);

-- =============================================
-- Workflow Instance Tables
-- =============================================
CREATE TABLE ProcessStatus (
    StatusCode NVARCHAR(10) NOT NULL PRIMARY KEY,   
    StatusDescription NVARCHAR(255) NOT NULL
);

INSERT INTO ProcessStatus (StatusCode, StatusDescription) VALUES
('NEW', 'Process is new'),
('ACTIVE', 'Process is active'),
('COMPLETED', 'Process has been completed'),
('SUSPENDED', 'Process has been suspended'),
('TERMINATED', 'Process has been terminated');


CREATE TABLE ProcessPriorities (
    PriorityCode NVARCHAR(10) NOT NULL PRIMARY KEY,
    PriorityDescription NVARCHAR(255) NOT NULL
);  

INSERT INTO ProcessPriorities (PriorityCode, PriorityDescription) VALUES
('LOW', 'Low Priority'),
('NORMAL', 'Normal Priority'),
('HIGH', 'High Priority'),
('CRITICAL', 'Critical Priority');

-- Application Workflow Instances
CREATE TABLE ProcessInstances (
    InstanceId UNIQUEIDENTIFIER PRIMARY KEY DEFAULT NEWID(),
    ProcessId UNIQUEIDENTIFIER NOT NULL,
    ApplicationId NVARCHAR(50) NOT NULL, -- External application reference
    Status NVARCHAR(10) NOT NULL DEFAULT 'NEW', -- 'Active', 'Completed', 'Suspended', 'Terminated'
    CurrentTaskId UNIQUEIDENTIFIER,
    StartedDate DATETIME2 NOT NULL DEFAULT GETUTCDATE(),
    StartedBy NVARCHAR(100) NOT NULL,
    CompletedDate DATETIME2,
    CompletedBy NVARCHAR(100),
    Priority NVARCHAR(10) DEFAULT 'NORMAL', -- 'Low', 'Normal', 'High', 'Critical' ProcessPriorities FK
    ContextData NVARCHAR(MAX), -- JSON data for workflow context
    FOREIGN KEY (Priority) REFERENCES ProcessPriorities(PriorityCode),
    FOREIGN KEY (Status) REFERENCES ProcessStatus(StatusCode),
    FOREIGN KEY (ProcessId) REFERENCES ProcessDefinitions(ProcessId),
    FOREIGN KEY (CurrentTaskId) REFERENCES TaskDefinitions(TaskId)
);

-- Stage Status Lookup Table
CREATE TABLE StageStatus (
    StatusCode NVARCHAR(20) NOT NULL PRIMARY KEY,
    StatusDescription NVARCHAR(255) NOT NULL
);

INSERT INTO StageStatus (StatusCode, StatusDescription) VALUES
('NEW', 'Stage is new'),
('IN_PROGRESS', 'Stage is in progress'),
('OVERDUE', 'Stage is overdue'),
('COMPLETED', 'Stage has been completed');

CREATE TABLE StageInstance(
    StageInstanceId UNIQUEIDENTIFIER PRIMARY KEY DEFAULT NEWID(),
    ProcessInstanceId uniqueidentifier NOT NULL,
    LaneId uniqueidentifier NOT NULL,
    Status nvarchar(20) NOT NULL DEFAULT 'NEW',
    StartedDate datetime2(7) NULL,
    CompletedDate datetime2(7) NULL,
    DurationDays  AS (datediff(day,StartedDate,CompletedDate)),
    RetryCount int NULL,
    CompletedCount int NULL,
    TotalCount int NULL,
    CreatedDate datetime2(7) NOT NULL DEFAULT GETUTCDATE(),
    CreatedBy nvarchar(100) NOT NULL,
    ModifiedDate datetime2(7) NULL,
    ModifiedBy nvarchar(100) NULL,
    FOREIGN KEY (ProcessInstanceId) REFERENCES ProcessInstances(InstanceId),
    FOREIGN KEY (LaneId) REFERENCES LaneDefinitions(LaneId),
    FOREIGN KEY (Status) REFERENCES StageStatus(StatusCode)
);


-- Task Instance Execution
CREATE TABLE TaskInstances (
    TaskInstanceId UNIQUEIDENTIFIER PRIMARY KEY DEFAULT NEWID(),
    InstanceId UNIQUEIDENTIFIER NOT NULL, -- ProcessInstance
    TaskId UNIQUEIDENTIFIER NOT NULL, -- TaskDefinition
    Status NVARCHAR(50) NOT NULL DEFAULT 'Pending', -- 'Pending', 'InProgress', 'Completed', 'Failed', 'Skipped'
    AssignedTo NVARCHAR(100),
    StartedDate DATETIME2,
    CompletedDate DATETIME2,
    DurationMinutes AS DATEDIFF(MINUTE, StartedDate, CompletedDate),
    Result NVARCHAR(50), -- 'Success', 'Failed', 'Retry', 'Skip'
    ResultData NVARCHAR(MAX), -- JSON result data
    ErrorMessage NVARCHAR(1000),
    RetryCount INT DEFAULT 0,
    FOREIGN KEY (InstanceId) REFERENCES ProcessInstances(InstanceId),
    FOREIGN KEY (TaskId) REFERENCES TaskDefinitions(TaskId)
);

-- =============================================
-- Validation Framework Tables
-- =============================================

-- Validation Rules
CREATE TABLE ValidationRules (
    ValidationId UNIQUEIDENTIFIER PRIMARY KEY DEFAULT NEWID(),
    ValidationName NVARCHAR(100) NOT NULL,
    Category NVARCHAR(50) NOT NULL, -- 'Company', 'Plant', 'Contacts', 'Products', 'Ingredients', 'Quote', 'Documentation'
    RuleType NVARCHAR(50) NOT NULL, -- 'Required', 'Format', 'Business', 'CrossReference'
    ValidationQuery NVARCHAR(MAX), -- SQL query for validation
    ErrorMessage NVARCHAR(500),
    IsActive BIT NOT NULL DEFAULT 1,
    CreatedDate DATETIME2 NOT NULL DEFAULT GETUTCDATE()
);

-- Validation Results
CREATE TABLE ValidationResults (
    ValidationResultId UNIQUEIDENTIFIER PRIMARY KEY DEFAULT NEWID(),
    InstanceId UNIQUEIDENTIFIER NOT NULL,
    ValidationId UNIQUEIDENTIFIER NOT NULL,
    TaskInstanceId UNIQUEIDENTIFIER,
    IsValid BIT NOT NULL,
    ValidationMessage NVARCHAR(500),
    ValidationDate DATETIME2 NOT NULL DEFAULT GETUTCDATE(),
    ValidatedBy NVARCHAR(100),
    FOREIGN KEY (InstanceId) REFERENCES ProcessInstances(InstanceId),
    FOREIGN KEY (ValidationId) REFERENCES ValidationRules(ValidationId),
    FOREIGN KEY (TaskInstanceId) REFERENCES TaskInstances(TaskInstanceId)
);

-- =============================================
-- Communication Tables
-- =============================================
-- Message Types Lookup Table
CREATE TABLE ProcessMessageTypes (
    MessageTypeCode NVARCHAR(20) NOT NULL PRIMARY KEY,
    MessageTypeDescription NVARCHAR(255) NOT NULL
);

INSERT INTO ProcessMessageTypes (MessageTypeCode, MessageTypeDescription) VALUES
('Standard', 'Standard message'),
('Urgent', 'Urgent message requiring immediate attention'),
('System', 'System-generated message'),
('Notification', 'Notification message');
-- ProcessMessages
CREATE TABLE ProcessMessages (
    MessageId UNIQUEIDENTIFIER PRIMARY KEY DEFAULT NEWID(),
    InstanceId UNIQUEIDENTIFIER NOT NULL,
    FromUser NVARCHAR(100) NOT NULL,
    ToUser NVARCHAR(100),
    ToRole NVARCHAR(50),
    MessageType NVARCHAR(20) DEFAULT 'Standard', -- 'Standard', 'Urgent', 'System', 'Notification'
    Subject NVARCHAR(200),
    MessageBody NVARCHAR(MAX) NOT NULL,
    SentDate DATETIME2 NOT NULL DEFAULT GETUTCDATE(),
    ReadDate DATETIME2,
    IsRead BIT NOT NULL DEFAULT 0,
    FOREIGN KEY (MessageType) REFERENCES ProcessMessageTypes(MessageTypeCode),
    FOREIGN KEY (InstanceId) REFERENCES ProcessInstances(InstanceId)
);

-- Comment Types Lookup Table
CREATE TABLE TaskCommentTypes (
    CommentTypeCode NVARCHAR(10) NOT NULL PRIMARY KEY,
    CommentTypeDescription NVARCHAR(255) NOT NULL
);

INSERT INTO TaskCommentTypes (CommentTypeCode, CommentTypeDescription) VALUES
('Internal', 'Internal comment for staff use only'),
('External', 'External comment visible to clients'),
('System', 'System-generated comment');

-- TaskComments
CREATE TABLE TaskComments (
    CommentId UNIQUEIDENTIFIER PRIMARY KEY DEFAULT NEWID(),
    InstanceId UNIQUEIDENTIFIER NOT NULL,
    TaskInstanceId UNIQUEIDENTIFIER,
    CommentType NVARCHAR(10) DEFAULT 'Internal', -- 'Internal', 'External', 'System'
    CommentText NVARCHAR(MAX) NOT NULL,
    Author NVARCHAR(100) NOT NULL,
    CreatedDate DATETIME2 NOT NULL DEFAULT GETUTCDATE(),
    IsVisible BIT NOT NULL DEFAULT 1,
    FOREIGN KEY (CommentType) REFERENCES TaskCommentTypes(CommentTypeCode),
    FOREIGN KEY (InstanceId) REFERENCES ProcessInstances(InstanceId),
    FOREIGN KEY (TaskInstanceId) REFERENCES TaskInstances(TaskInstanceId)
);

-- =============================================
-- Audit and History Tables
-- =============================================

-- Workflow History
CREATE TABLE WorkflowHistory (
    HistoryId UNIQUEIDENTIFIER PRIMARY KEY DEFAULT NEWID(),
    InstanceId UNIQUEIDENTIFIER NOT NULL,
    TaskInstanceId UNIQUEIDENTIFIER,
    Action NVARCHAR(100) NOT NULL,
    PreviousStatus NVARCHAR(50),
    NewStatus NVARCHAR(50),
    ActionBy NVARCHAR(100) NOT NULL,
    ActionDate DATETIME2 NOT NULL DEFAULT GETUTCDATE(),
    ActionReason NVARCHAR(500),
    Details NVARCHAR(MAX), -- JSON details
    FOREIGN KEY (InstanceId) REFERENCES ProcessInstances(InstanceId),
    FOREIGN KEY (TaskInstanceId) REFERENCES TaskInstances(TaskInstanceId)
);

-- =============================================
-- Indexes for Performance
-- =============================================

CREATE INDEX IX_ProcessInstances_ApplicationId ON ProcessInstances(ApplicationId);
CREATE INDEX IX_ProcessInstances_Status ON ProcessInstances(Status);
CREATE INDEX IX_ProcessInstances_StartedDate ON ProcessInstances(StartedDate);

CREATE INDEX IX_TaskInstances_Status ON TaskInstances(Status);
CREATE INDEX IX_TaskInstances_AssignedTo ON TaskInstances(AssignedTo);
CREATE INDEX IX_TaskInstances_StartedDate ON TaskInstances(StartedDate);

CREATE INDEX IX_ValidationResults_InstanceId ON ValidationResults(InstanceId);
CREATE INDEX IX_ValidationResults_IsValid ON ValidationResults(IsValid);

CREATE INDEX IX_ProcessMessages_ToUser ON ProcessMessages(ToUser);
CREATE INDEX IX_ProcessMessages_IsRead ON ProcessMessages(IsRead);

CREATE INDEX IX_WorkflowHistory_InstanceId ON WorkflowHistory(InstanceId);
CREATE INDEX IX_WorkflowHistory_ActionDate ON WorkflowHistory(ActionDate);

-- =============================================
-- Insert Process Definition and Tasks
-- =============================================
GO
-- Insert the Admin Completion Workflow Process
DECLARE @ProcessId UNIQUEIDENTIFIER = NEWID();
INSERT INTO ProcessDefinitions (ProcessId, ProcessName, ProcessVersion, Description, CreatedBy)
VALUES (@ProcessId, 'Application Workflow', '1.0', 'NCRC Application preprocessing and validation workflow for admins', 'admin');

-- Insert Task Definitions
DECLARE @TaskIds TABLE (TaskName NVARCHAR(100), TaskId UNIQUEIDENTIFIER);

-- Start Event
DECLARE @StartTaskId UNIQUEIDENTIFIER = NEWID();
INSERT INTO @TaskIds VALUES ('Start_Application_Submitted', @StartTaskId);
INSERT INTO TaskDefinitions (TaskId, ProcessId, TaskName, TaskType, TaskCategory, Sequence, AssigneeRole, Description, AutoComplete)
VALUES (@StartTaskId, @ProcessId, 'Start_Application_Submitted', 'Event', 'Start', 1, 'System', 'Application submitted and ready for admin review', 1);

-- Validation Tasks
DECLARE @ValidateCompanyId UNIQUEIDENTIFIER = NEWID();
INSERT INTO @TaskIds VALUES ('Validate_Company_Data', @ValidateCompanyId);
INSERT INTO TaskDefinitions (TaskId, ProcessId, TaskName, TaskType, TaskCategory, Sequence, AssigneeRole, EstimatedDurationMinutes, Description)
VALUES (@ValidateCompanyId, @ProcessId, 'Validate_Company_Data', 'ServiceTask', 'Validation', 2, 'Admin', 5, 'Validate company information and Kashrus DB status');

DECLARE @ValidatePlantId UNIQUEIDENTIFIER = NEWID();
INSERT INTO @TaskIds VALUES ('Validate_Plant_Data', @ValidatePlantId);
INSERT INTO TaskDefinitions (TaskId, ProcessId, TaskName, TaskType, TaskCategory, Sequence, AssigneeRole, EstimatedDurationMinutes, Description)
VALUES (@ValidatePlantId, @ProcessId, 'Validate_Plant_Data', 'ServiceTask', 'Validation', 3, 'Admin', 5, 'Validate plant location and manufacturing details');

DECLARE @ValidateContactsId UNIQUEIDENTIFIER = NEWID();
INSERT INTO @TaskIds VALUES ('Validate_Contacts', @ValidateContactsId);
INSERT INTO TaskDefinitions (TaskId, ProcessId, TaskName, TaskType, TaskCategory, Sequence, AssigneeRole, EstimatedDurationMinutes, Description)
VALUES (@ValidateContactsId, @ProcessId, 'Validate_Contacts', 'ServiceTask', 'Validation', 4, 'Admin', 3, 'Validate contact information and designate primary contact');

DECLARE @ValidateProductsId UNIQUEIDENTIFIER = NEWID();
INSERT INTO @TaskIds VALUES ('Validate_Products', @ValidateProductsId);
INSERT INTO TaskDefinitions (TaskId, ProcessId, TaskName, TaskType, TaskCategory, Sequence, AssigneeRole, EstimatedDurationMinutes, Description)
VALUES (@ValidateProductsId, @ProcessId, 'Validate_Products', 'ServiceTask', 'Validation', 5, 'Admin', 10, 'Validate product specifications and categorization');

DECLARE @ValidateIngredientsId UNIQUEIDENTIFIER = NEWID();
INSERT INTO @TaskIds VALUES ('Validate_Ingredients', @ValidateIngredientsId);
INSERT INTO TaskDefinitions (TaskId, ProcessId, TaskName, TaskType, TaskCategory, Sequence, AssigneeRole, EstimatedDurationMinutes, Description)
VALUES (@ValidateIngredientsId, @ProcessId, 'Validate_Ingredients', 'ServiceTask', 'Validation', 6, 'Admin', 15, 'Validate ingredient certifications and NCRC database entries');

DECLARE @ValidateQuoteId UNIQUEIDENTIFIER = NEWID();
INSERT INTO @TaskIds VALUES ('Validate_Quote', @ValidateQuoteId);
INSERT INTO TaskDefinitions (TaskId, ProcessId, TaskName, TaskType, TaskCategory, Sequence, AssigneeRole, EstimatedDurationMinutes, Description)
VALUES (@ValidateQuoteId, @ProcessId, 'Validate_Quote', 'UserTask', 'Validation', 7, 'Admin', 5, 'Verify quote information and acceptance status');

DECLARE @ValidateDocumentationId UNIQUEIDENTIFIER = NEWID();
INSERT INTO @TaskIds VALUES ('Validate_Documentation', @ValidateDocumentationId);
INSERT INTO TaskDefinitions (TaskId, ProcessId, TaskName, TaskType, TaskCategory, Sequence, AssigneeRole, EstimatedDurationMinutes, Description)
VALUES (@ValidateDocumentationId, @ProcessId, 'Validate_Documentation', 'ServiceTask', 'Validation', 8, 'Admin', 5, 'Validate all required documents are uploaded and processed');

-- Decision Gateway
DECLARE @AllValidationsPassedId UNIQUEIDENTIFIER = NEWID();
INSERT INTO @TaskIds VALUES ('All_Validations_Passed', @AllValidationsPassedId);
INSERT INTO TaskDefinitions (TaskId, ProcessId, TaskName, TaskType, TaskCategory, Sequence, AssigneeRole, Description, AutoComplete)
VALUES (@AllValidationsPassedId, @ProcessId, 'All_Validations_Passed', 'Gateway', 'Decision', 9, 'System', 'Check if all validation tasks have passed', 1);

-- Admin Action Tasks
DECLARE @MarkCompleteId UNIQUEIDENTIFIER = NEWID();
INSERT INTO @TaskIds VALUES ('Mark_Application_Complete', @MarkCompleteId);
INSERT INTO TaskDefinitions (TaskId, ProcessId, TaskName, TaskType, TaskCategory, Sequence, AssigneeRole, EstimatedDurationMinutes, Description)
VALUES (@MarkCompleteId, @ProcessId, 'Mark_Application_Complete', 'UserTask', 'Action', 10, 'Admin', 2, 'Admin marks application as complete and ready for dispatch');

DECLARE @AdminActionGatewayId UNIQUEIDENTIFIER = NEWID();
INSERT INTO @TaskIds VALUES ('Admin_Action_Gateway', @AdminActionGatewayId);
INSERT INTO TaskDefinitions (TaskId, ProcessId, TaskName, TaskType, TaskCategory, Sequence, AssigneeRole, Description, AutoComplete)
VALUES (@AdminActionGatewayId, @ProcessId, 'Admin_Action_Gateway', 'Gateway', 'Decision', 11, 'Admin', 'Admin chooses next action: Dispatch, Undo, Comment, or Message', 0);

DECLARE @DispatchToQueueId UNIQUEIDENTIFIER = NEWID();
INSERT INTO @TaskIds VALUES ('Dispatch_To_Queue', @DispatchToQueueId);
INSERT INTO TaskDefinitions (TaskId, ProcessId, TaskName, TaskType, TaskCategory, Sequence, AssigneeRole, EstimatedDurationMinutes, Description)
VALUES (@DispatchToQueueId, @ProcessId, 'Dispatch_To_Queue', 'ServiceTask', 'Action', 12, 'Admin', 1, 'Send application to dispatcher review queue');

DECLARE @UndoCompletionId UNIQUEIDENTIFIER = NEWID();
INSERT INTO @TaskIds VALUES ('Undo_Completion', @UndoCompletionId);
INSERT INTO TaskDefinitions (TaskId, ProcessId, TaskName, TaskType, TaskCategory, Sequence, AssigneeRole, EstimatedDurationMinutes, Description)
VALUES (@UndoCompletionId, @ProcessId, 'Undo_Completion', 'UserTask', 'Action', 13, 'Admin', 1, 'Return application to incomplete status for further review');

DECLARE @AddCommentId UNIQUEIDENTIFIER = NEWID();
INSERT INTO @TaskIds VALUES ('Add_Internal_Comment', @AddCommentId);
INSERT INTO TaskDefinitions (TaskId, ProcessId, TaskName, TaskType, TaskCategory, Sequence, AssigneeRole, EstimatedDurationMinutes, Description)
VALUES (@AddCommentId, @ProcessId, 'Add_Internal_Comment', 'UserTask', 'Notification', 14, 'Admin', 3, 'Add internal comment for audit trail');

DECLARE @SendMessageId UNIQUEIDENTIFIER = NEWID();
INSERT INTO @TaskIds VALUES ('Send_Message_To_Dispatcher', @SendMessageId);
INSERT INTO TaskDefinitions (TaskId, ProcessId, TaskName, TaskType, TaskCategory, Sequence, AssigneeRole, EstimatedDurationMinutes, Description)
VALUES (@SendMessageId, @ProcessId, 'Send_Message_To_Dispatcher', 'UserTask', 'Notification', 15, 'Admin', 5, 'Send message to dispatcher about application status');

-- End States
DECLARE @ApplicationDispatchedId UNIQUEIDENTIFIER = NEWID();
INSERT INTO @TaskIds VALUES ('Application_Dispatched', @ApplicationDispatchedId);
INSERT INTO TaskDefinitions (TaskId, ProcessId, TaskName, TaskType, TaskCategory, Sequence, AssigneeRole, Description, AutoComplete)
VALUES (@ApplicationDispatchedId, @ProcessId, 'Application_Dispatched', 'Event', 'End', 16, 'System', 'Application successfully dispatched to review queue', 1);

DECLARE @UnderReviewId UNIQUEIDENTIFIER = NEWID();
INSERT INTO @TaskIds VALUES ('Under_Review', @UnderReviewId);
INSERT INTO TaskDefinitions (TaskId, ProcessId, TaskName, TaskType, TaskCategory, Sequence, AssigneeRole, Description, AutoComplete)
VALUES (@UnderReviewId, @ProcessId, 'Under_Review', 'Event', 'End', 17, 'Dispatcher', 'Application is under review by dispatcher', 1);
GO
-- =============================================
-- Insert Validation Rules
-- =============================================

INSERT INTO ValidationRules (ValidationName, Category, RuleType, ValidationQuery, ErrorMessage)
VALUES 
('Company_Name_Required', 'Company', 'Required', 'SELECT CASE WHEN ISNULL(CompanyName, '''') = '''' THEN 0 ELSE 1 END', 'Company name is required'),
('Company_Address_Required', 'Company', 'Required', 'SELECT CASE WHEN ISNULL(Address, '''') = '''' THEN 0 ELSE 1 END', 'Company address is required'),
('Kashrus_ID_Generated', 'Company', 'Business', 'SELECT CASE WHEN ISNULL(KashrusCompanyId, '''') = '''' THEN 0 ELSE 1 END', 'Kashrus company ID must be generated'),

('Plant_Location_Required', 'Plant', 'Required', 'SELECT CASE WHEN ISNULL(PlantAddress, '''') = '''' THEN 0 ELSE 1 END', 'Plant location is required'),
('Plant_Contact_Required', 'Plant', 'Required', 'SELECT CASE WHEN ISNULL(PlantContactName, '''') = '''' THEN 0 ELSE 1 END', 'Plant contact is required'),
('Plant_ID_Generated', 'Plant', 'Business', 'SELECT CASE WHEN ISNULL(PlantId, '''') = '''' THEN 0 ELSE 1 END', 'Plant ID must be generated'),

('Primary_Contact_Designated', 'Contacts', 'Business', 'SELECT CASE WHEN EXISTS(SELECT 1 FROM Contacts WHERE IsPrimary = 1) THEN 1 ELSE 0 END', 'Primary contact must be designated'),
('Contact_Email_Valid', 'Contacts', 'Format', 'SELECT CASE WHEN Email LIKE ''%@%.%'' THEN 1 ELSE 0 END', 'Valid email address required'),

('Products_Exist', 'Products', 'Required', 'SELECT CASE WHEN COUNT(*) > 0 THEN 1 ELSE 0 END FROM Products', 'At least one product must be specified'),
('Product_Names_Required', 'Products', 'Required', 'SELECT CASE WHEN ISNULL(ProductName, '''') = '''' THEN 0 ELSE 1 END', 'Product names are required'),

('Ingredients_Exist', 'Ingredients', 'Required', 'SELECT CASE WHEN COUNT(*) > 0 THEN 1 ELSE 0 END FROM Ingredients', 'At least one ingredient must be specified'),
('Ingredient_Certifications_Valid', 'Ingredients', 'Business', 'SELECT CASE WHEN ISNULL(CertificationAgency, '''') = '''' THEN 0 ELSE 1 END', 'Ingredient certifications must be specified'),
('NCRC_IDs_Generated', 'Ingredients', 'Business', 'SELECT CASE WHEN ISNULL(NCRCId, '''') = '''' THEN 0 ELSE 1 END', 'NCRC ingredient IDs must be generated'),

('Quote_Exists', 'Quote', 'Required', 'SELECT CASE WHEN ISNULL(QuoteNumber, '''') = '''' THEN 0 ELSE 1 END', 'Quote must be provided'),
('Quote_Accepted', 'Quote', 'Business', 'SELECT CASE WHEN QuoteStatus = ''Accepted'' THEN 1 ELSE 0 END', 'Quote must be accepted before completion'),

('Required_Documents_Uploaded', 'Documentation', 'Required', 'SELECT CASE WHEN COUNT(*) >= 2 THEN 1 ELSE 0 END FROM Documents WHERE IsRequired = 1', 'All required documents must be uploaded'),
('Documents_Processed', 'Documentation', 'Business', 'SELECT CASE WHEN AllDocumentsProcessed = 1 THEN 1 ELSE 0 END', 'All documents must be processed successfully');

GO

-- =============================================
-- Sample Views for Workflow Monitoring
-- =============================================

-- View: Active Workflow Instances
CREATE VIEW vw_ActiveWorkflows AS
SELECT 
    pi.InstanceId,
    pi.ApplicationId,
    pd.ProcessName,
    pi.Status,
    td.TaskName AS CurrentTask,
    pi.StartedDate,
    pi.StartedBy,
    pi.Priority,
    DATEDIFF(HOUR, pi.StartedDate, GETUTCDATE()) AS HoursActive
FROM ProcessInstances pi
INNER JOIN ProcessDefinitions pd ON pi.ProcessId = pd.ProcessId
LEFT JOIN TaskDefinitions td ON pi.CurrentTaskId = td.TaskId
WHERE pi.Status = 'Active';
GO
-- View: Validation Status Summary
CREATE VIEW vw_ValidationStatus AS
SELECT 
    pi.InstanceId,
    pi.ApplicationId,
    COUNT(vr.ValidationId) AS TotalValidations,
    SUM(CASE WHEN vres.IsValid = 1 THEN 1 ELSE 0 END) AS PassedValidations,
    SUM(CASE WHEN vres.IsValid = 0 THEN 1 ELSE 0 END) AS FailedValidations,
    CASE 
        WHEN COUNT(vr.ValidationId) = SUM(CASE WHEN vres.IsValid = 1 THEN 1 ELSE 0 END) THEN 'All Passed'
        WHEN SUM(CASE WHEN vres.IsValid = 0 THEN 1 ELSE 0 END) > 0 THEN 'Has Failures'
        ELSE 'In Progress'
    END AS ValidationStatus
FROM ProcessInstances pi
CROSS JOIN ValidationRules vr
LEFT JOIN ValidationResults vres ON pi.InstanceId = vres.InstanceId AND vr.ValidationId = vres.ValidationId
WHERE vr.IsActive = 1
GROUP BY pi.InstanceId, pi.ApplicationId;
GO
-- View: Task Performance Metrics
CREATE VIEW vw_TaskPerformance AS
SELECT 
    td.TaskName,
    td.TaskType,
    td.TaskCategory,
    COUNT(ti.TaskInstanceId) AS TotalExecutions,
    AVG(CAST(ti.DurationMinutes AS FLOAT)) AS AvgDurationMinutes,
    td.EstimatedDurationMinutes,
    SUM(CASE WHEN ti.Status = 'Completed' THEN 1 ELSE 0 END) AS CompletedTasks,
    SUM(CASE WHEN ti.Status = 'Failed' THEN 1 ELSE 0 END) AS FailedTasks,
    CAST(SUM(CASE WHEN ti.Status = 'Completed' THEN 1 ELSE 0 END) AS FLOAT) / COUNT(ti.TaskInstanceId) * 100 AS SuccessRate
FROM TaskDefinitions td
LEFT JOIN TaskInstances ti ON td.TaskId = ti.TaskId
GROUP BY td.TaskId, td.TaskName, td.TaskType, td.TaskCategory, td.EstimatedDurationMinutes;

GO

-- =============================================
-- Stored Procedures for Workflow Management
-- =============================================

-- Procedure: Start New Workflow Instance
CREATE PROCEDURE sp_StartWorkflowInstance
    @ProcessName NVARCHAR(100),
    @ApplicationId NVARCHAR(50),
    @StartedBy NVARCHAR(100),
    @Priority NVARCHAR(20) = 'Normal'
AS
BEGIN
    SET NOCOUNT ON;
    
    DECLARE @ProcessId UNIQUEIDENTIFIER;
    DECLARE @InstanceId UNIQUEIDENTIFIER = NEWID();
    DECLARE @StartTaskId UNIQUEIDENTIFIER;
    
    -- Get Process ID
    SELECT @ProcessId = ProcessId 
    FROM ProcessDefinitions 
    WHERE ProcessName = @ProcessName AND IsActive = 1;
    
    IF @ProcessId IS NULL
    BEGIN
        RAISERROR('Process definition not found: %s', 16, 1, @ProcessName);
        RETURN;
    END
    
    -- Get Start Task
    SELECT TOP 1 @StartTaskId = TaskId 
    FROM TaskDefinitions 
    WHERE ProcessId = @ProcessId AND TaskType = 'Event' AND TaskCategory = 'Start'
    ORDER BY Sequence;
    
    -- Create Process Instance
    INSERT INTO ProcessInstances (InstanceId, ProcessId, ApplicationId, CurrentTaskId, StartedBy, Priority)
    VALUES (@InstanceId, @ProcessId, @ApplicationId, @StartTaskId, @StartedBy, @Priority);
    
    -- Log History
    INSERT INTO WorkflowHistory (InstanceId, Action, NewStatus, ActionBy, ActionReason)
    VALUES (@InstanceId, 'Workflow Started', 'Active', @StartedBy, 'New application submitted for processing');
    
    SELECT @InstanceId AS InstanceId;
END;
GO
-- Procedure: Complete Task
CREATE PROCEDURE sp_CompleteTask
    @InstanceId UNIQUEIDENTIFIER,
    @TaskName NVARCHAR(100),
    @CompletedBy NVARCHAR(100),
    @Result NVARCHAR(50) = 'Success',
    @ResultData NVARCHAR(MAX) = NULL
AS
BEGIN
    SET NOCOUNT ON;
    
    DECLARE @TaskInstanceId UNIQUEIDENTIFIER;
    DECLARE @TaskId UNIQUEIDENTIFIER;
    DECLARE @NextTaskId UNIQUEIDENTIFIER;
    
    -- Get current task instance
    SELECT @TaskInstanceId = ti.TaskInstanceId, @TaskId = ti.TaskId
    FROM TaskInstances ti
    INNER JOIN TaskDefinitions td ON ti.TaskId = td.TaskId
    WHERE ti.InstanceId = @InstanceId 
    AND td.TaskName = @TaskName 
    AND ti.Status IN ('Pending', 'InProgress');
    
    IF @TaskInstanceId IS NULL
    BEGIN
        RAISERROR('Task instance not found or already completed: %s', 16, 1, @TaskName);
        RETURN;
    END
    
    -- Complete the task
    UPDATE TaskInstances 
    SET Status = 'Completed',
        CompletedDate = GETUTCDATE(),
        Result = @Result,
        ResultData = @ResultData
    WHERE TaskInstanceId = @TaskInstanceId;
    
    -- Get next task based on flow
    SELECT TOP 1 @NextTaskId = tf.ToTaskId
    FROM TaskFlow tf
    WHERE tf.FromTaskId = @TaskId
    AND (tf.Condition IS NULL OR tf.Condition = @Result OR tf.IsDefault = 1)
    ORDER BY tf.IsDefault;
    
    -- Update process instance current task
    IF @NextTaskId IS NOT NULL
    BEGIN
        UPDATE ProcessInstances 
        SET CurrentTaskId = @NextTaskId
        WHERE InstanceId = @InstanceId;
        
        -- Create next task instance if not exists
        IF NOT EXISTS (SELECT 1 FROM TaskInstances WHERE InstanceId = @InstanceId AND TaskId = @NextTaskId)
        BEGIN
            INSERT INTO TaskInstances (InstanceId, TaskId, Status, StartedDate)
            VALUES (@InstanceId, @NextTaskId, 'Pending', GETUTCDATE());
        END
    END
    
    -- Log history
    INSERT INTO WorkflowHistory (InstanceId, TaskInstanceId, Action, NewStatus, ActionBy, Details)
    VALUES (@InstanceId, @TaskInstanceId, 'Task Completed: ' + @TaskName, 'Completed', @CompletedBy, @ResultData);
END;
GO
-- Procedure: Run Validation Check
CREATE PROCEDURE sp_RunValidationCheck
    @InstanceId UNIQUEIDENTIFIER,
    @ValidationCategory NVARCHAR(50) = NULL,
    @ValidatedBy NVARCHAR(100)
AS
BEGIN
    SET NOCOUNT ON;
    
    DECLARE @ValidationId UNIQUEIDENTIFIER;
    DECLARE @ValidationName NVARCHAR(100);
    DECLARE @ValidationQuery NVARCHAR(MAX);
    DECLARE @ErrorMessage NVARCHAR(500);
    DECLARE @IsValid BIT;
    DECLARE @ValidationMessage NVARCHAR(500);
    DECLARE @SQL NVARCHAR(MAX);
    
    -- Cursor for validation rules
    DECLARE validation_cursor CURSOR FOR
    SELECT ValidationId, ValidationName, ValidationQuery, ErrorMessage
    FROM ValidationRules
    WHERE IsActive = 1 
    AND (@ValidationCategory IS NULL OR Category = @ValidationCategory);
    
    OPEN validation_cursor;
    FETCH NEXT FROM validation_cursor INTO @ValidationId, @ValidationName, @ValidationQuery, @ErrorMessage;
    
    WHILE @@FETCH_STATUS = 0
    BEGIN
        -- Execute validation query
        SET @SQL = 'SELECT @IsValid = (' + @ValidationQuery + ')';
        
        BEGIN TRY
            EXEC sp_executesql @SQL, N'@IsValid BIT OUTPUT', @IsValid OUTPUT;
            SET @ValidationMessage = CASE WHEN @IsValid = 1 THEN 'Validation passed' ELSE @ErrorMessage END;
        END TRY
        BEGIN CATCH
            SET @IsValid = 0;
            SET @ValidationMessage = 'Validation error: ' + ERROR_MESSAGE();
        END CATCH
        
        -- Insert or update validation result
        MERGE ValidationResults AS target
        USING (SELECT @InstanceId AS InstanceId, @ValidationId AS ValidationId) AS source
        ON target.InstanceId = source.InstanceId AND target.ValidationId = source.ValidationId
        WHEN MATCHED THEN
            UPDATE SET IsValid = @IsValid, 
            ValidationMessage = @ValidationMessage,
            ValidationDate = GETUTCDATE(),
            ValidatedBy = @ValidatedBy
        WHEN NOT MATCHED THEN
            INSERT (InstanceId, ValidationId, IsValid, ValidationMessage, ValidatedBy)
            VALUES (@InstanceId, @ValidationId, @IsValid, @ValidationMessage, @ValidatedBy);
        
        FETCH NEXT FROM validation_cursor INTO @ValidationId, @ValidationName, @ValidationQuery, @ErrorMessage;
    END
    
    CLOSE validation_cursor;
    DEALLOCATE validation_cursor;
    
    -- Return validation summary
    SELECT 
        vr.Category,
        COUNT(*) AS TotalChecks,
        SUM(CASE WHEN vres.IsValid = 1 THEN 1 ELSE 0 END) AS PassedChecks,
        SUM(CASE WHEN vres.IsValid = 0 THEN 1 ELSE 0 END) AS FailedChecks
    FROM ValidationRules vr
    INNER JOIN ValidationResults vres ON vr.ValidationId = vres.ValidationId
    WHERE vres.InstanceId = @InstanceId
    AND (@ValidationCategory IS NULL OR vr.Category = @ValidationCategory)
    GROUP BY vr.Category;
END;
GO
-- Procedure: Add Message
CREATE PROCEDURE sp_AddMessage
    @InstanceId UNIQUEIDENTIFIER,
    @FromUser NVARCHAR(100),
    @ToUser NVARCHAR(100) = NULL,
    @ToRole NVARCHAR(50) = NULL,
    @MessageType NVARCHAR(50) = 'Standard',
    @Subject NVARCHAR(200) = NULL,
    @MessageBody NVARCHAR(MAX)
AS
BEGIN
    SET NOCOUNT ON;
    
    DECLARE @MessageId UNIQUEIDENTIFIER = NEWID();
    
    INSERT INTO ProcessMessages (MessageId, InstanceId, FromUser, ToUser, ToRole, MessageType, Subject, MessageBody)
    VALUES (@MessageId, @InstanceId, @FromUser, @ToUser, @ToRole, @MessageType, @Subject, @MessageBody);
    
    -- Log history
    INSERT INTO WorkflowHistory (InstanceId, Action, ActionBy, Details)
    VALUES (@InstanceId, 'Message Sent', @FromUser, 'To: ' + ISNULL(@ToUser, @ToRole) + ' - ' + ISNULL(@Subject, 'No Subject'));
    
    SELECT @MessageId AS MessageId;
END;

GO
-- Procedure: Add Comment
CREATE PROCEDURE sp_AddComment
    @InstanceId UNIQUEIDENTIFIER,
    @TaskInstanceId UNIQUEIDENTIFIER = NULL,
    @CommentType NVARCHAR(50) = 'Internal',
    @CommentText NVARCHAR(MAX),
    @Author NVARCHAR(100)
AS
BEGIN
    SET NOCOUNT ON;
    
    DECLARE @CommentId UNIQUEIDENTIFIER = NEWID();
    
    INSERT INTO TaskComments (CommentId, InstanceId, TaskInstanceId, CommentType, CommentText, Author)
    VALUES (@CommentId, @InstanceId, @TaskInstanceId, @CommentType, @CommentText, @Author);
    
    -- Log history
    INSERT INTO WorkflowHistory (InstanceId, TaskInstanceId, Action, ActionBy, Details)
    VALUES (@InstanceId, @TaskInstanceId, 'Comment Added', @Author, LEFT(@CommentText, 200));
    
    SELECT @CommentId AS CommentId;
END;

GO
-- Procedure: Get Workflow Status
CREATE PROCEDURE sp_GetWorkflowStatus
    @InstanceId UNIQUEIDENTIFIER
AS
BEGIN
    SET NOCOUNT ON;
    
    -- Process Instance Info
    SELECT 
        pi.InstanceId,
        pi.ApplicationId,
        pi.KashrusCompanyId,
        pd.ProcessName,
        pi.Status,
        td.TaskName AS CurrentTask,
        td.TaskType AS CurrentTaskType,
        td.AssigneeRole AS CurrentAssignee,
        pi.StartedDate,
        pi.StartedBy,
        pi.Priority,
        DATEDIFF(HOUR, pi.StartedDate, GETUTCDATE()) AS HoursActive
    FROM ProcessInstances pi
    INNER JOIN ProcessDefinitions pd ON pi.ProcessId = pd.ProcessId
    LEFT JOIN TaskDefinitions td ON pi.CurrentTaskId = td.TaskId
    WHERE pi.InstanceId = @InstanceId;
    
    -- Validation Status
    SELECT 
        vr.Category,
        vr.ValidationName,
        vres.IsValid,
        vres.ValidationMessage,
        vres.ValidationDate,
        vres.ValidatedBy
    FROM ValidationRules vr
    LEFT JOIN ValidationResults vres ON vr.ValidationId = vres.ValidationId AND vres.InstanceId = @InstanceId
    WHERE vr.IsActive = 1
    ORDER BY vr.Category, vr.ValidationName;
    
    -- Task History
    SELECT 
        td.TaskName,
        ti.Status,
        ti.StartedDate,
        ti.CompletedDate,
        ti.DurationMinutes,
        ti.Result,
        ti.AssignedTo
    FROM TaskInstances ti
    INNER JOIN TaskDefinitions td ON ti.TaskId = td.TaskId
    WHERE ti.InstanceId = @InstanceId
    ORDER BY ti.StartedDate;
    
    -- Recent ProcessMessages
    SELECT TOP 10
        m.FromUser,
        m.ToUser,
        m.ToRole,
        m.MessageType,
        m.Subject,
        m.MessageBody,
        m.SentDate,
        m.IsRead
    FROM ProcessMessages m
    WHERE m.InstanceId = @InstanceId
    ORDER BY m.SentDate DESC;
    
    -- Recent TaskComments
    SELECT TOP 10
        c.CommentType,
        c.CommentText,
        c.Author,
        c.CreatedDate,
        td.TaskName AS RelatedTask
    FROM TaskComments c
    LEFT JOIN TaskInstances ti ON c.TaskInstanceId = ti.TaskInstanceId
    LEFT JOIN TaskDefinitions td ON ti.TaskId = td.TaskId
    WHERE c.InstanceId = @InstanceId AND c.IsVisible = 1
    ORDER BY c.CreatedDate DESC;
END;

GO
-- =============================================
-- Sample Data Insertion
-- =============================================

-- Create a sample workflow instance
DECLARE @SampleInstanceId UNIQUEIDENTIFIER;
EXEC sp_StartWorkflowInstance 
    @ProcessName = 'Admin Completion Workflow',
    @ApplicationId = 'APP-2025-0717-001',
    @StartedBy = 'J. Mitchell',
    @Priority = 'Normal';
GO
-- Insert some sample validation results
DECLARE @SampleProcessInstanceId UNIQUEIDENTIFIER;
SELECT TOP 1 @SampleProcessInstanceId = InstanceId 
FROM ProcessInstances 
WHERE ApplicationId = 'APP-2025-0717-001';
GO
-- Sample validation execution
EXEC sp_RunValidationCheck 
    @InstanceId = @SampleProcessInstanceId,
    @ValidatedBy = 'System';
GO
-- Sample message
EXEC sp_AddMessage
    @InstanceId = @SampleProcessInstanceId,
    @FromUser = 'J. Mitchell',
    @ToRole = 'Dispatcher',
    @Subject = 'Application Ready for Review',
    @MessageBody = 'Application ready for initial review. All documentation complete.';
GO
-- Sample comment
EXEC sp_AddComment
    @InstanceId = @SampleProcessInstanceId,
    @CommentType = 'Internal',
    @CommentText = 'Verified all ingredient certifications with suppliers. Coconut oil documentation updated.',
    @Author = 'J. Mitchell';

GO
-- =============================================
-- Function: Check All Validations Passed
-- =============================================

CREATE FUNCTION fn_AllValidationsPassed(@InstanceId UNIQUEIDENTIFIER)
RETURNS BIT
AS
BEGIN
    DECLARE @Result BIT = 0;
    
    IF NOT EXISTS (
        SELECT 1 
        FROM ValidationRules vr
        LEFT JOIN ValidationResults vres ON vr.ValidationId = vres.ValidationId AND vres.InstanceId = @InstanceId
        WHERE vr.IsActive = 1 
        AND (vres.IsValid IS NULL OR vres.IsValid = 0)
    )
    BEGIN
        SET @Result = 1;
    END
    
    RETURN @Result;
END;

GO
-- =============================================
-- Trigger: Auto-advance workflow on task completion
-- =============================================

CREATE TRIGGER tr_TaskCompletion_AutoAdvance
ON TaskInstances
AFTER UPDATE
AS
BEGIN
    SET NOCOUNT ON;
    
    -- Only process when status changes to Completed
    IF UPDATE(Status)
    BEGIN
        DECLARE @InstanceId UNIQUEIDENTIFIER;
        DECLARE @TaskId UNIQUEIDENTIFIER;
        DECLARE @TaskName NVARCHAR(100);
        DECLARE @NextTaskId UNIQUEIDENTIFIER;
        
        -- Get completed tasks
        SELECT 
            i.InstanceId,
            i.TaskId,
            td.TaskName
        FROM inserted i
        INNER JOIN TaskDefinitions td ON i.TaskId = td.TaskId
        WHERE i.Status = 'Completed'
        AND NOT EXISTS (SELECT 1 FROM deleted d WHERE d.TaskInstanceId = i.TaskInstanceId AND d.Status = 'Completed');
        
        DECLARE task_cursor CURSOR FOR
        SELECT InstanceId, TaskId, TaskName FROM inserted 
        WHERE Status = 'Completed';
        
        OPEN task_cursor;
        FETCH NEXT FROM task_cursor INTO @InstanceId, @TaskId, @TaskName;
        
        WHILE @@FETCH_STATUS = 0
        BEGIN
            -- For validation tasks, check if all validations in category passed
            IF @TaskName LIKE 'Validate_%'
            BEGIN
                DECLARE @Category NVARCHAR(50) = REPLACE(REPLACE(@TaskName, 'Validate_', ''), '_Data', '');
                
                -- Run validation check for this category
                EXEC sp_RunValidationCheck 
                    @InstanceId = @InstanceId,
                    @ValidationCategory = @Category,
                    @ValidatedBy = 'System';
            END
            
            -- Check for auto-advance to next task
            SELECT TOP 1 @NextTaskId = tf.ToTaskId
            FROM TaskFlow tf
            INNER JOIN TaskDefinitions td ON tf.ToTaskId = td.TaskId
            WHERE tf.FromTaskId = @TaskId
            AND td.AutoComplete = 1;
            
            IF @NextTaskId IS NOT NULL
            BEGIN
                -- Auto-complete next task if it's a system task
                INSERT INTO TaskInstances (InstanceId, TaskId, Status, StartedDate, CompletedDate, Result)
                VALUES (@InstanceId, @NextTaskId, 'Completed', GETUTCDATE(), GETUTCDATE(), 'Success');
            END
            
            FETCH NEXT FROM task_cursor INTO @InstanceId, @TaskId, @TaskName;
        END
        
        CLOSE task_cursor;
        DEALLOCATE task_cursor;
    END
END;

GO
-- =============================================
-- Performance and Monitoring Views
-- =============================================

-- View: Workflow Dashboard
CREATE VIEW vw_WorkflowDashboard AS
SELECT 
    'Total Active Workflows' AS Metric,
    COUNT(*) AS Value,
    'Count' AS Unit
FROM ProcessInstances 
WHERE Status = 'Active'

UNION ALL

SELECT 
    'Average Hours to Complete',
    AVG(CAST(DATEDIFF(HOUR, StartedDate, CompletedDate) AS FLOAT)),
    'Hours'
FROM ProcessInstances 
WHERE Status = 'Completed' AND CompletedDate IS NOT NULL

UNION ALL

SELECT 
    'Pending Admin Tasks',
    COUNT(*),
    'Count'
FROM TaskInstances ti
INNER JOIN TaskDefinitions td ON ti.TaskId = td.TaskId
WHERE ti.Status = 'Pending' AND td.AssigneeRole = 'Admin'

UNION ALL

SELECT 
    'Failed Validations',
    COUNT(*),
    'Count'
FROM ValidationResults 
WHERE IsValid = 0 AND ValidationDate >= DATEADD(DAY, -7, GETUTCDATE());

GO
-- View: Bottleneck Analysis
CREATE VIEW vw_BottleneckAnalysis AS
SELECT 
    td.TaskName,
    td.AssigneeRole,
    COUNT(ti.TaskInstanceId) AS PendingTasks,
    AVG(CAST(DATEDIFF(HOUR, ti.StartedDate, GETUTCDATE()) AS FLOAT)) AS AvgHoursPending,
    td.EstimatedDurationMinutes / 60.0 AS EstimatedHours
FROM TaskInstances ti
INNER JOIN TaskDefinitions td ON ti.TaskId = td.TaskId
WHERE ti.Status = 'Pending'
GROUP BY td.TaskName, td.AssigneeRole, td.EstimatedDurationMinutes
HAVING COUNT(ti.TaskInstanceId) > 0
ORDER BY PendingTasks DESC, AvgHoursPending DESC;

GO
-- =============================================
-- Cleanup and Maintenance Procedures
-- =============================================

-- Procedure: Archive Completed Workflows
CREATE PROCEDURE sp_ArchiveCompletedWorkflows
    @DaysOld INT = 90
AS
BEGIN
    SET NOCOUNT ON;
    
    DECLARE @CutoffDate DATETIME2 = DATEADD(DAY, -@DaysOld, GETUTCDATE());
    DECLARE @ArchivedCount INT = 0;
    
    -- Archive completed workflows older than specified days
    UPDATE ProcessInstances 
    SET Status = 'Archived'
    WHERE Status = 'Completed' 
    AND CompletedDate < @CutoffDate;
    
    SET @ArchivedCount = @@ROWCOUNT;
    
    SELECT @ArchivedCount AS ArchivedWorkflows;
END;
GO
PRINT 'Admin Completion Workflow DDL and stored procedures created successfully!';
PRINT 'Database schema includes:';
PRINT '- Process and Task Definitions';
PRINT '- Workflow Instance Management';
PRINT '- Validation Framework';
PRINT '- Communication System';
PRINT '- Audit and History Tracking';
PRINT '- Performance Monitoring Views';
PRINT '- Sample data and test procedures';
PRINT '';
PRINT 'Key stored procedures:';
PRINT '- sp_StartWorkflowInstance';
PRINT '- sp_CompleteTask';
PRINT '- sp_RunValidationCheck';
PRINT '- sp_GetWorkflowStatus';
PRINT '- sp_AddMessage';
PRINT '- sp_AddComment';