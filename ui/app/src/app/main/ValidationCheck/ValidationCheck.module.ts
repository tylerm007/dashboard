import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {VALIDATIONCHECK_MODULE_DECLARATIONS, ValidationCheckRoutingModule} from  './ValidationCheck-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    ValidationCheckRoutingModule
  ],
  declarations: VALIDATIONCHECK_MODULE_DECLARATIONS,
  exports: VALIDATIONCHECK_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class ValidationCheckModule { }