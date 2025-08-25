import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {WFPROCESSPRIORITY_MODULE_DECLARATIONS, WFProcessPriorityRoutingModule} from  './WFProcessPriority-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    WFProcessPriorityRoutingModule
  ],
  declarations: WFPROCESSPRIORITY_MODULE_DECLARATIONS,
  exports: WFPROCESSPRIORITY_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class WFProcessPriorityModule { }