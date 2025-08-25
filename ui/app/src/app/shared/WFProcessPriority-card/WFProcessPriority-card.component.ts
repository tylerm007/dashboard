import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './WFProcessPriority-card.component.html',
  styleUrls: ['./WFProcessPriority-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.WFProcessPriority-card]': 'true'
  }
})

export class WFProcessPriorityCardComponent {


}