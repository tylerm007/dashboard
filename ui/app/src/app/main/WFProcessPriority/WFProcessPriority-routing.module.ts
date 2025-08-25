import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { WFProcessPriorityHomeComponent } from './home/WFProcessPriority-home.component';
import { WFProcessPriorityNewComponent } from './new/WFProcessPriority-new.component';
import { WFProcessPriorityDetailComponent } from './detail/WFProcessPriority-detail.component';

const routes: Routes = [
  {path: '', component: WFProcessPriorityHomeComponent},
  { path: 'new', component: WFProcessPriorityNewComponent },
  { path: ':PriorityCode', component: WFProcessPriorityDetailComponent,
    data: {
      oPermission: {
        permissionId: 'WFProcessPriority-detail-permissions'
      }
    }
  },{
    path: ':Priority/ProcessInstance', loadChildren: () => import('../ProcessInstance/ProcessInstance.module').then(m => m.ProcessInstanceModule),
    data: {
        oPermission: {
            permissionId: 'ProcessInstance-detail-permissions'
        }
    }
}
];

export const WFPROCESSPRIORITY_MODULE_DECLARATIONS = [
    WFProcessPriorityHomeComponent,
    WFProcessPriorityNewComponent,
    WFProcessPriorityDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class WFProcessPriorityRoutingModule { }