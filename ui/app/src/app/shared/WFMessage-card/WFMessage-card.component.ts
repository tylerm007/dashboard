import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './WFMessage-card.component.html',
  styleUrls: ['./WFMessage-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.WFMessage-card]': 'true'
  }
})

export class WFMessageCardComponent {


}