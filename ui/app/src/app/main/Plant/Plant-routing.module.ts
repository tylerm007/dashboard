import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PlantHomeComponent } from './home/Plant-home.component';
import { PlantNewComponent } from './new/Plant-new.component';
import { PlantDetailComponent } from './detail/Plant-detail.component';

const routes: Routes = [
  {path: '', component: PlantHomeComponent},
  { path: 'new', component: PlantNewComponent },
  { path: ':PlantID', component: PlantDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Plant-detail-permissions'
      }
    }
  }
];

export const PLANT_MODULE_DECLARATIONS = [
    PlantHomeComponent,
    PlantNewComponent,
    PlantDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class PlantRoutingModule { }