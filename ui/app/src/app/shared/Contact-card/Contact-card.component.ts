import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Contact-card.component.html',
  styleUrls: ['./Contact-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Contact-card]': 'true'
  }
})

export class ContactCardComponent {


}