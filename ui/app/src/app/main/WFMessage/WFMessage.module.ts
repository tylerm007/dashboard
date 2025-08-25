import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {WFMESSAGE_MODULE_DECLARATIONS, WFMessageRoutingModule} from  './WFMessage-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    WFMessageRoutingModule
  ],
  declarations: WFMESSAGE_MODULE_DECLARATIONS,
  exports: WFMESSAGE_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class WFMessageModule { }