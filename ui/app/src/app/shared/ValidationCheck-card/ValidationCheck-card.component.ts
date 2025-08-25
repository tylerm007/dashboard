import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './ValidationCheck-card.component.html',
  styleUrls: ['./ValidationCheck-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.ValidationCheck-card]': 'true'
  }
})

export class ValidationCheckCardComponent {


}