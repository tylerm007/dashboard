import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'Comment-new',
  templateUrl: './Comment-new.component.html',
  styleUrls: ['./Comment-new.component.scss']
})
export class CommentNewComponent {
  @ViewChild("CommentForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {'CommentId': '(newid())', 'CommentType': "('Internal')", 'CreatedDate': '(getutcdate())'}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}