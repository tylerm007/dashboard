import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'WFProcessPriority-new',
  templateUrl: './WFProcessPriority-new.component.html',
  styleUrls: ['./WFProcessPriority-new.component.scss']
})
export class WFProcessPriorityNewComponent {
  @ViewChild("WFProcessPriorityForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}