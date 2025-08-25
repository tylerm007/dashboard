import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {WFPROCESSSTATUS_MODULE_DECLARATIONS, WFProcessStatusRoutingModule} from  './WFProcessStatus-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    WFProcessStatusRoutingModule
  ],
  declarations: WFPROCESSSTATUS_MODULE_DECLARATIONS,
  exports: WFPROCESSSTATUS_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class WFProcessStatusModule { }