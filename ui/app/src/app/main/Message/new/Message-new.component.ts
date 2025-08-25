import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'Message-new',
  templateUrl: './Message-new.component.html',
  styleUrls: ['./Message-new.component.scss']
})
export class MessageNewComponent {
  @ViewChild("MessageForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {'MessageId': '(newid())', 'MessageType': "('Standard')", 'SentDate': '(getutcdate())'}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}