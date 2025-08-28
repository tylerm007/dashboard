import { MenuRootItem } from 'ontimize-web-ngx';

import { LaneDefinitionCardComponent } from './LaneDefinition-card/LaneDefinition-card.component';

import { ProcessDefinitionCardComponent } from './ProcessDefinition-card/ProcessDefinition-card.component';

import { ProcessInstanceCardComponent } from './ProcessInstance-card/ProcessInstance-card.component';

import { ProcessMessageCardComponent } from './ProcessMessage-card/ProcessMessage-card.component';

import { ProcessMessageTypeCardComponent } from './ProcessMessageType-card/ProcessMessageType-card.component';

import { ProcessPriorityCardComponent } from './ProcessPriority-card/ProcessPriority-card.component';

import { ProcessStatusCardComponent } from './ProcessStatus-card/ProcessStatus-card.component';

import { StageInstanceCardComponent } from './StageInstance-card/StageInstance-card.component';

import { StageStatusCardComponent } from './StageStatus-card/StageStatus-card.component';

import { SysdiagramCardComponent } from './Sysdiagram-card/Sysdiagram-card.component';

import { TaskCommentCardComponent } from './TaskComment-card/TaskComment-card.component';

import { TaskCommentTypeCardComponent } from './TaskCommentType-card/TaskCommentType-card.component';

import { TaskDefinitionCardComponent } from './TaskDefinition-card/TaskDefinition-card.component';

import { TaskFlowCardComponent } from './TaskFlow-card/TaskFlow-card.component';

import { TaskInstanceCardComponent } from './TaskInstance-card/TaskInstance-card.component';

import { ValidationResultCardComponent } from './ValidationResult-card/ValidationResult-card.component';

import { ValidationRuleCardComponent } from './ValidationRule-card/ValidationRule-card.component';

import { WFActivityLogCardComponent } from './WFActivityLog-card/WFActivityLog-card.component';

import { WFActivityStatusCardComponent } from './WFActivityStatus-card/WFActivityStatus-card.component';

import { WFApplicationCardComponent } from './WFApplication-card/WFApplication-card.component';

import { WFApplicationCommentCardComponent } from './WFApplicationComment-card/WFApplicationComment-card.component';

import { WFApplicationMessageCardComponent } from './WFApplicationMessage-card/WFApplicationMessage-card.component';

import { WFApplicationStatusCardComponent } from './WFApplicationStatus-card/WFApplicationStatus-card.component';

import { WFCompanyCardComponent } from './WFCompany-card/WFCompany-card.component';

import { WFContactCardComponent } from './WFContact-card/WFContact-card.component';

import { WFDashboardCardComponent } from './WFDashboard-card/WFDashboard-card.component';

import { WFFileCardComponent } from './WFFile-card/WFFile-card.component';

import { WFFileTypeCardComponent } from './WFFileType-card/WFFileType-card.component';

import { WFIngredientCardComponent } from './WFIngredient-card/WFIngredient-card.component';

import { WFPlantCardComponent } from './WFPlant-card/WFPlant-card.component';

import { WFPriorityCardComponent } from './WFPriority-card/WFPriority-card.component';

import { WFProductCardComponent } from './WFProduct-card/WFProduct-card.component';

import { WFQuoteCardComponent } from './WFQuote-card/WFQuote-card.component';

import { WFQuoteItemCardComponent } from './WFQuoteItem-card/WFQuoteItem-card.component';

import { WFQuoteStatusCardComponent } from './WFQuoteStatus-card/WFQuoteStatus-card.component';

import { WFRoleCardComponent } from './WFRole-card/WFRole-card.component';

import { WFUserCardComponent } from './WFUser-card/WFUser-card.component';

import { WorkflowHistoryCardComponent } from './WorkflowHistory-card/WorkflowHistory-card.component';


export const MENU_CONFIG: MenuRootItem[] = [
    { id: 'home', name: 'HOME', icon: 'home', route: '/main/home' },
    
    {
    id: 'data', name: ' data', icon: 'remove_red_eye', opened: true,
    items: [
    
        { id: 'LaneDefinition', name: 'LANEDEFINITION', icon: 'view_list', route: '/main/LaneDefinition' }
    
        ,{ id: 'ProcessDefinition', name: 'PROCESSDEFINITION', icon: 'view_list', route: '/main/ProcessDefinition' }
    
        ,{ id: 'ProcessInstance', name: 'PROCESSINSTANCE', icon: 'view_list', route: '/main/ProcessInstance' }
    
        ,{ id: 'ProcessMessage', name: 'PROCESSMESSAGE', icon: 'view_list', route: '/main/ProcessMessage' }
    
        ,{ id: 'ProcessMessageType', name: 'PROCESSMESSAGETYPE', icon: 'view_list', route: '/main/ProcessMessageType' }
    
        ,{ id: 'ProcessPriority', name: 'PROCESSPRIORITY', icon: 'view_list', route: '/main/ProcessPriority' }
    
        ,{ id: 'ProcessStatus', name: 'PROCESSSTATUS', icon: 'view_list', route: '/main/ProcessStatus' }
    
        ,{ id: 'StageInstance', name: 'STAGEINSTANCE', icon: 'view_list', route: '/main/StageInstance' }
    
        ,{ id: 'StageStatus', name: 'STAGESTATUS', icon: 'view_list', route: '/main/StageStatus' }
    
        ,{ id: 'Sysdiagram', name: 'SYSDIAGRAM', icon: 'view_list', route: '/main/Sysdiagram' }
    
        ,{ id: 'TaskComment', name: 'TASKCOMMENT', icon: 'view_list', route: '/main/TaskComment' }
    
        ,{ id: 'TaskCommentType', name: 'TASKCOMMENTTYPE', icon: 'view_list', route: '/main/TaskCommentType' }
    
        ,{ id: 'TaskDefinition', name: 'TASKDEFINITION', icon: 'view_list', route: '/main/TaskDefinition' }
    
        ,{ id: 'TaskFlow', name: 'TASKFLOW', icon: 'view_list', route: '/main/TaskFlow' }
    
        ,{ id: 'TaskInstance', name: 'TASKINSTANCE', icon: 'view_list', route: '/main/TaskInstance' }
    
        ,{ id: 'ValidationResult', name: 'VALIDATIONRESULT', icon: 'view_list', route: '/main/ValidationResult' }
    
        ,{ id: 'ValidationRule', name: 'VALIDATIONRULE', icon: 'view_list', route: '/main/ValidationRule' }
    
        ,{ id: 'WFActivityLog', name: 'WFACTIVITYLOG', icon: 'view_list', route: '/main/WFActivityLog' }
    
        ,{ id: 'WFActivityStatus', name: 'WFACTIVITYSTATUS', icon: 'view_list', route: '/main/WFActivityStatus' }
    
        ,{ id: 'WFApplication', name: 'WFAPPLICATION', icon: 'view_list', route: '/main/WFApplication' }
    
        ,{ id: 'WFApplicationComment', name: 'WFAPPLICATIONCOMMENT', icon: 'view_list', route: '/main/WFApplicationComment' }
    
        ,{ id: 'WFApplicationMessage', name: 'WFAPPLICATIONMESSAGE', icon: 'view_list', route: '/main/WFApplicationMessage' }
    
        ,{ id: 'WFApplicationStatus', name: 'WFAPPLICATIONSTATUS', icon: 'view_list', route: '/main/WFApplicationStatus' }
    
        ,{ id: 'WFCompany', name: 'WFCOMPANY', icon: 'view_list', route: '/main/WFCompany' }
    
        ,{ id: 'WFContact', name: 'WFCONTACT', icon: 'view_list', route: '/main/WFContact' }
    
        ,{ id: 'WFDashboard', name: 'WFDASHBOARD', icon: 'view_list', route: '/main/WFDashboard' }
    
        ,{ id: 'WFFile', name: 'WFFILE', icon: 'view_list', route: '/main/WFFile' }
    
        ,{ id: 'WFFileType', name: 'WFFILETYPE', icon: 'view_list', route: '/main/WFFileType' }
    
        ,{ id: 'WFIngredient', name: 'WFINGREDIENT', icon: 'view_list', route: '/main/WFIngredient' }
    
        ,{ id: 'WFPlant', name: 'WFPLANT', icon: 'view_list', route: '/main/WFPlant' }
    
        ,{ id: 'WFPriority', name: 'WFPRIORITY', icon: 'view_list', route: '/main/WFPriority' }
    
        ,{ id: 'WFProduct', name: 'WFPRODUCT', icon: 'view_list', route: '/main/WFProduct' }
    
        ,{ id: 'WFQuote', name: 'WFQUOTE', icon: 'view_list', route: '/main/WFQuote' }
    
        ,{ id: 'WFQuoteItem', name: 'WFQUOTEITEM', icon: 'view_list', route: '/main/WFQuoteItem' }
    
        ,{ id: 'WFQuoteStatus', name: 'WFQUOTESTATUS', icon: 'view_list', route: '/main/WFQuoteStatus' }
    
        ,{ id: 'WFRole', name: 'WFROLE', icon: 'view_list', route: '/main/WFRole' }
    
        ,{ id: 'WFUser', name: 'WFUSER', icon: 'view_list', route: '/main/WFUser' }
    
        ,{ id: 'WorkflowHistory', name: 'WORKFLOWHISTORY', icon: 'view_list', route: '/main/WorkflowHistory' }
    
    ] 
},
    
    { id: 'settings', name: 'Settings', icon: 'settings', route: '/main/settings'}
    ,{ id: 'about', name: 'About', icon: 'info', route: '/main/about'}
    ,{ id: 'logout', name: 'LOGOUT', route: '/login', icon: 'power_settings_new', confirm: 'yes' }
];

export const MENU_COMPONENTS = [

    LaneDefinitionCardComponent

    ,ProcessDefinitionCardComponent

    ,ProcessInstanceCardComponent

    ,ProcessMessageCardComponent

    ,ProcessMessageTypeCardComponent

    ,ProcessPriorityCardComponent

    ,ProcessStatusCardComponent

    ,StageInstanceCardComponent

    ,StageStatusCardComponent

    ,SysdiagramCardComponent

    ,TaskCommentCardComponent

    ,TaskCommentTypeCardComponent

    ,TaskDefinitionCardComponent

    ,TaskFlowCardComponent

    ,TaskInstanceCardComponent

    ,ValidationResultCardComponent

    ,ValidationRuleCardComponent

    ,WFActivityLogCardComponent

    ,WFActivityStatusCardComponent

    ,WFApplicationCardComponent

    ,WFApplicationCommentCardComponent

    ,WFApplicationMessageCardComponent

    ,WFApplicationStatusCardComponent

    ,WFCompanyCardComponent

    ,WFContactCardComponent

    ,WFDashboardCardComponent

    ,WFFileCardComponent

    ,WFFileTypeCardComponent

    ,WFIngredientCardComponent

    ,WFPlantCardComponent

    ,WFPriorityCardComponent

    ,WFProductCardComponent

    ,WFQuoteCardComponent

    ,WFQuoteItemCardComponent

    ,WFQuoteStatusCardComponent

    ,WFRoleCardComponent

    ,WFUserCardComponent

    ,WorkflowHistoryCardComponent

];