import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ProcessInstanceHomeComponent } from './home/ProcessInstance-home.component';
import { ProcessInstanceNewComponent } from './new/ProcessInstance-new.component';
import { ProcessInstanceDetailComponent } from './detail/ProcessInstance-detail.component';

const routes: Routes = [
  {path: '', component: ProcessInstanceHomeComponent},
  { path: 'new', component: ProcessInstanceNewComponent },
  { path: ':InstanceId', component: ProcessInstanceDetailComponent,
    data: {
      oPermission: {
        permissionId: 'ProcessInstance-detail-permissions'
      }
    }
  },{
    path: ':InstanceId/Comment', loadChildren: () => import('../Comment/Comment.module').then(m => m.CommentModule),
    data: {
        oPermission: {
            permissionId: 'Comment-detail-permissions'
        }
    }
},{
    path: ':InstanceId/Message', loadChildren: () => import('../Message/Message.module').then(m => m.MessageModule),
    data: {
        oPermission: {
            permissionId: 'Message-detail-permissions'
        }
    }
},{
    path: ':InstanceId/TaskInstance', loadChildren: () => import('../TaskInstance/TaskInstance.module').then(m => m.TaskInstanceModule),
    data: {
        oPermission: {
            permissionId: 'TaskInstance-detail-permissions'
        }
    }
},{
    path: ':InstanceId/ValidationResult', loadChildren: () => import('../ValidationResult/ValidationResult.module').then(m => m.ValidationResultModule),
    data: {
        oPermission: {
            permissionId: 'ValidationResult-detail-permissions'
        }
    }
},{
    path: ':InstanceId/WorkflowHistory', loadChildren: () => import('../WorkflowHistory/WorkflowHistory.module').then(m => m.WorkflowHistoryModule),
    data: {
        oPermission: {
            permissionId: 'WorkflowHistory-detail-permissions'
        }
    }
}
];

export const PROCESSINSTANCE_MODULE_DECLARATIONS = [
    ProcessInstanceHomeComponent,
    ProcessInstanceNewComponent,
    ProcessInstanceDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ProcessInstanceRoutingModule { }