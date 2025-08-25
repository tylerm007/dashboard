import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { IngredientHomeComponent } from './home/Ingredient-home.component';
import { IngredientNewComponent } from './new/Ingredient-new.component';
import { IngredientDetailComponent } from './detail/Ingredient-detail.component';

const routes: Routes = [
  {path: '', component: IngredientHomeComponent},
  { path: 'new', component: IngredientNewComponent },
  { path: ':IngredientID', component: IngredientDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Ingredient-detail-permissions'
      }
    }
  }
];

export const INGREDIENT_MODULE_DECLARATIONS = [
    IngredientHomeComponent,
    IngredientNewComponent,
    IngredientDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class IngredientRoutingModule { }