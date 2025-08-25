import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'WFComment-new',
  templateUrl: './WFComment-new.component.html',
  styleUrls: ['./WFComment-new.component.scss']
})
export class WFCommentNewComponent {
  @ViewChild("WFCommentForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {'CommentID': '0', 'CommentType': "('internal')", 'CreatedDate': '(getdate())'}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}