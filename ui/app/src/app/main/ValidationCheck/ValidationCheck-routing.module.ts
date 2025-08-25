import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ValidationCheckHomeComponent } from './home/ValidationCheck-home.component';
import { ValidationCheckNewComponent } from './new/ValidationCheck-new.component';
import { ValidationCheckDetailComponent } from './detail/ValidationCheck-detail.component';

const routes: Routes = [
  {path: '', component: ValidationCheckHomeComponent},
  { path: 'new', component: ValidationCheckNewComponent },
  { path: ':ValidationID', component: ValidationCheckDetailComponent,
    data: {
      oPermission: {
        permissionId: 'ValidationCheck-detail-permissions'
      }
    }
  }
];

export const VALIDATIONCHECK_MODULE_DECLARATIONS = [
    ValidationCheckHomeComponent,
    ValidationCheckNewComponent,
    ValidationCheckDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ValidationCheckRoutingModule { }