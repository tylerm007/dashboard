import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { WFProductHomeComponent } from './home/WFProduct-home.component';
import { WFProductNewComponent } from './new/WFProduct-new.component';
import { WFProductDetailComponent } from './detail/WFProduct-detail.component';

const routes: Routes = [
  {path: '', component: WFProductHomeComponent},
  { path: 'new', component: WFProductNewComponent },
  { path: ':ProductID', component: WFProductDetailComponent,
    data: {
      oPermission: {
        permissionId: 'WFProduct-detail-permissions'
      }
    }
  },{
    path: ':ProductID/WFIngredient', loadChildren: () => import('../WFIngredient/WFIngredient.module').then(m => m.WFIngredientModule),
    data: {
        oPermission: {
            permissionId: 'WFIngredient-detail-permissions'
        }
    }
}
];

export const WFPRODUCT_MODULE_DECLARATIONS = [
    WFProductHomeComponent,
    WFProductNewComponent,
    WFProductDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class WFProductRoutingModule { }