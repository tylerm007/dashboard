import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'Plant-new',
  templateUrl: './Plant-new.component.html',
  styleUrls: ['./Plant-new.component.scss']
})
export class PlantNewComponent {
  @ViewChild("PlantForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {'OperationalStatus': "('Active')", 'CreatedDate': '(getdate())', 'PlantID': '0'}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}