import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'Contact-new',
  templateUrl: './Contact-new.component.html',
  styleUrls: ['./Contact-new.component.scss']
})
export class ContactNewComponent {
  @ViewChild("ContactForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {'CreatedDate': '(getdate())', 'ContactID': '0'}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}