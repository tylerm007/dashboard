import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MessageHomeComponent } from './home/Message-home.component';
import { MessageNewComponent } from './new/Message-new.component';
import { MessageDetailComponent } from './detail/Message-detail.component';

const routes: Routes = [
  {path: '', component: MessageHomeComponent},
  { path: 'new', component: MessageNewComponent },
  { path: ':MessageId', component: MessageDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Message-detail-permissions'
      }
    }
  }
];

export const MESSAGE_MODULE_DECLARATIONS = [
    MessageHomeComponent,
    MessageNewComponent,
    MessageDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class MessageRoutingModule { }