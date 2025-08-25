import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './WFProcessStatus-card.component.html',
  styleUrls: ['./WFProcessStatus-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.WFProcessStatus-card]': 'true'
  }
})

export class WFProcessStatusCardComponent {


}