import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ContactHomeComponent } from './home/Contact-home.component';
import { ContactNewComponent } from './new/Contact-new.component';
import { ContactDetailComponent } from './detail/Contact-detail.component';

const routes: Routes = [
  {path: '', component: ContactHomeComponent},
  { path: 'new', component: ContactNewComponent },
  { path: ':ContactID', component: ContactDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Contact-detail-permissions'
      }
    }
  }
];

export const CONTACT_MODULE_DECLARATIONS = [
    ContactHomeComponent,
    ContactNewComponent,
    ContactDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ContactRoutingModule { }