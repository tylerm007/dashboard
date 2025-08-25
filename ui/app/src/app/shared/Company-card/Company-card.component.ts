import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Company-card.component.html',
  styleUrls: ['./Company-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Company-card]': 'true'
  }
})

export class CompanyCardComponent {


}