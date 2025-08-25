ae3bb04f-359e-482c-8fa2-02d739d68bdb	X	Application_Dispatched	Event	End
32724850-f16d-4094-9bf4-3c5a95278c95	X	Dispatch_To_Queue	ServiceTask	Action
d4e8c720-1aaa-48f5-9772-463415edf52d	X	Start_Application_Submitted	Event	Start
12b8adee-4187-4317-8f09-49b7ffb7a7ac	X	Validate_Plant_Data	ServiceTask	Validation
483cbd86-29e8-49e5-be74-4a7bb57e9837	X	Validate_Ingredients	ServiceTask	Validation
c73a3866-856d-4361-8fb5-718c291951c7	X	Validate_Contacts	ServiceTask	Validation
1ab297cd-53b6-463d-a1a0-8b2f106c82c9	X	Under_Review	Event	End
ee641fbf-b645-4e82-8691-8e0bf247ccb9	X	All_Validations_Passed	Gateway	Decision
544e58bb-d694-49f6-acb5-a30f00b58702	X	Undo_Completion	UserTask	Action
372c5f9a-9e06-4468-b602-ae4b94dd4470	X	Send_Message_To_Dispatcher	UserTask	Notification
b46e2dfb-9d47-4d16-866c-b1500eeb26f0	X	Validate_Products	ServiceTask	Validation
70911d8f-8eff-4271-9d6e-bbb29b8d494b	X	Validate_Company_Data	ServiceTask	Validation
95b9f6b1-f6ce-4dd6-a6c2-cd6e5284c092	X	Admin_Action_Gateway	Gateway	Decision
2c5bc0a8-f93c-4118-939d-cdfb004a01e5	X	Add_Internal_Comment	UserTask	Notification
2f54c4e6-324b-4f2e-a0ba-d546864063da	X	Validate_Quote	UserTask	Validation
ea063bee-c825-4a5b-b9ae-f326fa74bb28	X	Validate_Documentation	ServiceTask	Validation


INSERT INTO [dbo].[TaskFlow]
           ([FlowId]
           ,[FromTaskId]
           ,[ToTaskId]
           ,[Condition]
    )
     VALUES
    (NEWID()
    ,'ee641fbf-b645-4e82-8691-8e0bf247ccb9'
    ,'ae3bb04f-359e-482c-8fa2-02d739d68bdb'
    ,'Application_Dispatched - End'
    ),(NEWID()
    ,'ee641fbf-b645-4e82-8691-8e0bf247ccb9'
    ,'32724850-f16d-4094-9bf4-3c5a95278c95'
    ,'Dispatch_To_Queue'
    ),(NEWID()
    ,'d4e8c720-1aaa-48f5-9772-463415edf52d'
    ,'12b8adee-4187-4317-8f09-49b7ffb7a7ac'
    ,'Start_Application_Submitted'
    ),(NEWID()
    ,'d4e8c720-1aaa-48f5-9772-463415edf52d'
    ,'483cbd86-29e8-49e5-be74-4a7bb57e9837'
    ,'Start_Application_Submitted'
    ),(NEWID()
    ,'d4e8c720-1aaa-48f5-9772-463415edf52d'
    ,'c73a3866-856d-4361-8fb5-718c291951c7'
    ,'Start_Application_Submitted'
    ),(NEWID()
    ,'d4e8c720-1aaa-48f5-9772-463415edf52d'
    ,'b46e2dfb-9d47-4d16-866c-b1500eeb26f0'
    ,'Start_Application_Submitted'
    ),(NEWID()
    ,'d4e8c720-1aaa-48f5-9772-463415edf52d'
    ,'70911d8f-8eff-4271-9d6e-bbb29b8d494b'
    ,'Start_Application_Submitted'
    ),
    (NEWID()
    ,'ee641fbf-b645-4e82-8691-8e0bf247ccb9'
    ,'95b9f6b1-f6ce-4dd6-a6c2-cd6e5284c092'
    ,'Admin Action Gateway'
    ),(NEWID()
    ,'d4e8c720-1aaa-48f5-9772-463415edf52d'
    ,'2c5bc0a8-f93c-4118-939d-cdfb004a01e5'
    ,'Start_Application_Submitted'
    ),(NEWID()
    ,'d4e8c720-1aaa-48f5-9772-463415edf52d'
    ,'2f54c4e6-324b-4f2e-a0ba-d546864063da'
    ,'Start_Application_Submitted'
    ),(NEWID()
    ,'d4e8c720-1aaa-48f5-9772-463415edf52d'
    ,'ea063bee-c825-4a5b-b9ae-f326fa74bb28'
    ,'Start_Application_Submitted'
    );
    GO