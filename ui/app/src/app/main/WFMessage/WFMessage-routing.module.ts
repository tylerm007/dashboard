import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { WFMessageHomeComponent } from './home/WFMessage-home.component';
import { WFMessageNewComponent } from './new/WFMessage-new.component';
import { WFMessageDetailComponent } from './detail/WFMessage-detail.component';

const routes: Routes = [
  {path: '', component: WFMessageHomeComponent},
  { path: 'new', component: WFMessageNewComponent },
  { path: ':MessageID', component: WFMessageDetailComponent,
    data: {
      oPermission: {
        permissionId: 'WFMessage-detail-permissions'
      }
    }
  }
];

export const WFMESSAGE_MODULE_DECLARATIONS = [
    WFMessageHomeComponent,
    WFMessageNewComponent,
    WFMessageDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class WFMessageRoutingModule { }