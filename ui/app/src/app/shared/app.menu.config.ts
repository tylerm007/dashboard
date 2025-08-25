import { MenuRootItem } from 'ontimize-web-ngx';

import { CommentCardComponent } from './Comment-card/Comment-card.component';

import { CompanyCardComponent } from './Company-card/Company-card.component';

import { ContactCardComponent } from './Contact-card/Contact-card.component';

import { IngredientCardComponent } from './Ingredient-card/Ingredient-card.component';

import { MessageCardComponent } from './Message-card/Message-card.component';

import { PlantCardComponent } from './Plant-card/Plant-card.component';

import { ProcessDefinitionCardComponent } from './ProcessDefinition-card/ProcessDefinition-card.component';

import { ProcessInstanceCardComponent } from './ProcessInstance-card/ProcessInstance-card.component';

import { ProductCardComponent } from './Product-card/Product-card.component';

import { SysdiagramCardComponent } from './Sysdiagram-card/Sysdiagram-card.component';

import { TaskDefinitionCardComponent } from './TaskDefinition-card/TaskDefinition-card.component';

import { TaskFlowCardComponent } from './TaskFlow-card/TaskFlow-card.component';

import { TaskInstanceCardComponent } from './TaskInstance-card/TaskInstance-card.component';

import { ValidationCheckCardComponent } from './ValidationCheck-card/ValidationCheck-card.component';

import { ValidationResultCardComponent } from './ValidationResult-card/ValidationResult-card.component';

import { ValidationRuleCardComponent } from './ValidationRule-card/ValidationRule-card.component';

import { WFActivityLogCardComponent } from './WFActivityLog-card/WFActivityLog-card.component';

import { WFActivityStatusCardComponent } from './WFActivityStatus-card/WFActivityStatus-card.component';

import { WFApplicationCardComponent } from './WFApplication-card/WFApplication-card.component';

import { WFApplicationStatusCardComponent } from './WFApplicationStatus-card/WFApplicationStatus-card.component';

import { WFCommentCardComponent } from './WFComment-card/WFComment-card.component';

import { WFDashboardCardComponent } from './WFDashboard-card/WFDashboard-card.component';

import { WFFileCardComponent } from './WFFile-card/WFFile-card.component';

import { WFFileTypeCardComponent } from './WFFileType-card/WFFileType-card.component';

import { WFMessageCardComponent } from './WFMessage-card/WFMessage-card.component';

import { WFPriorityCardComponent } from './WFPriority-card/WFPriority-card.component';

import { WFProcessPriorityCardComponent } from './WFProcessPriority-card/WFProcessPriority-card.component';

import { WFProcessStatusCardComponent } from './WFProcessStatus-card/WFProcessStatus-card.component';

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
    
        { id: 'Comment', name: 'COMMENT', icon: 'view_list', route: '/main/Comment' }
    
        ,{ id: 'Company', name: 'COMPANY', icon: 'view_list', route: '/main/Company' }
    
        ,{ id: 'Contact', name: 'CONTACT', icon: 'view_list', route: '/main/Contact' }
    
        ,{ id: 'Ingredient', name: 'INGREDIENT', icon: 'view_list', route: '/main/Ingredient' }
    
        ,{ id: 'Message', name: 'MESSAGE', icon: 'view_list', route: '/main/Message' }
    
        ,{ id: 'Plant', name: 'PLANT', icon: 'view_list', route: '/main/Plant' }
    
        ,{ id: 'ProcessDefinition', name: 'PROCESSDEFINITION', icon: 'view_list', route: '/main/ProcessDefinition' }
    
        ,{ id: 'ProcessInstance', name: 'PROCESSINSTANCE', icon: 'view_list', route: '/main/ProcessInstance' }
    
        ,{ id: 'Product', name: 'PRODUCT', icon: 'view_list', route: '/main/Product' }
    
        ,{ id: 'Sysdiagram', name: 'SYSDIAGRAM', icon: 'view_list', route: '/main/Sysdiagram' }
    
        ,{ id: 'TaskDefinition', name: 'TASKDEFINITION', icon: 'view_list', route: '/main/TaskDefinition' }
    
        ,{ id: 'TaskFlow', name: 'TASKFLOW', icon: 'view_list', route: '/main/TaskFlow' }
    
        ,{ id: 'TaskInstance', name: 'TASKINSTANCE', icon: 'view_list', route: '/main/TaskInstance' }
    
        ,{ id: 'ValidationCheck', name: 'VALIDATIONCHECK', icon: 'view_list', route: '/main/ValidationCheck' }
    
        ,{ id: 'ValidationResult', name: 'VALIDATIONRESULT', icon: 'view_list', route: '/main/ValidationResult' }
    
        ,{ id: 'ValidationRule', name: 'VALIDATIONRULE', icon: 'view_list', route: '/main/ValidationRule' }
    
        ,{ id: 'WFActivityLog', name: 'WFACTIVITYLOG', icon: 'view_list', route: '/main/WFActivityLog' }
    
        ,{ id: 'WFActivityStatus', name: 'WFACTIVITYSTATUS', icon: 'view_list', route: '/main/WFActivityStatus' }
    
        ,{ id: 'WFApplication', name: 'WFAPPLICATION', icon: 'view_list', route: '/main/WFApplication' }
    
        ,{ id: 'WFApplicationStatus', name: 'WFAPPLICATIONSTATUS', icon: 'view_list', route: '/main/WFApplicationStatus' }
    
        ,{ id: 'WFComment', name: 'WFCOMMENT', icon: 'view_list', route: '/main/WFComment' }
    
        ,{ id: 'WFDashboard', name: 'WFDASHBOARD', icon: 'view_list', route: '/main/WFDashboard' }
    
        ,{ id: 'WFFile', name: 'WFFILE', icon: 'view_list', route: '/main/WFFile' }
    
        ,{ id: 'WFFileType', name: 'WFFILETYPE', icon: 'view_list', route: '/main/WFFileType' }
    
        ,{ id: 'WFMessage', name: 'WFMESSAGE', icon: 'view_list', route: '/main/WFMessage' }
    
        ,{ id: 'WFPriority', name: 'WFPRIORITY', icon: 'view_list', route: '/main/WFPriority' }
    
        ,{ id: 'WFProcessPriority', name: 'WFPROCESSPRIORITY', icon: 'view_list', route: '/main/WFProcessPriority' }
    
        ,{ id: 'WFProcessStatus', name: 'WFPROCESSSTATUS', icon: 'view_list', route: '/main/WFProcessStatus' }
    
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

    CommentCardComponent

    ,CompanyCardComponent

    ,ContactCardComponent

    ,IngredientCardComponent

    ,MessageCardComponent

    ,PlantCardComponent

    ,ProcessDefinitionCardComponent

    ,ProcessInstanceCardComponent

    ,ProductCardComponent

    ,SysdiagramCardComponent

    ,TaskDefinitionCardComponent

    ,TaskFlowCardComponent

    ,TaskInstanceCardComponent

    ,ValidationCheckCardComponent

    ,ValidationResultCardComponent

    ,ValidationRuleCardComponent

    ,WFActivityLogCardComponent

    ,WFActivityStatusCardComponent

    ,WFApplicationCardComponent

    ,WFApplicationStatusCardComponent

    ,WFCommentCardComponent

    ,WFDashboardCardComponent

    ,WFFileCardComponent

    ,WFFileTypeCardComponent

    ,WFMessageCardComponent

    ,WFPriorityCardComponent

    ,WFProcessPriorityCardComponent

    ,WFProcessStatusCardComponent

    ,WFQuoteCardComponent

    ,WFQuoteItemCardComponent

    ,WFQuoteStatusCardComponent

    ,WFRoleCardComponent

    ,WFUserCardComponent

    ,WorkflowHistoryCardComponent

];