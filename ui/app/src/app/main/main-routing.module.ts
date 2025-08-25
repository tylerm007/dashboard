import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { MainComponent } from './main.component';

export const routes: Routes = [
  {
    path: '', component: MainComponent,
    children: [
        { path: '', redirectTo: 'home', pathMatch: 'full' },
        { path: 'about', loadChildren: () => import('./about/about.module').then(m => m.AboutModule) },
        { path: 'home', loadChildren: () => import('./home/home.module').then(m => m.HomeModule) },
        { path: 'settings', loadChildren: () => import('./settings/settings.module').then(m => m.SettingsModule) },
      
    
        { path: 'Comment', loadChildren: () => import('./Comment/Comment.module').then(m => m.CommentModule) },
    
        { path: 'Company', loadChildren: () => import('./Company/Company.module').then(m => m.CompanyModule) },
    
        { path: 'Contact', loadChildren: () => import('./Contact/Contact.module').then(m => m.ContactModule) },
    
        { path: 'Ingredient', loadChildren: () => import('./Ingredient/Ingredient.module').then(m => m.IngredientModule) },
    
        { path: 'Message', loadChildren: () => import('./Message/Message.module').then(m => m.MessageModule) },
    
        { path: 'Plant', loadChildren: () => import('./Plant/Plant.module').then(m => m.PlantModule) },
    
        { path: 'ProcessDefinition', loadChildren: () => import('./ProcessDefinition/ProcessDefinition.module').then(m => m.ProcessDefinitionModule) },
    
        { path: 'ProcessInstance', loadChildren: () => import('./ProcessInstance/ProcessInstance.module').then(m => m.ProcessInstanceModule) },
    
        { path: 'Product', loadChildren: () => import('./Product/Product.module').then(m => m.ProductModule) },
    
        { path: 'Sysdiagram', loadChildren: () => import('./Sysdiagram/Sysdiagram.module').then(m => m.SysdiagramModule) },
    
        { path: 'TaskDefinition', loadChildren: () => import('./TaskDefinition/TaskDefinition.module').then(m => m.TaskDefinitionModule) },
    
        { path: 'TaskFlow', loadChildren: () => import('./TaskFlow/TaskFlow.module').then(m => m.TaskFlowModule) },
    
        { path: 'TaskInstance', loadChildren: () => import('./TaskInstance/TaskInstance.module').then(m => m.TaskInstanceModule) },
    
        { path: 'ValidationCheck', loadChildren: () => import('./ValidationCheck/ValidationCheck.module').then(m => m.ValidationCheckModule) },
    
        { path: 'ValidationResult', loadChildren: () => import('./ValidationResult/ValidationResult.module').then(m => m.ValidationResultModule) },
    
        { path: 'ValidationRule', loadChildren: () => import('./ValidationRule/ValidationRule.module').then(m => m.ValidationRuleModule) },
    
        { path: 'WFActivityLog', loadChildren: () => import('./WFActivityLog/WFActivityLog.module').then(m => m.WFActivityLogModule) },
    
        { path: 'WFActivityStatus', loadChildren: () => import('./WFActivityStatus/WFActivityStatus.module').then(m => m.WFActivityStatusModule) },
    
        { path: 'WFApplication', loadChildren: () => import('./WFApplication/WFApplication.module').then(m => m.WFApplicationModule) },
    
        { path: 'WFApplicationStatus', loadChildren: () => import('./WFApplicationStatus/WFApplicationStatus.module').then(m => m.WFApplicationStatusModule) },
    
        { path: 'WFComment', loadChildren: () => import('./WFComment/WFComment.module').then(m => m.WFCommentModule) },
    
        { path: 'WFDashboard', loadChildren: () => import('./WFDashboard/WFDashboard.module').then(m => m.WFDashboardModule) },
    
        { path: 'WFFile', loadChildren: () => import('./WFFile/WFFile.module').then(m => m.WFFileModule) },
    
        { path: 'WFFileType', loadChildren: () => import('./WFFileType/WFFileType.module').then(m => m.WFFileTypeModule) },
    
        { path: 'WFMessage', loadChildren: () => import('./WFMessage/WFMessage.module').then(m => m.WFMessageModule) },
    
        { path: 'WFPriority', loadChildren: () => import('./WFPriority/WFPriority.module').then(m => m.WFPriorityModule) },
    
        { path: 'WFProcessPriority', loadChildren: () => import('./WFProcessPriority/WFProcessPriority.module').then(m => m.WFProcessPriorityModule) },
    
        { path: 'WFProcessStatus', loadChildren: () => import('./WFProcessStatus/WFProcessStatus.module').then(m => m.WFProcessStatusModule) },
    
        { path: 'WFQuote', loadChildren: () => import('./WFQuote/WFQuote.module').then(m => m.WFQuoteModule) },
    
        { path: 'WFQuoteItem', loadChildren: () => import('./WFQuoteItem/WFQuoteItem.module').then(m => m.WFQuoteItemModule) },
    
        { path: 'WFQuoteStatus', loadChildren: () => import('./WFQuoteStatus/WFQuoteStatus.module').then(m => m.WFQuoteStatusModule) },
    
        { path: 'WFRole', loadChildren: () => import('./WFRole/WFRole.module').then(m => m.WFRoleModule) },
    
        { path: 'WFUser', loadChildren: () => import('./WFUser/WFUser.module').then(m => m.WFUserModule) },
    
        { path: 'WorkflowHistory', loadChildren: () => import('./WorkflowHistory/WorkflowHistory.module').then(m => m.WorkflowHistoryModule) },
    
    ]
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class MainRoutingModule { }