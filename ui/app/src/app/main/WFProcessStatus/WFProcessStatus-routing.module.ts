import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { WFProcessStatusHomeComponent } from './home/WFProcessStatus-home.component';
import { WFProcessStatusNewComponent } from './new/WFProcessStatus-new.component';
import { WFProcessStatusDetailComponent } from './detail/WFProcessStatus-detail.component';

const routes: Routes = [
  {path: '', component: WFProcessStatusHomeComponent},
  { path: 'new', component: WFProcessStatusNewComponent },
  { path: ':StatusCode', component: WFProcessStatusDetailComponent,
    data: {
      oPermission: {
        permissionId: 'WFProcessStatus-detail-permissions'
      }
    }
  },{
    path: ':Status/ProcessInstance', loadChildren: () => import('../ProcessInstance/ProcessInstance.module').then(m => m.ProcessInstanceModule),
    data: {
        oPermission: {
            permissionId: 'ProcessInstance-detail-permissions'
        }
    }
}
];

export const WFPROCESSSTATUS_MODULE_DECLARATIONS = [
    WFProcessStatusHomeComponent,
    WFProcessStatusNewComponent,
    WFProcessStatusDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class WFProcessStatusRoutingModule { }