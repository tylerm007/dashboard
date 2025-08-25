import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'Company-new',
  templateUrl: './Company-new.component.html',
  styleUrls: ['./Company-new.component.scss']
})
export class CompanyNewComponent {
  @ViewChild("CompanyForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {'PlantCount': '((0))', 'CreatedDate': '(getdate())', 'LastUpdatedDate': '(getdate())', 'CompanyID': '0'}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}