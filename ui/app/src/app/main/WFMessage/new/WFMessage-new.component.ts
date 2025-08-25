import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'WFMessage-new',
  templateUrl: './WFMessage-new.component.html',
  styleUrls: ['./WFMessage-new.component.scss']
})
export class WFMessageNewComponent {
  @ViewChild("WFMessageForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {'MessageID': '0', 'MessageType': "('outgoing')", 'Priority': "('normal')", 'SentDate': '(getdate())'}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}