import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'ValidationCheck-new',
  templateUrl: './ValidationCheck-new.component.html',
  styleUrls: ['./ValidationCheck-new.component.scss']
})
export class ValidationCheckNewComponent {
  @ViewChild("ValidationCheckForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {'ValidationID': '0', 'LastCheckedDate': '(getdate())'}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}