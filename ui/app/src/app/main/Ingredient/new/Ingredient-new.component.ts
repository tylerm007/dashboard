import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'Ingredient-new',
  templateUrl: './Ingredient-new.component.html',
  styleUrls: ['./Ingredient-new.component.scss']
})
export class IngredientNewComponent {
  @ViewChild("IngredientForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {'Status': "('Original')", 'CreatedDate': '(getdate())', 'IngredientID': '0'}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}