import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {INGREDIENT_MODULE_DECLARATIONS, IngredientRoutingModule} from  './Ingredient-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    IngredientRoutingModule
  ],
  declarations: INGREDIENT_MODULE_DECLARATIONS,
  exports: INGREDIENT_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class IngredientModule { }