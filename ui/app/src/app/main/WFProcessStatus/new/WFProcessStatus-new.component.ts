import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'WFProcessStatus-new',
  templateUrl: './WFProcessStatus-new.component.html',
  styleUrls: ['./WFProcessStatus-new.component.scss']
})
export class WFProcessStatusNewComponent {
  @ViewChild("WFProcessStatusForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}